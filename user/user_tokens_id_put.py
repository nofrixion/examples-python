#-----------------------------------------------------------------------------
# Description: Example of calling the NoFrixion MoneyMoov API user/tokens POST 
# method. It provides a way to update a user access token's description
#
# Usage:
# 1. Create a user access token in the sandbox portal at:
#    https:#portal-sandbox.nofrixion.com.
# 2. Set the token as an environment variable in your console:
#    set NOFRIXION_USER_TOKEN=<JWT token from previous step>
# 3. Run the script using the command: python -u "filename"
# 4. If successful the updated user access token will be displayed.
#-----------------------------------------------------------------------------

# The 'requests' library for Python can be used to make calls to the MoneyMoov API in
# popular python frameworks such as Django and Flask.
import requests
import os

# Remember, the JWT access token must be securely stored ('os' module above allows storage in environment variable)
jwtToken = os.environ['NOFRIXION_USER_TOKEN']

baseUrl = "https://api-sandbox.nofrixion.com/api/v1/user/tokens"

tokenID = "042a5ab9-3f36-4d6e-a7c8-fcdc901c7e2d"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {jwtToken}"
}

tokenData = {
    "Description": "Updated description"
}

try:
    response = requests.request("PUT", f"{baseUrl}/{tokenID}", headers=headers, data=tokenData)
    if response.ok:
        print(response.json())
    else:
        # If not OK, response contains MoneyMoov problem (https://docs.nofrixion.com/reference/error-messages)
        print(response.json())
        
except Exception as ex:
    print(ex)

