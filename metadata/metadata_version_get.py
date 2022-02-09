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

url = "https://api-sandbox.nofrixion.com/api/v1/metadata/version"

headers = {
    "Accept": "text/plain"
}

response = requests.request("GET", url, headers=headers)

# The response text contains the API Version
print(response.text)

# Can also check HTTP status code/message
print(response.status_code)
print(response.reason)