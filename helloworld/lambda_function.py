# importing libraries that we will be using in our lambda code
import json

# entry point of lambda function or main function 
def lambda_handler(event, context):
    # TODO implement
    
    # create a message from event data
    message = event['key1'] + event['key2'] + event['key3']
    
    #print the message
    print(message)
    
    # let us return this message
    return message