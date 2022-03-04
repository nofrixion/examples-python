#-----------------------------------------------------------------------------
# Description: Example of calling the NoFrixion MoneyMoov API user/tokens POST 
# method. It provides a convenient way to refresh a user access token
#
# Usage:
# 1. Create a user access token in the sandbox portal at:
#    https:#portal-sandbox.nofrixion.com.
# 2. Set the token as an environment variable in your console:
#    set NOFRIXION_USER_TOKEN=<JWT token from previous step>
# 3. Run the script using the command: python -u "filename"
# 4. If successful the new user access and refresh tokens will be displayed.
#-----------------------------------------------------------------------------

# The 'requests' library for Python can be used to make calls to the MoneyMoov API in
# popular python frameworks such as Django and Flask.
import requests
import os

# Remember, the JWT access token must be securely stored ('os' module above allows storage in environment variable)
jwtToken = os.environ['NOFRIXION_USER_TOKEN']

baseUrl = "https://api-sandbox.nofrixion.com/api/v1/user/tokens/refresh"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {jwtToken}"
}

refreshToken = {
    "refreshToken": "v1.MdyA7UHuFilihLPYqBsyYbSBTAUAhH-nkpngxFBdnSbNz4YQ-E5VYK6ie6R87Edp73_0uHzkhOYK0Q3TvQG18UM"
}

try:
    response = requests.request("POST", baseUrl, headers=headers, data=refreshToken)

    if response.ok:
        # The json response contains the new user token (accessToken) and a new refresh token (refreshToken)
        # Save these, the are not stored in the database.
        newTokens = response.json()
        print(newTokens["accessToken"])
        print(newTokens["refreshToken"])
    else:
        # If not OK, response contains MoneyMoov problem (https://docs.nofrixion.com/reference/error-messages)
        print(response.json())

except Exception as ex:
    print(ex)
