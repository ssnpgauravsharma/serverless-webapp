import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employees')


response = table.get_item(
    Key={
        'emp_id': '20'
    }
)
print(response["Item"])