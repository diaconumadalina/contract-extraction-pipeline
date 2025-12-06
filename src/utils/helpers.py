import re


def extract_json(text: str) -> str:
    """
    Removes markdown fences and extracts raw JSON.
    """
    text = text.strip()

    # remove ```json ... ```
    text = re.sub(r"```json", "", text, flags=re.IGNORECASE)
    text = re.sub(r"```", "", text)

    # find first { ... }
    json_match = re.search(r"\{.*\}", text, flags=re.DOTALL)
    if json_match:
        return json_match.group(0)

    return text
