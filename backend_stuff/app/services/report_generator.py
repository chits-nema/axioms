# report_generator.py
from weasyprint import HTML, CSS

def generate_report_html(product: str, rankings: list[dict], recommendation: dict, criteria: list[dict]) -> str:
    criteria_labels = {c["key"]: c["label"] for c in criteria}
    
    # build vendor rows
    vendor_rows = ""
    for rank, vendor in enumerate(rankings, 1):
        vendor_rows += f"<tr><td>#{rank}</td><td><strong>{vendor['vendor']}</strong></td>"
        for c in criteria:
            score = vendor.get(c["key"], "-")
            weighted = vendor.get(f"{c['key']}_weighted", "-")
            vendor_rows += f"<td>{score} <small>({weighted})</small></td>"
        vendor_rows += f"<td><strong>{vendor['weighted_score']}</strong></td></tr>"

    # build criteria headers
    criteria_headers = "".join(f"<th>{c['label']}</th>" for c in criteria)

    return f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; padding: 40px; color: #333; }}
            h1 {{ color: #1a1a2e; }}
            h2 {{ color: #16213e; border-bottom: 2px solid #0f3460; padding-bottom: 8px; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 20px; font-size: 10px; }}
            th {{ background: #0f3460; color: white; padding: 10px; text-align: left; }}
            td {{ padding: 5px 6px; border-bottom: 1px solid #ddd; max-width: 80px}}
            tr:nth-child(even) {{ background: #f5f5f5; }}
            tr:first-child td {{ background: #e8f4e8; font-weight: bold; }}
            .recommendation {{ background: #e8f4e8; border-left: 4px solid #2d6a4f; padding: 20px; margin: 20px 0; border-radius: 4px; }}
            .meta {{ color: #666; font-size: 13px; margin-bottom: 30px; }}
        </style>
    </head>
    <body>
        <h1>Vendor Evaluation Report</h1>
        <p class="meta">Product: <strong>{product}</strong> &nbsp;|&nbsp; Generated: {__import__('datetime').date.today()}</p>

        <h2>Recommendation</h2>
        <div class="recommendation">
            <strong>Recommended Vendor: {recommendation['recommended_vendor']}</strong><br><br>
            {recommendation['reasoning']}<br><br>
            <em>Trade-offs: {recommendation['trade_offs']}</em>
        </div>

        <h2>Comparison Matrix</h2>
        <table>
            <thead>
                <tr>
                    <th>#</th>
                    <th>Vendor</th>
                    {criteria_headers}
                    <th>Weighted Score</th>
                </tr>
            </thead>
            <tbody>
                {vendor_rows}
            </tbody>
        </table>
    </body>
    </html>
    """

def generate_report_pdf(product: str, rankings: list, recommendation: dict, criteria: list) -> bytes:
    html = generate_report_html(product, rankings, recommendation, criteria)
    css = CSS(string="@page { size: A4 landscape; margin: 1cm;}")
    return HTML(string=html).write_pdf(stylesheets=[css])