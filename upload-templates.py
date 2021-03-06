import boto3, os, logging
from botocore.exceptions import ClientError

filecount = 0


def get_file_names():
    global filecount
    s3_bucket = "<ADD YOUR GLOBAL BUCKET NAME HERE>"
    files = os.listdir()
    files.remove(os.path.basename(__file__))

    for file in files:
        upload_to_aws(file, s3_bucket, file)
        filecount += 1


def upload_to_aws(file, s3_bucket, s3_file_name):
    # Upload the folder
    s3_client = boto3.client("s3")

    try:
        response = s3_client.upload_file(file, s3_bucket, s3_file_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


get_file_names()
print(str(filecount) + " files uploaded successfully")
