import pandas as pd

def mask_email(email):
    if not email:
        return None
    name, domain = email.split("@")
    return name[:2] + "****@" + domain

def mask_phone(phone):
    digits = "".join(filter(str.isdigit, phone))
    return "******" + digits[-4:]

def parse_epoch(val):
    try:
        return pd.to_datetime(int(str(val).split(":")[-1]), unit="s")
    except:
        return None

def clean_json(records):
    users, phones, jobs = [], [], []

    for r in records:
        uid = r["user_id"]

        users.append({
            "user_id": uid,
            "name": r["user_details"]["name"],
            "username": mask_email(r["user_details"]["username"]),
            "dob": r["user_details"]["dob"],
            "address": r["user_details"]["address"],
            "created_at": parse_epoch(r["created_at"]),
            "updated_at": parse_epoch(r["updated_at"])
        })

        for p in r["user_details"]["telephone_numbers"]:
            phones.append({
                "user_id": uid,
                "phone": mask_phone(p)
            })

        for j in r["jobs_history"]:
            jobs.append({
                "job_id": j["id"],
                "user_id": uid,
                "occupation": j["occupation"],
                "is_fulltime": j["is_fulltime"],
                "start": j["start"],
                "end": j["end"],
                "logged_at": pd.to_datetime(r["logged_at"], unit="s")
            })

    return pd.DataFrame(users), pd.DataFrame(phones), pd.DataFrame(jobs)
