# The 'requests' library for Python can be used to make calls to the MoneyMoov API in popular python frameworks such as Django and Flask.
import requests
import os

# Remember, the JWT access token must be securely stored ('os' module above allows storage in environment variable)
jwtToken = os.environ['NOFRIXION_SANDBOX_TOKEN']

# id of payout to delete must be specified
payoutId = "c59ea782-50c4-42bc-98bd-08d9ea12f96c"

url = f"https://api-sandbox.nofrixion.com/api/v1/payouts/{payoutId}"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {jwtToken}"
}

response = requests.request("DELETE", url, headers=headers)

# Process response / reason. Expect 200: OK on success
print(f"{response.status_code}: {response.reason}")

