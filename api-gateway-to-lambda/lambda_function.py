import json


def lambda_handler(event, context):
	
	# let us print out the event
	print(event)
	
	# Parse out query string params
	firstname = event['queryStringParameters']['firstname']
	lastname = event['queryStringParameters']['lastname']

	print('firstname=  ',  firstname)
	print('lastname='  , lastname)

	#Construct the body of the response object
	Response = {}
	Response['firstname'] = firstname
	Response['lastname'] = lastname
	Response['message'] = firstname + lastname + ' invoked Lambda function'

	#Construct http response object
	responseObject = {}
	responseObject['statusCode'] = 200
	responseObject['headers'] = {}
	responseObject['headers']['Content-Type'] = 'application/json'
	responseObject['body'] = json.dumps(Response)

	#Return the response object back to the 
	return responseObject