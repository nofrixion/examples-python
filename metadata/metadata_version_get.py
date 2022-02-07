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