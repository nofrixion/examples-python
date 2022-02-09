#-----------------------------------------------------------------------------
# Description: Example of calling the NoFrixion MoneyMoov API payouts PUT 
# method. It provides a convenient way to modify a previously created payout
#
# Usage:
# 1. Create a user access token in the sandbox portal at:
#    https:#portal-sandbox.nofrixion.com.
# 2. Set the token as an environment variable in your console:
#    set NOFRIXION_SANDBOX_TOKEN=<JWT token from previous step>
# 3. Run the script using the command: python -u "filename"
# 4. If successful user the updated payout ID will be displayed.
#-----------------------------------------------------------------------------

# The 'requests' library for Python can be used to make calls to the MoneyMoov API in popular python frameworks such as Django and Flask.
import requests
import os

# Remember, the JWT access token must be securely stored ('os' module above allows storage in environment variable)
jwtToken = os.environ['NOFRIXION_SANDBOX_TOKEN']

# id of payout to update must be specified
payoutId = "7d245bfe-5e3a-4945-2a23-08d9e9d0d973"

url = f"https://api-sandbox.nofrixion.com/api/v1/payouts/{payoutId}"

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

response = requests.request("PUT", url, headers=headers, data=payoutData)

# Process response / reason. Expect 200 / OK on success
print(f"{response.status_code} : {response.reason}")

# Alternatively API returns updated payout ID in response body.
print(response.text)