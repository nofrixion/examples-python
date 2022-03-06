#-----------------------------------------------------------------------------
# Description: Example of calling the NoFrixion MoneyMoov API 
# paymentrequests/{id}/pisp POST method. It submits a payment initiation  
# request.
#
# Usage:
# 1. Create a user access token in the sandbox portal at:
#    https:#portal-sandbox.nofrixion.com.
# 2. Set the token as an environment variable in your console:
#    set NOFRIXION_USER_TOKEN=<JWT token from previous step>
# 3. Run the script using the command: python -u "filename"
# 4. If successful a JSON object containing the payment initiation ID and redirect
#    URL will be displayed.
#-----------------------------------------------------------------------------

# The 'requests' library for Python can be used to make calls to the MoneyMoov API in
# popular python frameworks such as Django and Flask.
import requests
import os

# Remember, the JWT access token must be securely stored ('os' module above allows storage in environment variable)
# ... and when dealing with payment requests, use a MERCHANT token!
jwtToken = os.environ['NOFRIXION_MERCHANT_TOKEN']

baseUrl = "https://api-sandbox.nofrixion.com/api/v1/paymentrequests"
paymentRequestID = "e747d05e-3d60-4edb-9886-08d9f65a6611"

# PISP provider id, use the paymentrequests/{id}/pisp/providers GET action to see a list
providerID = "H120000001"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {jwtToken}"
}

paymentData = {
    "providerID": providerID
}

try:
    response = requests.request("POST", f"{baseUrl}/{paymentRequestID}/pisp", headers=headers, data=paymentData)

    if response.ok:
        #  On successful update, the API returns the payment initiation response containing
        #  payment initiation ID and the URL to redirect the payer to their financial institution.
        print(response.json())
    else:
        # If not OK, response contains MoneyMoov problem (https://docs.nofrixion.com/reference/error-messages)
        print(response.json())

except Exception as ex:
    print(ex)