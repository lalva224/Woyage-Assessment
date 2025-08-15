from dotenv import load_dotenv
import os 
import boto3
load_dotenv()

#using python-dotenv. It is better to load them all in a config file at once.
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")
AWS_ACCESS_KEY= os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY= os.getenv("AWS_SECRET_KEY")
AWS_REGION= os.getenv("AWS-REGION")
BUCKET_NAME = os.getenv("BUCKET_NAME")

s3_client = boto3.client("s3",aws_access_key_id=AWS_ACCESS_KEY,aws_secret_access_key=AWS_SECRET_KEY,region_name=AWS_REGION)

