import os
import boto3
import csv
from io import StringIO

# Retrieve AWS credentials from environment variables
aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']

# Create an S3 client with credentials
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

# The S3 bucket name
bucket_name = 'learn-project-infra-s3-test20240103185015553500000002'

# The name you want the CSV file to have in S3
s3_file_name = 'test.csv'

# Sample data for the CSV file
csv_data = [
    ['Name', 'Age', 'City'],
    ['Alice', '24', 'New York'],
    ['Bob', '27', 'San Francisco']
]

# Create a CSV file in memory
csv_buffer = StringIO()
csv_writer = csv.writer(csv_buffer)
csv_writer.writerows(csv_data)

# Upload the CSV file to S3
s3.put_object(Bucket=bucket_name, Key=s3_file_name, Body=csv_buffer.getvalue())

print(f'File {s3_file_name} uploaded to {bucket_name}')