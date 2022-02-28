#-----------------------------------------------------------------------------
# Description: Example of calling the NoFrixion MoneyMoov API Metadata/Verion
# GET method. It provides a convenient way to check the current version of the API.
#
# Usage:
# 1. Run the script using the command: python -u "filename"
# 2. If successful a string with the current version of the version will be
# displayed.
#-----------------------------------------------------------------------------

# The 'requests' library for Python can be used to make calls to the MoneyMoov API in
# popular python frameworks such as Django and Flask.

import requests

baseUrl = "https://api-sandbox.nofrixion.com/api/v1/metadata/version"

headers = {
    "Accept": "application/json"
}

response = requests.request("GET", baseUrl, headers=headers)

# The response json contains the API Version details
print(response.json())