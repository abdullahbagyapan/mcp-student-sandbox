import os

def get_aws_secret():
    key = os.getenv("AWS_SECRET_KEY")
    if not key:
        raise EnvironmentError("AWS_SECRET_KEY not set")
    return key

def connect():
    key = get_aws_secret()
    print("Connecting securely...")