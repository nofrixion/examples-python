#-----------------------------------------------------------------------------
# Description: Example of calling the NoFrixion MoneyMoov API payouts PUT 
# method. It provides a convenient way to modify a previously created payout
#
# Usage:
# 1. Create a user access token in the sandbox portal at:
#    https:#portal-sandbox.nofrixion.com.
# 2. Set the token as an environment variable in your console:
#    set NOFRIXION_USER_TOKEN=<JWT token from previous step>
# 3. Run the script using the command: python -u "filename"
# 4. If successful user the updated payout object will be displayed.
#-----------------------------------------------------------------------------

# The 'requests' library for Python can be used to make calls to the MoneyMoov API in popular python frameworks such as Django and Flask.
import requests
import os

# Remember, the JWT access token must be securely stored ('os' module above allows storage in environment variable)
jwtToken = os.environ['NOFRIXION_USER_TOKEN']

baseUrl = "https://api-sandbox.nofrixion.com/api/v1/payouts"

# id of payout to update must be specified
payoutId = "432629ae-d126-41d6-002b-08d9f815df7c"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {jwtToken}"
}

payoutData = {
    "AccountID": "A120P0JR",
    "Currency": "EUR",
    "Amount": "0.01",
    "YourReference": "Updated payout",
    "DestinationIBAN": "GB94BARC10201530093459",
    "DestinationAccountName": "Destination Name",
    "TheirReference": "Their reference"
}

response = requests.request("PUT", f"{baseUrl}/{payoutId}", headers=headers, data=payoutData)

if response.ok:
    # API returns updated payout object response body.
    print(response.json())
else:
    # If not OK, response contains MoneyMoov problem ( see https://docs.nofrixion.com/reference/error-messages for details)
    print(response.json())
