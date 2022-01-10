import requests

url = "https://api.meraki.com/api/v1/organizations"

payload = '''{ "name": "DevNet" }'''

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "2ecc538a20050c22c0e5fa4912297d1b727877f1"
}

response = requests.request('POST', url, headers=headers, data = payload)

print(response.text.encode('utf8'))



