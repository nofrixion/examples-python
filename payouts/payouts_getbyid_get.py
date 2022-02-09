#-----------------------------------------------------------------------------
# Description: Example of calling the NoFrixion MoneyMoov API payouts/getbyid/{id} GET 
# method. It provides a convenient way to obtain a pending payout information, including
# the URL used for payout approval.
#
# Usage:
# 1. Create a user access token in the sandbox portal at:
#    https:#portal-sandbox.nofrixion.com.
# 2. Set the token as an environment variable in your console:
#    set NOFRIXION_SANDBOX_TOKEN=<JWT token from previous step>
# 3. Run the script using the command: python -u "filename"
# 4. If successful user the payout details will be displayed.
#-----------------------------------------------------------------------------

# The 'requests' module for Python can be used to make calls to the MoneyMoov API in popular python frameworks such as Django and Flask.
import requests
import os

# Remember, the JWT access token must be securely stored ('os' module above allows storage in environment variable)
jwtToken = os.environ['NOFRIXION_SANDBOX_TOKEN']

# id of required payout must be specified
payoutId = "7d245bfe-5e3a-4945-2a23-08d9e9d0d973"

url = f"https://api-sandbox.nofrixion.com/api/v1/payouts/getbyid/{payoutId}"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {jwtToken}"
}

response = requests.request("GET", url, headers=headers)

# Python will convert the JSON response to a dict
payout = response.json()

# Can just print it, but easier to read by iterating over dict keys.
for payoutField in payout.keys():
    print(f"{payoutField}: {payout[payoutField]}")
