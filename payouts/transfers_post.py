#-----------------------------------------------------------------------------
# Description: Example of calling the NoFrixion MoneyMoov API transfers POST 
# method. It provides a way to transfer funds between merchant accounts
#
# Usage:
# 1. Create a user access token in the sandbox portal at:
#    https:#portal-sandbox.nofrixion.com.
# 2. Set the token as an environment variable in your console:
#    set NOFRIXION_USER_TOKEN=<JWT token from previous step>
# 3. Run the script using the command: python -u "filename"
# 4. If successful user the transfer details will be displayed.
#-----------------------------------------------------------------------------

# The 'requests' library for Python can be used to make calls to the MoneyMoov API in
# popular python frameworks such as Django and Flask.
import requests
import os

# Remember, the JWT access token must be securely stored ('os' module above allows storage in environment variable)
jwtToken = os.environ['NOFRIXION_USER_TOKEN']

baseUrl = "https://api-sandbox.nofrixion.com/api/v1/payouts/transfer"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {jwtToken}"
}

transferData = {
    "Amount": "0.02",
    "Currency": "EUR",
    "SourceAccount": "A120R2Y3",
    "DestinationAccount": "A120P0JR",
    "Reference": "My reference",
    "ExternalReference": "Ext reference"
}

response = requests.request("POST", baseUrl, headers=headers, data=transferData)

if response.ok:
    # Response body confirms transfer details
    print(response.json())
else:
    # If not OK, response contains MoneyMoov problem (https://docs.nofrixion.com/reference/error-messages)
    print(response.json())
