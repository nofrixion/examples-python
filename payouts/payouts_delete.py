#-----------------------------------------------------------------------------
# Description: Example of calling the NoFrixion MoneyMoov API payouts DELETE 
# method. It provides a way to delete a previously created payout.
#
# Usage:
# 1. Create a user access token in the sandbox portal at:
#    https:#portal-sandbox.nofrixion.com.
# 2. Set the token as an environment variable in your console:
#    set NOFRIXION_USER_TOKEN=<JWT token from previous step>
# 3. Run the script using the command: python -u "filename"
# 4. If successful HTTP status code 200 will be displayed.
#-----------------------------------------------------------------------------

# The 'requests' library for Python can be used to make calls to the MoneyMoov API in popular python frameworks such as Django and Flask.
import requests
import os

# Remember, the JWT access token must be securely stored ('os' module above allows storage in environment variable)
jwtToken = os.environ['NOFRIXION_USER_TOKEN']

baseUrl = "https://api-sandbox.nofrixion.com/api/v1/payouts"

# id of payout to delete must be specified
payoutId = "b38163d9-6c86-468e-002c-08d9f815df7c"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {jwtToken}"
}

response = requests.request("DELETE", f"{baseUrl}/{payoutId}", headers=headers)

if response.ok:
    # Process response / reason. Expect "200: OK" on success
    print(f"{response.status_code}: {response.reason}")
else:
    # If not OK, response contains MoneyMoov problem (https://docs.nofrixion.com/reference/error-messages)
    print(response.json())

