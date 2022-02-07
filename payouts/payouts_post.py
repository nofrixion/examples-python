# The 'requests' library for Python can be used to make calls to the MoneyMoov API in
# popular python frameworks such as Django and Flask.
import requests
import os

# Remember, the JWT access token must be securely stored ('os' module above allows storage in environment variable)
jwtToken = os.environ['NOFRIXION_SANDBOX_TOKEN']

url = "https://api-sandbox.nofrixion.com/api/v1/payouts"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {jwtToken}"
}

paymentData = {
    "AccountID": "A120P0JR",
    "Currency": "EUR",
    "Amount": "1.00",
    "YourReference": "My reference",
    "DestinationIBAN": "GB33BUKB20201555555555",
    "DestinationAccountName": "Destination Name",
    "TheirReference": "Their reference"
}

response = requests.request("POST", url, headers=headers, data=paymentData)

# On successful payout creation, the API returns the payout ID (UUID format)
print(response.text)
