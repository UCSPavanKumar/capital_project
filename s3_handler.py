import boto3
class S3handler:
    def __init__(self) -> None:
        self.region='us-east-1'

    def s3_read_file(self,process_name):
        s3 = boto3.resource('s3')
        

