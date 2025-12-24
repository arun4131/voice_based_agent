from speech import speak, listen
from memory import init_memory
from tools import check_jobs, check_schemes
from gemini import ask_gemini_for_intent

GENDER_MAP = {
    "అమ్మాయి": "female",
    "స్త్రీ": "female",
    "మగాడు": "male",
    "పురుషుడు": "male"
}
EDUCATION_MAP = {
    "10వ తరగతి": "10th",
    "12వ తరగతి": "12th",
    "డిప్లొమా": "diploma",
    "డిగ్రీ": "degree",
    "పీజీ": "pg"
}
LOCATION_MAP = {
    "హైదరాబాద్": "Hyderabad",
    "విజయవాడ": "Vijayawada",
    "గుంటూరు": "Guntur"
}
LOCATION_REVERSE_MAP = {
    "Hyderabad": "హైదరాబాద్",
    "Vijayawada": "విజయవాడ",
    "Guntur": "గుంటూరు"
}



QUESTIONS_TE = {
    
    "age": "మీ వయస్సు ఎంత?",
    "education": "మీ విద్య ఏమిటి? (10వ తరగతి / 12వ తరగతి / డిప్లొమా / డిగ్రీ / పీజీ)",
    "department": "మీకు ఏ ప్రభుత్వ శాఖలో ఉద్యోగం కావాలి? (ఏపీపీఎస్సీ / సచివాలయం / గ్రామీణ అభివృద్ధి / నీటిపారుదల)",
    "location": "మీరు ఉద్యోగం చేయాలనుకునే ప్రాంతం ఏది?",
    "gender": "మీ లింగం ఏమిటి?"
}




def main():
    memory = init_memory()

    # Greeting
    speak("నమస్తే. నేను ప్రభుత్వ సేవల సహాయకుడిని.")

    # -------- Intent (Gemini ONLY ONCE) --------
    speak("మీకు ఉద్యోగ సమాచారం కావాలా లేదా ప్రభుత్వ పథకాలు కావాలా?")
    user_text = listen()
    intent = ask_gemini_for_intent(user_text)
    memory["intent"] = intent

    # -------- Fixed questions (Rule-based) --------
    # Basic details (for both job & scheme)
    for field in ["age", "education", "gender"]:
        speak(QUESTIONS_TE[field])
        spoken = listen()

        if field == "gender":
            memory["gender"] = GENDER_MAP.get(spoken, None)

        elif field == "education":
            memory["education"] = EDUCATION_MAP.get(spoken, None)

        else:
            
            if field == "location":
                memory["location"] = LOCATION_MAP.get(spoken, spoken)
            else:
                memory[field] = spoken



    # Extra questions only for job intent
    if memory["intent"] == "job":
        for field in ["department", "location"]:
            speak(QUESTIONS_TE[field])
            spoken = listen()

            if field == "gender":
                memory["gender"] = GENDER_MAP.get(spoken, None)

            elif field == "education":
                memory["education"] = EDUCATION_MAP.get(spoken, None)

            else:
                memory[field] = spoken


    # -------- Tools --------
    if memory["intent"] == "job":
        result = check_jobs(memory)

        if result["status"] == "FOUND":
            speak("మీకు సరిపోయే ఉద్యోగాలు ఇవి.")
            speak(", ".join(result["results"]))

        elif result["status"] == "ALTERNATIVE":
            speak("మీరు ఎంచుకున్న ప్రాంతంలో ఉద్యోగాలు లేవు.")
            speak(
                "కానీ ఈ ప్రాంతాలలో ఉన్నాయి: " +
                ", ".join(result["results"])
            )

        else:
            speak("మీకు సరిపోయే ఉద్యోగాలు ప్రస్తుతం లభించలేదు.")

    else:
        schemes = check_schemes(memory)
        if schemes:
            speak("మీకు సరిపోయే ప్రభుత్వ పథకాలు ఇవి.")
            speak(", ".join(schemes))
        else:
            speak("మీకు సరిపోయే ప్రభుత్వ పథకాలు లభించలేదు.")


if __name__ == "__main__":
    main()
