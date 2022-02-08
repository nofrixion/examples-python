# The 'requests' library for Python can be used to make calls to the MoneyMoov API in
# popular python frameworks such as Django and Flask.
import requests
import json
import os

# Remember, the JWT access token must be securely stored ('os' module above allows storage in environment variable)
jwtToken = os.environ['NOFRIXION_SANDBOX_TOKEN']

url = "https://api-sandbox.nofrixion.com/api/v1/accounts"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {jwtToken}"
}

response = requests.request("GET", url, headers=headers)

# JSON response is stored as Python dict
accountList = json.loads(response.text)

# exmaple: view keys/values for each account in the list
for account in accountList:
    for accountField in account.keys():
        print(f"{accountField}: {account[accountField]}")
    # Print a blank line between accounts for readability
    print()