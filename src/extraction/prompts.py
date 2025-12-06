BASE_EXTRACTION_PROMPT = """
Extract structured information from the contract text below.

Return ONLY valid JSON. No commentary. No code blocks.

Required fields:
- contract_title
- buyer
- supplier
- contract_value
- start_date
- end_date

If a field is missing, return null.

JSON schema:
{{
  "contract_title": "",
  "buyer": "",
  "supplier": "",
  "contract_value": "",
  "start_date": "",
  "end_date": ""
}}
"""
