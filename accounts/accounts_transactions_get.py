#-----------------------------------------------------------------------------
# Description: Example of calling the NoFrixion MoneyMoov API Accounts/{accounId}/transactions 
# GET method. It provides a convenient way to retrieve a list of transactions for the specified
# account.
#
# Usage:
# 1. Create a user access token in the sandbox portal at:
#    https:#portal-sandbox.nofrixion.com.
# 2. Set the token as an environment variable in your console:
#    set NOFRIXION_SANDBOX_TOKEN=<JWT token from previous step>
# 3. Run the script using the command: python -u "filename"
# 4. If successful a list of transactions will be displayed.
#-----------------------------------------------------------------------------

# The 'requests' library for Python can be used to make calls to the MoneyMoov API in
# popular python frameworks such as Django and Flask.
import requests
import json
import os

# Remember, the JWT access token must be securely stored ('os' module above allows storage in environment variable)
jwtToken = os.environ['NOFRIXION_SANDBOX_TOKEN']

# need to specify the account to get transactions for
accountId = "A120P0JR"

# by default each call will return 20 transactions, we can change this using a query parameter as shown below.
queryParams = "?size=10"

url = f"https://api-sandbox.nofrixion.com/api/v1/accounts/{accountId}/transactions{queryParams}"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {jwtToken}"
}

response = requests.request("GET", url, headers=headers)

# The response is a JSON object containing
# - transactions: a property that is an array of JSON objects
# - metdata fields: 'page', 'pageStartBalance', 'size', 'totalPages', 'totalSize'
#   - these can be used to help with pagination of results (and can be passed in the query string)

data = response.json()

# example: view keys/values for each transaction in the list
# you will notice that the "merchantAccount" property contains further nested objects

for transaction in data['transactions']:
    for transactionField in transaction.keys():
        print(f"{transactionField}: {transaction[transactionField]}")
    # Print a blank line between transactions for readability
    print()

# use metadata to summarise displayed transactions
print(f"Showing page {data['page'] + 1} of {data['totalPages'] + 1}. {data['totalSize']} transactions in total.")
