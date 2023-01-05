import json


def hello(event, context):
    body = {
        "message": "This is an example for serverless framework",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
