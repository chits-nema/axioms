# report_generator.py
from fpdf import FPDF
import io

def generate_report_html(product: str, rankings: list[dict], recommendation: dict, criteria: list[dict]) -> str:
    # Keep this if anything else calls it, or delete if only PDF is used
    return "<html><body><p>Report</p></body></html>"

def generate_report_pdf(product: str, rankings: list[dict], recommendation: dict, criteria: list[dict]) -> bytes:
    criteria_labels = {c["key"]: c["label"] for c in criteria}
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, f"Evaluation Report: {product}", ln=True)
    
    pdf.set_font("Helvetica", "B", 12)
    pdf.ln(5)
    pdf.cell(0, 8, "Rankings", ln=True)
    
    pdf.set_font("Helvetica", size=10)
    for rank in rankings:
        pdf.cell(0, 7, f"  {rank.get('vendor', '')} — Score: {rank.get('score', '')}", ln=True)
    
    pdf.ln(5)
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 8, "Recommendation", ln=True)
    pdf.set_font("Helvetica", size=10)
    pdf.multi_cell(0, 7, str(recommendation))
    
    return bytes(pdf.output())