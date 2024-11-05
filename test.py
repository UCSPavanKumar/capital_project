from EDQClientRest import EDQClientRest
import boto3
import pandas as pd
from s3_handler import S3handler
if __name__ == '__main__':
    s3handler = S3handler()
    data = s3handler.get_s3_file()
    df = pd.read_csv(data)
    print(df.head(10))
    
   