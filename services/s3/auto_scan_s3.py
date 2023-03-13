import boto3
from dotenv import load_dotenv
# from pathlib import Path
import os
# import logging
import time

key = os.getenv("key")
secret = os.getenv("secret")
region = os.getenv("region")


s3_client = boto3.client('s3', aws_access_key_id=key, aws_secret_access_key=secret, region_name=region)

response = s3_client.list_objects_v2(
    Bucket='nimbleocrbills')

for content in response.get('Contents', []):
    print(content['Key'])
    time.sleep(100)