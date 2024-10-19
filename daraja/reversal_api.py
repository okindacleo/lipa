from django.http import HttpResponse, JsonResponse
import requests
from requests.auth import HTTPBasicAuth

from daraja.access_token import generate_access_token 
from daraja.utils import get_timestamp, generate_security_credential
from daraja.encode import generate_password
from daraja import keys
from daraja.generate_account import generate_random_string
from daraja.utils import generate_security_credential


def reverse_c2b_or_b2c(initiator, transaction_id, amount, receiver_party):

	api_url = 'https://sandbox.safaricom.co.ke/mpesa/reversal/v1/request'#API Endpoint
	
	formatted_time = get_timestamp()
	decoded_password = generate_password(formatted_time)
	my_access_token = generate_access_token()
	
	headers = { "Authorization": "Bearer %s" % my_access_token }

	request = {
		    
	   "Initiator":initiator,
	   "SecurityCredential": [generate_security_credential('Okinda@123')],
	   "CommandID": "TransactionReversal",
	   "TransactionID": [transaction_id],
	   "Amount": [amount],
	   "ReceiverParty": receiver_party, # Reversing to aPaybill number
	   "RecieverIdentifierType": "4",
	   "ResultURL":"https://dundisha.herokuapp.com/api/payments/reversal/result/",
	   "QueueTimeOutURL":"https://dundisha.herokuapp.com/api/payments/reversal/timeout/",
	   "Remarks":"Reversal request for wrong transaction",
	   "Occasion":"Reversal",

	}


	try:
		response = requests.post(api_url, json=request, headers=headers)

	except:
		response = requests.post(api_url, json=request, headers=headers, verify=False)
	

	data = response.json()


	print(request["SecurityCredential"])
	print(data)
	#
	if data["ResponseCode"] == "0":
		print('SUCCESS! REVERSE TRANSACTION')