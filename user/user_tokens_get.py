#-----------------------------------------------------------------------------
# Description: Example of calling the NoFrixion MoneyMoov API user/tokens 
# GET method. It provides a convenient way to retrieve information about  
# access tokens issued to the authenticated user.
#
# Usage:
# 1. Create a user access token in the sandbox portal at:
#    https:#portal-sandbox.nofrixion.com.
# 2. Set the token as an environment variable in your console:
#    set NOFRIXION_USER_TOKEN=<JWT token from previous step>
# 3. Run the script using the command: python -u "filename"
# 4. If successful the user's API access tokens will be displayed.
#-----------------------------------------------------------------------------

# The 'requests' module for Python can be used to make calls to the MoneyMoov API in popular python frameworks such as Django and Flask.
import requests
import os

# Remember, the JWT access token must be securely stored ('os' module above allows storage in environment variable)
jwtToken = os.environ['NOFRIXION_USER_TOKEN']

baseUrl = "https://api-sandbox.nofrixion.com/api/v1/user/tokens"

# Note optional url paramaters for paging the token list are exposed in the API
# - see https://api-sandbox.nofrixion.com/swagger/index.html for full details

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {jwtToken}"
}

try:
    response = requests.request("GET", baseUrl, headers=headers)

    if response.ok:
        # Returns JSON object containing page metadata and tokens.
        tokensPage = response.json()
        #  User tokens are stored in 'content' property, do something with these...
        print(tokensPage["content"])
    else:
        # If not OK, response contains MoneyMoov problem (https://docs.nofrixion.com/reference/error-messages)
        print(response.json())
        
except Exception as ex:
    print(ex)