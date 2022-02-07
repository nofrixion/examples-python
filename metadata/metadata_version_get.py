# The 'requests' library for Python can be used to make calls to the MoneyMoov API in
# popular python frameworks such as Django and Flask.

import requests

apiServer = "https://api-sandbox.nofrixion.com/api/v1/"
apiEndpoint = "metadata/version"

headers = {
    "Accept": "text/plain"
}

response = requests.request("GET", apiServer + apiEndpoint, headers=headers)

# The response text contains the API Version
print(response.text)

# Can also check HTTP status code/message
print(response.status_code)
print(response.reason)