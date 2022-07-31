# import the boto3 which will use to interact  with the aws

import boto3

AWS_REGION = input("Enter the AWS_REGION Name")
S3_BUCKET_NAME = input("Enter the bucket name")

s3_client = boto3.client("s3", region_name=AWS_REGION)

s3_client.delete_bucket_policy(Bucket=S3_BUCKET_NAME)

print('Wow, Your bucket Policy has been deleted')