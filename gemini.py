from google import genai
from config import API_KEY

client = genai.Client(api_key=API_KEY)
MODEL = "models/gemini-flash-latest"

USED = False   # 🔒 ensures only one call


def ask_gemini_for_intent(user_text):
    global USED
    if USED:
        return None
    USED = True

    prompt = f"""
యూజర్ ఇలా చెప్పాడు: "{user_text}"

అతను ఏం కావాలనుకుంటున్నాడు?
కేవలం ఒక పదం మాత్రమే ఇవ్వండి:
"job" లేదా "scheme"
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )
    text = response.text.lower()

    if "job" in text:
        return "job"
    return "scheme"
