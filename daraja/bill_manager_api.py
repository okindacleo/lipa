from django.http import HttpResponse, JsonResponse
import requests
from requests.auth import HTTPBasicAuth

from daraja.access_token import generate_access_token 
from daraja.utils import get_timestamp
from daraja.encode import generate_password
from daraja import keys
from daraja.generate_account import generate_random_string
from daraja.utils import generate_security_credential

def bill_manager_opt_in():

	#first API to opt you as a biller to our bill manager features
	api_url = "https://sandbox.safaricom.co.ke/v1/billmanager-invoice/optin" #API Endpoint

	formatted_time = get_timestamp()
	decoded_password = generate_password(formatted_time)
	my_access_token = generate_access_token()

		
	headers = { "Authorization": "Bearer %s" % my_access_token }


	request = {
	    "ShortCode":keys.shortcode,
	    "Logo": "fileurl",
	    "Email":keys.email,
	    "OfficialContact": keys.contact,
	    "SendReminders": "1",
	    "CallbackUrl": "https://dundisha.herokuapp.com/api/payments/bill_manager_optin/result/"
	  }



	try:
		response = requests.post(api_url, json=request, headers=headers)

	except:
		response = requests.post(api_url, json=request, headers=headers, verify=False)
	

	data = response.json()


	#print(data)
	#
	if data["rescode"] == "200":
		print('SUCCESS! BILL MANAGER OPT-IN')


bill_manager_opt_in()