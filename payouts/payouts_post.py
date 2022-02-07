# The 'requests' library for Python can be used to make calls to the MoneyMoov API in
# popular python frameworks such as Django and Flask.
import os, requests

# Remember, the JWT access token must be securely stored ('os' module above allows storage in environment variable)
jwtToken = os.environ['NOFRIXION_DEV_TOKEN']

url = "https://api-dev.nofrixion.com/api/v1/payouts"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {jwtToken}"
}

paymentData = {
    "AccountID": "A120P0JR",
    "Currency": "EUR",
    "Amount": "2.34",
    "YourReference": "My reference",
    "DestinationIBAN": "GB94BARC10201530093459",
    "DestinationAccountName": "Destination Name",
    "TheirReference": "Their reference"
}

response = requests.request("POST", url, headers=headers, data=paymentData)

# Process response
print(response.status_code)
print(response.reason)
