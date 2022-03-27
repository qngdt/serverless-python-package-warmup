import json

import hello

def handler(event, context):
    body = {
        "message": hello.hello(),
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
