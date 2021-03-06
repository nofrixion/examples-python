#-----------------------------------------------------------------------------
# Description: Example of calling the NoFrixion MoneyMoov API 
# paymentrequests/{id}/card/capture POST method. It captures payment for a   
# previously authorised card payment.
#
# Usage:
# 1. Create a user access token in the sandbox portal at:
#    https:#portal-sandbox.nofrixion.com.
# 2. Set the token as an environment variable in your console:
#    set NOFRIXION_USER_TOKEN=<JWT token from previous step>
# 3. Run the script using the command: python -u "filename"
# 4. If successful JSON object containing the card payment respone
#    model will be displayed
#-----------------------------------------------------------------------------

# The 'requests' library for Python can be used to make calls to the MoneyMoov API in
# popular python frameworks such as Django and Flask.
import requests
import os

# Remember, the JWT access token must be securely stored ('os' module above allows storage in environment variable)
# ... and when dealing with payment requests, use a MERCHANT token!
jwtToken = os.environ['NOFRIXION_MERCHANT_TOKEN']

baseUrl = "https://api-sandbox.nofrixion.com/api/v1/paymentrequests"

paymentRequestID = "187ec02c-860f-4414-ccb5-08da00f4d66d"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {jwtToken}"
}

postData = {
    "AuthorizationID": "6467848603196559404005",
    "Amount": "0.10"
}

try:
    response = requests.request("POST", f"{baseUrl}/{paymentRequestID}/card/capture", headers=headers, data=postData)

    if response.ok:
        #   On success, the API returns the card payment response model 
        print(response.json())
    else:
        # If not OK, response contains MoneyMoov problem (https://docs.nofrixion.com/reference/error-messages)
        print(response.json())

except Exception as ex:
    print(ex)