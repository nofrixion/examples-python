#-----------------------------------------------------------------------------
# Description: Example of calling the NoFrixion MoneyMoov API 
# paymentrequests/{id}/card/void POST method. It voids a recently  
# processed card payment, authorisation or capture.
#
# Usage:
# 1. Create a user access token in the sandbox portal at:
#    https:#portal-sandbox.nofrixion.com.
# 2. Set the token as an environment variable in your console:
#    set NOFRIXION_USER_TOKEN=<JWT token from previous step>
# 3. Run the script using the command: python -u "filename"
# 4. If successful JSON object containing the card payment respone
#    model will be displayed.
#-----------------------------------------------------------------------------

# The 'requests' library for Python can be used to make calls to the MoneyMoov API in
# popular python frameworks such as Django and Flask.
import requests
import os

# Remember, the JWT access token must be securely stored ('os' module above allows storage in environment variable)
# ... and when dealing with payment requests, use a MERCHANT token!
jwtToken = os.environ['NOFRIXION_MERCHANT_TOKEN']

baseUrl = "https://api-sandbox.nofrixion.com/api/v1/paymentrequests"
paymentRequestID = "07b8f673-e3bb-4e1c-9d2b-08d9f6a98048"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {jwtToken}"
}

try:
    response = requests.request("POST", f"{baseUrl}/{paymentRequestID}/card/void", headers=headers)

    if response.ok:
        #  On successful void, the API returns the card payment response model with 'status': 'VOIDED'
        print(response.json())
    else:
        # If not OK, response contains MoneyMoov problem (https://docs.nofrixion.com/reference/error-messages)
        print(response.json())

except Exception as ex:
    print(ex)