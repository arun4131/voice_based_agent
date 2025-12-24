def job_eligibility(age, edu, gender):
    jobs = []

    if age is None or edu is None:
        return []

    if 18 <= age <= 35:
        if edu in ["degree", "pg"]:
            jobs.append("అఫీసర్ / Officer పోస్టులు")
        elif edu == "diploma":
            jobs.append("జూనియర్ ఇంజనీర్ పోస్టులు")
        elif edu in ["10th", "12th"]:
            jobs.append("గ్రూప్ D / క్లర్క్")

    return jobs


def scheme_eligibility(age, edu, gender):
    schemes = []

    if gender == "female":
        schemes.append("మహిళా సంక్షేమ పథకం")

    if age is not None and age <= 25 and edu in ["12th", "degree", "pg"]:
        schemes.append("విద్యార్థులకు స్కాలర్‌షిప్ పథకం")

    if edu in ["10th", "12th", "diploma"]:
        schemes.append("స్కిల్ డెవలప్‌మెంట్ పథకం")

    if age is not None and 18 <= age <= 35:
        schemes.append("యూత్ ఎంకరేజ్‌మెంట్ పథకం")

    return schemes
