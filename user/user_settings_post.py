#-----------------------------------------------------------------------------
# Description: Example of calling the NoFrixion MoneyMoov API user/settings POST 
# method. It provides a convenient way to update the current user settings.
#
# Usage:
# 1. Create a user access token in the sandbox portal at:
#    https:#portal-sandbox.nofrixion.com.
# 2. Set the token as an environment variable in your console:
#    set NOFRIXION_USER_TOKEN=<JWT token from previous step>
# 3. Run the script using the command: python -u "filename"
# 4. If successful HTTP status code 200 will be displayed.
#-----------------------------------------------------------------------------

# The 'requests' module for Python can be used to make calls to the MoneyMoov API in popular python frameworks such as Django and Flask.
import requests
import os

# Remember, the JWT access token must be securely stored ('os' module above allows storage in environment variable)
jwtToken = os.environ['NOFRIXION_USER_TOKEN']

baseUrl = "https://api-sandbox.nofrixion.com/api/v1/user/settings"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": f"Bearer {jwtToken}"
}

settingName = "CurrentMerchantID"
settingValue = "6f80138d-870b-4b07-8bc4-a4fd33a0d30f"
postData = f"userSettings[0].Name={settingName}&userSettings[0].Value={settingValue}"

response = requests.request("POST", baseUrl, headers=headers, data=postData)

if response.ok:
    # HTTP status code 200 on success
    print(response.status_code)
else:
    # If not OK, response contains MoneyMoov problem (https://docs.nofrixion.com/reference/error-messages)
    print(response.json())