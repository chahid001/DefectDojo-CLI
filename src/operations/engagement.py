import requests
import loading.load as loading


def create_engagement(url, name, product_id, token, date):
    headers = token
    data = {
        "name": name,
        "description": f"This is the engagement of the pipeline ID {name}",
        "product": product_id,
        "target_start": date,
        "target_end": date,
    }
    response = requests.post(f"{url}api/v2/engagements/", headers=headers, json=data) 
    if response.status_code == 201:
        loading.print_c("Engagment got created ✅", "GREEN")
    else:
        loading.print_c("An error has occured ❌", "RED")
    id = response.json().get("id")
    return id