#-----------------------------------------------------------------------------
# Description: Example of calling the NoFrixion MoneyMoov API payouts POST 
# method. It provides a way to initate receipt of payment from third parties
#
# Usage:
# 1. Create a user access token in the sandbox portal at:
#    https:#portal-sandbox.nofrixion.com.
# 2. Set the token as an environment variable in your console:
#    set NOFRIXION_USER_TOKEN=<JWT token from previous step>
# 3. Run the script using the command: python -u "filename"
# 4. If successful the newly created payment request object will be displayed.
#-----------------------------------------------------------------------------

# The 'requests' library for Python can be used to make calls to the MoneyMoov API in
# popular python frameworks such as Django and Flask.
import requests
import os

# Remember, the JWT access token must be securely stored ('os' module above allows storage in environment variable)
# ... and when dealing with payment requests, use a MERCHANT token!
jwtToken = os.environ['NOFRIXION_MERCHANT_TOKEN']

baseUrl = "https://api-sandbox.nofrixion.com/api/v1/paymentrequests"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {jwtToken}"
}

paymentRequestData = {
    "MerchantID": "AB4476A1-8364-4D13-91CE-F4C4CA4EE6BE",
    "Amount": "0.99",
    "Currency": "EUR",
    "CustomerID": "C202202024158",
    "OrderID": "Sample order",
    #The methods below allow the purchaser to choose from those listed - BTC lightning payments coming soon!
    "PaymentMethodTypes": "card,pisp",
    "Description": "API Payment request",
    #URLs to integrate with merchant's site (required for card payments)
    "OriginUrl": "https://some.origin.url",
    "CallbackUrl": "https://some.callback.url",
    #PISP specific fields
    "PispAccountID": "A120P0JR",
    "PispRecipientReference": "Recipient ref",
    #Card specific fields
    "CardAuthorizeOnly": "true",
    "CardCreateToken": "false",
    "IgnoreAddressVerification": "true",
    "CardIgnoreCVN": "true"
    #Shipping and billing address data can also be included in the payment request
    #=> see https://api-sandbox.nofrixion.com/swagger/index.html for a complete reference.
}

try:
    response = requests.request("POST", baseUrl, headers=headers, data=paymentRequestData)

    if response.ok:
        # On successful creation, the API returns the payment request object
        print(response.json())
    else:
        # If not OK, response contains MoneyMoov problem (https://docs.nofrixion.com/reference/error-messages)
        print(response.json())

except Exception as ex:
    print(ex)