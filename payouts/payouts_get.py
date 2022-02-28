#-----------------------------------------------------------------------------
# Description: Example of calling the NoFrixion MoneyMoov API payouts GET 
# method. It provides a convenient way to obtain a list of pending payouts.
#
# Usage:
# 1. Create a user access token in the sandbox portal at:
#    https:#portal-sandbox.nofrixion.com.
# 2. Set the token as an environment variable in your console:
#    set NOFRIXION_USER_TOKEN=<JWT token from previous step>
# 3. Run the script using the command: python -u "filename"
# 4. If successful user a list of payouts will be displayed.
#-----------------------------------------------------------------------------

# The 'requests' module for Python can be used to make calls to the MoneyMoov API in popular python frameworks such as Django and Flask.
import requests
import os

# Remember, the JWT access token must be securely stored ('os' module above allows storage in environment variable)
jwtToken = os.environ['NOFRIXION_USER_TOKEN']

baseUrl = "https://api-sandbox.nofrixion.com/api/v1/payouts"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {jwtToken}"
}

response = requests.request("GET", baseUrl, headers=headers)

if response.ok:
    # The response data is a JSON object containing:
    # - content: a property that is an array of payout objects
    # - metdata fields: 'pageNumber', 'pageSize', 'totalPages', 'totalSize'
    #   - these can be used to help with pagination of results (and can be passed in the query string)
    data = response.json()

    # For exmaple: view keys/values for each payout in the content property
    for payout in data["content"]:
        for payoutField in payout.keys():
            print(f"{payoutField}: {payout[payoutField]}")
        # Print a blank line between payouts for readability
        print()

    # Display metadata
    print(f"Retrieved page {data['pageNumber']} of {data['totalPages']} payout pages.")
else:
    # If not OK, response contains MoneyMoov problem (https://docs.nofrixion.com/reference/error-messages)
    print(response.json())