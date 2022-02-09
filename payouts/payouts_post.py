#-----------------------------------------------------------------------------
# Description: Example of calling the NoFrixion MoneyMoov API payouts POST 
# method. It provides a way to initiate funds transfer to third party accounts
#
# Usage:
# 1. Create a user access token in the sandbox portal at:
#    https:#portal-sandbox.nofrixion.com.
# 2. Set the token as an environment variable in your console:
#    set NOFRIXION_SANDBOX_TOKEN=<JWT token from previous step>
# 3. Run the script using the command: python -u "filename"
# 4. If successful user the newly created payout ID will be displayed.
#-----------------------------------------------------------------------------

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
