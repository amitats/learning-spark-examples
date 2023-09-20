import json
import boto3
def lambda_handler(event, context):
    client = boto3.client('ec2')
    clientsns = boto3.client('sns')
    addresses_dict = client.describe_addresses()
    for eip_dict in addresses_dict['Addresses']:
        if "NetworkInterfaceId" not in eip_dict:
	        print(eip_dict['PublicIp'])
	        message =  'you have unattached elastic IP'
	        topic_arn = 'arn:aws:sns:ap-south-1:615760805870:mynewtopic'
        	clientsns.publish(TopicArn=topic_arn,Message=message)
             # TODO implement
