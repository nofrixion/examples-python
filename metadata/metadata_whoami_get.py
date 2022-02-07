# The 'requests' library for Python can be used to make calls to the MoneyMoov API in
# popular python frameworks such as Django and Flask.

import requests, os

# Remember, the JWT access token must be securely stored ('os' module above allows storage in environment variable)
jwtToken = os.environ['NOFRIXION_SANDBOX_TOKEN']

url = "https://api-sandbox.nofrixion.com/api/v1/metadata/whoami"

headers = {
    "Accept": "text/plain",
    "Authorization": f"Bearer {jwtToken}"
}

response = requests.request("GET", url, headers=headers)

# Response is the user ID of the user issued the JWT access token.
print(response.text)