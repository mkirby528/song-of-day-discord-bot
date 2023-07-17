import boto3
import os
from boto3.dynamodb.conditions import Key

dynamodb_resource = boto3.resource("dynamodb")
TABLE_NAME = os.environ["DYANMO_TABLE_NAME"]
table = dynamodb_resource.Table(TABLE_NAME)


def insert_item(item):
    return table.put_item(Item=item)


def item_in_table(item):
    response = table.query(KeyConditionExpression=Key('id').eq(item['id']))
    return len(response["Items"]) != 0
