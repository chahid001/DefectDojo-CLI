import requests
import json
import loading.load as loading

def create_product(url, product_name, product_type, tags, token): 

    headers = token
    data = {
        "name": product_name,
        "description": f"Scan Reports for {product_name}",
        "prod_type": product_type,
        "tags": tags,
    }   
    response = requests.post(f"{url}api/v2/products/", headers=headers, json=data)  
    
    if "product with this name already exists." in response.json()["name"]:
        loading.print_c("Product already exist........ ♻️", "MAGENTA")
    else:
        loading.print_c("Project got created ✅", "GREEN")
    id_response = requests.get(f"{url}api/v2/products/?name={product_name}", headers=headers, json=data)
    data = json.loads(id_response.text)

    return data['results'][0]['id']