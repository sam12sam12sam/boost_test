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
        if isinstance(r, str):
            try:
                r = json.loads(r)
            except (json.JSONDecodeError, TypeError):
                continue # Skip invalid records

        uid = r.get("user_id", "")
        details = r.get("user_details", {})
        
        if not isinstance(details, dict):
            details = {}

        users.append({
            "user_id": uid,
            "name": details.get("name", ""),
            "username": mask_email(details.get("username", "")),
            "dob": details.get("dob", ""),
            "address": details.get("address", ""),
            "created_at": parse_epoch(r.get("created_at", "")),
            "updated_at": parse_epoch(r.get("updated_at", ""))
        })

        for p in details.get("telephone_numbers", []):
            phones.append({
                "user_id": uid,
                "phone": mask_phone(p)
            })

        for j in r.get("jobs_history", []):
            # Ensure nested job 'j' is also a dictionary
            if isinstance(j, dict):
                jobs.append({
                    "job_id": j.get("id", ""),
                    "user_id": uid,
                    "occupation": j.get("occupation", ""),
                    "is_fulltime": j.get("is_fulltime", ""),
                    "start": j.get("start", ""),
                    "end": j.get("end", ""),
                    "logged_at": pd.to_datetime(r.get("logged_at", 0), unit="s") if r.get("logged_at") else ""
                })

    return pd.DataFrame(users), pd.DataFrame(phones), pd.DataFrame(jobs)
