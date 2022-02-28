#-----------------------------------------------------------------------------
# Description: Example of calling the NoFrixion MoneyMoov API Accounts Get
# method. It provides a convenient way to retrieve a list of your payment
# accounts.
#
# Usage:
# 1. Create a user access token in the sandbox portal at:
#    https:#portal-sandbox.nofrixion.com.
# 2. Set the token as an environment variable in your console:
#    set NOFRIXION_USER_TOKEN=<JWT token from previous step>
# 3. Run the script using the command: python -u "filename"
# 4. If successful a list of your accounts will be displayed.
#-----------------------------------------------------------------------------

# The 'requests' library for Python can be used to make calls to the MoneyMoov API in
# popular python frameworks such as Django and Flask.
import requests
import os

# Remember, the JWT access token must be securely stored ('os' module above allows storage in environment variable)
jwtToken = os.environ['NOFRIXION_USER_TOKEN']

baseUrl = "https://api-sandbox.nofrixion.com/api/v1/accounts"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {jwtToken}"
}

response = requests.request("GET", baseUrl, headers=headers)


if response.ok:
    # Convert JSON response to Python dict
    accountList = response.json()

    # example: view keys/values for each account in the list
    for account in accountList:
        for accountField in account.keys():
            print(f"{accountField}: {account[accountField]}")
        # Print a blank line between accounts for readability
        print()
else:
    # If not OK, response contains MoneyMoov problem (https://docs.nofrixion.com/reference/error-messages)
    print(response.json())
