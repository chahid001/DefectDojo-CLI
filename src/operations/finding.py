import requests
import loading.load as loading

def uploadToDefectDojo(url, product_id, product_type, eng_id, scan, filename, token):


    multipart_form_data = {
        'file': (filename, open(filename, 'rb')),
        'scan_type': (None, scan),
        'product': (None, product_id),
        'engagement': (None, eng_id),
        'product_type': (None, product_type),
    }
    uri = f'{url}/api/v2/import-scan/'
    response = requests.post(
        uri,
        files=multipart_form_data,
        headers=token
    )