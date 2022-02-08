# Transfers money between merchant accounts

# The 'requests' library for Python can be used to make calls to the MoneyMoov API in
# popular python frameworks such as Django and Flask.
import requests
import os

# Remember, the JWT access token must be securely stored ('os' module above allows storage in environment variable)
jwtToken = os.environ['NOFRIXION_SANDBOX_TOKEN']

url = "https://api-sandbox.nofrixion.com/api/v1/transfers"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {jwtToken}"
}

transferData = {
    "Amount": "1.00",
    "Currency": "EUR",
    "SourceAccount": "A120R2Y3",
    "DestinationAccount": "A120P0JR",
    "Reference": "My reference",
    "ExternalReference": "Ext reference"
}

response = requests.request("POST", url, headers=headers, data=transferData)

# Process response
print(response.status_code)  # 201 on success
print(response.content) # JSON with transfer details
