#-----------------------------------------------------------------------------
# Description: Example of calling the NoFrixion MoneyMoov API Metadata/WhoAmI GET
# method. It provides a convenient way to check that a JWT access token is valid.
#
# Usage:
# 1. Create a user access token in the sandbox portal at:
#    https:#portal-sandbox.nofrixion.com.
# 2. Set the token as an environment variable in your console:
#    set NOFRIXION_USER_TOKEN=<JWT token from previous step>
# 3. Run the script using the command: python -u "filename"
# 4. If successful a JSON object containing user details will be displayed.
#-----------------------------------------------------------------------------

# The 'requests' library for Python can be used to make calls to the MoneyMoov API in
# popular python frameworks such as Django and Flask.

import requests
import os

# Remember, the JWT access token must be securely stored ('os' module above allows storage in environment variable)
jwtToken = os.environ['NOFRIXION_USER_TOKEN']

baseUrl = "https://api-sandbox.nofrixion.com/api/v1/metadata/whoami"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {jwtToken}"
}

response = requests.request("GET", baseUrl, headers=headers)

# Response object contains details of currently authenticated user.
print(response.json())