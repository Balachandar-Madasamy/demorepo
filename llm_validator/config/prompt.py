# Step 2: Build prompt for LLM
# prompt = f"""
#     You are an expert financial document parser.
#     Extract the following fields from the term sheet text and return ONLY JSON:
#
#     - Issuer
#     - Instrument
#     - Principal Amount
#     - Coupon
#     - Maturity Date
#     - Issue Date
#     - Governing Law
#     - Use of Proceeds
#
#     Term Sheet Text:
#     """
prompt = """
You are an expert financial document parser.
Extract as JSON with keys:
Issuer, Instrument, Principal Amount, Coupon, Maturity Date, Issue Date, Governing Law, Use of Proceeds
Return ONLY valid JSON. No extra words, no markdown, no explanations.
Term Sheet Text:
"""
