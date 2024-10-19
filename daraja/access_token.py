import requests
from requests.auth import HTTPBasicAuth
from daraja import keys

#import keys

#request = ''

def generate_access_token():

	consumer_key = keys.consumer_key
	consumer_secret = keys.consumer_secret

	api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
	#api_URL = "https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
	#api_URL = "https://api.safaricom.co.ke/oauth/v1/generate"#production

	#r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

	try:
		r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
		
	except:
		r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret), verify=False)
		print('json error')

	json_response = r.json()
	my_access_token = json_response['access_token']
	print
	#print(json_response)
	#print(dict(json_response))

	return my_access_token

#generate_access_token()