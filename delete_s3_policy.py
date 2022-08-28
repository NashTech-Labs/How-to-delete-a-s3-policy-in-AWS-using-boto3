# By MuZakkir Saifi
# import the boto3 which will use to interact  with the aws

import boto3

REGION = input("Enter the REGION Name")
S3_BUCKET_NAME = input("Enter the bucket name")

client_for_s3 = boto3.client("s3", region_name=REGION)

client_for_s3.delete_bucket_policy(Bucket=S3_BUCKET_NAME)

print('Wow, Your bucket Policy has been deleted')