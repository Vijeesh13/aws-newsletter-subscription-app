import json
import boto3
import os
import re

sns = boto3.client("sns")
TOPIC_ARN = os.environ["TOPIC_ARN"]

EMAIL_REGEX = r"[^@]+@[^@]+\.[^@]+"

def build_response(status, body):
    return {
        "statusCode": status,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "OPTIONS,POST",
            "Access-Control-Allow-Headers": "Content-Type"
        },
        "body": json.dumps(body)
    }

def lambda_handler(event, context):
    if event.get("httpMethod") == "OPTIONS":
        return build_response(200, {"message": "CORS OK"})

    body = json.loads(event.get("body", "{}"))
    email = body.get("email", "").strip()

    if not re.match(EMAIL_REGEX, email):
        return build_response(400, {"error": "Invalid email"})

    sns.subscribe(
        TopicArn=TOPIC_ARN,
        Protocol="email",
        Endpoint=email
    )

    return build_response(200, {"message": "Check your email to confirm subscription!"})
