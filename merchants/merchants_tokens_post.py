#-----------------------------------------------------------------------------
# Description: Example of calling the NoFrixion MoneyMoov API merchant/tokens POST 
# method. It provides a convenient way to create a merchant token.
#
# Usage:
# 1. Create a user access token in the sandbox portal at:
#    https:#portal-sandbox.nofrixion.com.
# 2. Set the token as an environment variable in your console:
#    set NOFRIXION_USER_TOKEN=<JWT token from previous step>
# 3. Run the script using the command: python -u "filename"
# 4. If successful the Merchant token is returned in the response body 
#    (save this in a safe place, it isn't stored in the NoFrixion systems).
#-----------------------------------------------------------------------------

# The 'requests' library for Python can be used to make calls to the MoneyMoov API in
# popular python frameworks such as Django and Flask.
import requests
import os

# Remember, the JWT access token must be securely stored ('os' module above allows storage in environment variable)
jwtToken = os.environ['NOFRIXION_USER_TOKEN']

baseUrl = "https://api-sandbox.nofrixion.com/api/v1/merchants/tokens"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {jwtToken}"
}

tokenData = {
    "MerchantID":"6f80138d-870b-4b07-8bc4-a4fd33a0d30f",
    "Description":"API created token"
}

response = requests.request("POST", baseUrl, headers=headers, data = tokenData)

if response.ok:
    # Returned JSON data contains the new merchant token => MAKE SURE YOU SAVE THIS! (we don't store it).
    print(response.json())
else:
    # If not OK, response contains MoneyMoov problem (https:#docs.nofrixion.com/reference/error-messages)
    print(response.json())
