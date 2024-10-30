import boto3
import config
import sys
if sys.version_info[0]<3:
    from StringIO import StringIO #for python 2.x
else:
    from io import StringIO # for python 3.x

class S3handler:
    def __init__(self) -> None:
        self.region='us-east-1'
        self.s3_client = boto3.client('s3')

    def s3_prepare_file(self,process_name:str,file_name:str):
        """
        preparing file format with filename
        """
        path =f"api-sts/{process_name}/{file_name}"
        return path
    
    def get_s3_file(self):
        bucket = config.default_config['s3_bucket']
        key = self.s3_prepare_file('sample','example.csv')
        try:
            response = self.s3_client.get_object(Bucket=bucket,Key=key)
            body = response['Body']
            csv_str = body.read().decode('utf-8')
            return StringIO(csv_str)
        except Exception as e:
            return str(e)
        

        
        

