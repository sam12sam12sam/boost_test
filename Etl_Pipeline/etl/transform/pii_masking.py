def mask_email(email):
    if not email or "@" not in email:
        return email
    name, domain = email.split("@")
    return name[:2] + "****@" + domain

def mask_phone(phone):
    if not phone:
        return phone
    return "******" + phone[-4:]
