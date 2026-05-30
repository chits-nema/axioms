from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from catalogue_to_context.retriever import get_vendor_context
from typing import Optional, List
from fastapi import APIRouter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import os

# Initialize the router. 
# This automatically prepends '/catalog' to all endpoints in this file.
router = APIRouter(
    prefix="/catalog",
    tags=["Catalog Evaluation"]
)


llm = None  # Ask chits

class PurchaseRequest(BaseModel):
    product: str = Field(..., description="The name of the product to evaluate (e.g., 'CRM Software')")
    metrics: List[str] = Field(default=[], description="Optional list of evaluation metrics. Generated if empty.")
    category: Optional[str] = Field(default=None, description="Optional folder category filter (e.g., 'crm', 'laptops')")
    vendors: List[str] = Field(default=[], description="Optional specific list of vendors to filter by")


class VendorScore(BaseModel):
    vendor_name: str = Field(description="The name of the vendor")
    scores: dict[str, int] = Field(description="Dictionary mapping each metric name to a score from 1-10")
    final_weighted_score: float = Field(description="The calculated mathematical score factoring in user weights")
    justification: str = Field(description="A 1-sentence reason defending this specific score based on catalog evidence")


class FinalRecommendation(BaseModel):
    rankings: List[VendorScore] = Field(description="List of evaluated vendors ranked from highest score to lowest")
    summary: str = Field(description="A high-level executive summary detailing why the top choice is recommended")


@router.post("/evaluate", response_model=dict)
async def evaluate_catalog_purchase(request: PurchaseRequest):
    try:
        # --- STEP 1: Auto-Generate Metrics if Missing ---
        if not request.metrics:
            print(f"No metrics provided for '{request.product}'. Auto-generating metrics via LLM...")
            
            metric_prompt = ChatPromptTemplate.from_messages([
                ("system", "You are an expert procurement consultant. The user wants to purchase '{product}'. "
                           "Identify and return a JSON list containing exactly the 4 most critical evaluation metrics "
                           "for this product category. Return ONLY a raw JSON array of strings."),
            ])
            
            # Use a basic JSON parser to extract the raw list of strings
            metric_chain = metric_prompt | llm | JsonOutputParser()
            request.metrics = metric_chain.invoke({"product": request.product})
            print(f"Successfully generated metrics: {request.metrics}")

        # --- STEP 2: Weigh the Metrics ---
        
        #weighed_map = kanayas

        # --- STEP 3: Retrieve Context from VectorDB 
        vendor_data = get_vendor_context(
            product=request.product,
            metrics=request.metrics,
            category=request.category,
            vendors=request.vendors if request.vendors else None
        )

        if not vendor_data:
            raise HTTPException(status_code=404, detail="No relevant vendor documents found in the database.")

        # --- STEP 4: Format Retrieved Snippets for the Prompt ---

        context_string = ""
        for vendor, chunks in vendor_data.items():
            vendor_text = "\n".join(chunks) if isinstance(chunks, list) else chunks
            context_string += f"\n\n### VENDOR: {vendor} ###\n{vendor_text}\n"

        # --- STEP 5: Set up the Final Decision Engine Chain ---
        parser = JsonOutputParser(pydantic_object=FinalRecommendation)
        
        evaluation_prompt = ChatPromptTemplate.from_messages([
            ("system", "You are an impartial corporate purchasing agent. "
                       "Evaluate the vendors using ONLY the verified facts from the provided Vendor Context. "
                       "Do not invent facts, features, or figures outside the text.\n\n"
                       "The user has assigned these importance weights to the metrics (out of 10): {weights}.\n"
                       "For each vendor, score them 1-10 on each metric, calculate their final weighted score, "
                       "and sort them from highest to lowest.\n\n"
                       "{format_instructions}"),
            ("user", "Vendor Context:\n{context}")
        ])

        generation_chain = evaluation_prompt | llm | parser

        # --- STEP 6: Execute and Return Structure ---
        print("Executing final vendor matrix generation via LLM...")
        llm_response = generation_chain.invoke({
            #"weights": weighed_map,
            "context": context_string,
            "format_instructions": parser.get_format_instructions()
        })

        return {
            "status": "success",
            "evaluated_product": request.product,
            #"metrics_used": weighed_map,
            "evaluation_results": llm_response
        }

    except Exception as e:
        # Catch unexpected pipeline bugs cleanly without crashing the worker instance
        raise HTTPException(status_code=500, detail=f"Evaluation Pipeline Error: {str(e)}")