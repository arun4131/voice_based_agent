# ---- Mock Government Jobs ----
JOBS = [
    {
        "title": "గ్రూప్-4 క్లర్క్",
        "department": "APPSC",
        "location": "Hyderabad",
        "education": "degree"
    },
    {
        "title": "జూనియర్ అసిస్టెంట్",
        "department": "Secretariat",
        "location": "Vijayawada",
        "education": "degree"
    },
    {
        "title": "పంచాయతీ కార్యదర్శి",
        "department": "Rural Development",
        "location": "Guntur",
        "education": "degree"
    },
    {
        "title": "టెక్నికల్ అసిస్టెంట్",
        "department": "Irrigation",
        "location": "Hyderabad",
        "education": "diploma"
    }
]


# ---- Mock Government Schemes ----
SCHEMES = [
    {
        "name": "YSR ఆసరా",
        "min_age": 18,
        "max_age": 60,
        "education": None,
        "gender": "female"
    },
    {
        "name": "YSR రైతు భరోసా",
        "min_age": 18,
        "max_age": 65,
        "education": None,
        "gender": None
    },
    {
        "name": "విద్యా దీవెన",
        "min_age": 15,
        "max_age": 25,
        "education": "degree",
        "gender": None
    }
]


def check_jobs(memory):
    user_loc = memory.get("location", "").lower()
    user_edu = memory.get("education", "").lower()

    same_location_jobs = []
    other_location_jobs = []

    for job in JOBS:
        if job["education"].lower() != user_edu:
            continue

        job_text = f'{job["title"]} ({job["department"]}, {job["location"]})'

        # Priority 1: same location
        if job["location"].lower() == user_loc:
            same_location_jobs.append(job_text)
        else:
            other_location_jobs.append(job_text)

    # Case 1: Found jobs in same location (any department)
    if same_location_jobs:
        return {
            "status": "FOUND",
            "results": same_location_jobs
        }

    # Case 2: Found jobs in other locations (any department)
    if other_location_jobs:
        return {
            "status": "ALTERNATIVE",
            "results": other_location_jobs
        }

    # Case 3: No government jobs at all
    return {
        "status": "NONE"
    }



def check_schemes(memory):
    age = int(memory.get("age", 0))
    edu = memory.get("education")
    gender = memory.get("gender")

    eligible = []

    for s in SCHEMES:
        if not (s["min_age"] <= age <= s["max_age"]):
            continue
        if s["education"] and s["education"] != edu:
            continue
        if s["gender"] and s["gender"] != gender:
            continue

        eligible.append(s["name"])

    return eligible
