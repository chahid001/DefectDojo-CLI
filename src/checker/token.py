import requests
import loading.load as loading

def check_token(url, token):
    try:
        response = requests.get(f'{url}api/v2/users/me/', headers=token)
    except:
        return 4
    if response.status_code == 404:
        return 5
    elif response.status_code == 403:
        return 6
  
