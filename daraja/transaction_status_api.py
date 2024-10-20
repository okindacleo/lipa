from django.http import HttpResponse, JsonResponse
import requests
from requests.auth import HTTPBasicAuth

from daraja.access_token import generate_access_token 
from daraja.utils import get_timestamp, generate_security_credential
from daraja.encode import generate_password
from daraja import keys
from daraja.generate_account import generate_random_string
from daraja.utils import generate_security_credential


def trans_status(transaction_id, initiator):

	api_url = 'https://sandbox.safaricom.co.ke/mpesa/transactionstatus/v1/query'#API Endpoint

	formatted_time = get_timestamp()
	decoded_password = generate_password(formatted_time)
	my_access_token = generate_access_token()
	
	headers = { "Authorization": "Bearer %s" % my_access_token }

	request = {
		    
	   "Initiator":initiator,
	   "SecurityCredential": generate_security_credential('Okinda@123'),
	   "CommandID": "TransactionStatusQuery",
	   "TransactionID": transaction_id,
	   #"OriginatorConversationID":"1236-7134259-1",
	   "OriginatorConversationID":"AG_20190826_0000777ab7d848b9e721",
	   "PartyA":keys.business_shortCode,
	   "IdentifierType":"4",
	   "ResultURL":"https://inject-50d08d8f31b6.herokuapp.com/api/payments/trans_status/result/",
	   "QueueTimeOutURL":"https://inject-50d08d8f31b6.herokuapp.com/api/payments/trans_status/timeout/",
	   "Remarks":"Transaction Status Check",
	   "Occasion":"Checking Status",

	}


	try:
		response = requests.post(api_url, json=request, headers=headers)

	except:
		response = requests.post(api_url, json=request, headers=headers, verify=False)
	

	data = response.json()


	#print(request["SecurityCredential"])
	print(data)
	#
	if data["ResponseCode"] == "0":
		print('SUCCESS! TRANSACTION STATUS')