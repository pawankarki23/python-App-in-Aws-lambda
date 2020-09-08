# to parse the url - s3 filename
#import urllib.parse

# os library
import os
# create unique IDs 
import uuid

# import Image module from Pillow
from PIL import Image 

# AWS SDK for python
import boto3

# initialize the S3 object
s3 = boto3.client('s3')
     

print('Loading image resize lambda function')


def resize_image(image_path, resized_path):
    with Image.open(image_path) as image:
        image.thumbnail((128, 128))
        image.save(resized_path)
     

def lambda_handler(event, context):
    # Let us print the event so that we can see how it looks 
    print(event)
    
    # Get the triggering bucket name from the event 
    bucket = event['Records'][0]['s3']['bucket']['name']
    print(bucket)

    #Get the file/key name from the event
    key = event['Records'][0]['s3']['object']['key']
    #key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    print('input filename that is to be processed is = ', key)
    
    # save the file in /tmp directory -- lambda provide /tmp directory for storage during the execution of function
    temp_save_path = '/tmp/{}{}'.format(uuid.uuid4(), key)
    print('temp_save_path ', temp_save_path)
    
    # create a resized filename 
    temp_resize_path = '/tmp/resized-{}'.format(key)
    print('resized filename ', temp_resize_path)
    
    # Now dowload the file from s3 to /tmp directory
    s3.download_file(bucket, key, temp_save_path)
    print('Dirs in /tmp ', os.listdir('/tmp/'))
    
    # resize the image -- create image thumbnail
    resize_image(temp_save_path, temp_resize_path)
    print('Dirs in /tmp ', os.listdir('/tmp/'))

    # upload resized image to destination bucket
    dest_bucket = '{}-resized'.format(bucket)
    s3.upload_file(temp_resize_path,dest_bucket , key)
    
    print('Done with uploading file to dest bucket ', dest_bucket)