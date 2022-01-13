import requests

url = "https://api.meraki.com/api/v1/networks/N_628815097971626163"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "2ecc538a20050c22c0e5fa4912297d1b727877f1"
}

response = requests.request('DELETE', url, headers=headers, data = payload)

print(response.status_code)

