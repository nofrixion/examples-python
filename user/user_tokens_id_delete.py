# -----------------------------------------------------------------------------
# Description: Example of calling the NoFrixion MoneyMoov API user/tokens/{id}
# GET method. It provides a convenient way to delete a specified user
# access token.
#
# Usage:
# 1. Create a user access token in the sandbox portal at:
#    https:#portal-sandbox.nofrixion.com.
# 2. Set the token as an environment variable in your console:
#    set NOFRIXION_USER_TOKEN=<JWT token from previous step>
# 3. Run the script using the command: python -u "filename"
# 4. If successful the HTTP status code "200" will be displayed.
# -----------------------------------------------------------------------------

# The 'requests' module for Python can be used to make calls to the MoneyMoov API in popular python frameworks such as Django and Flask.
import requests
import os

# Remember, the JWT access token must be securely stored ('os' module above allows storage in environment variable)
jwtToken = os.environ['NOFRIXION_USER_TOKEN']

baseUrl = "https://api-sandbox.nofrixion.com/api/v1/user/tokens"
tokenID = "2435ceda-7fbe-41d7-8b6d-dd82f3703d12"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {jwtToken}"
}

try:
    response = requests.request("DELETE", f"{baseUrl}/{tokenID}", headers=headers)

    if response.ok:
        # Returns HTTP status 200 on successful delete.
        print(response.status_code)
    else:
        # If not OK, response contains MoneyMoov problem (https://docs.nofrixion.com/reference/error-messages)
        print(response.json())

except Exception as ex:
    print(ex)