import os
import boto3
from botocore.exceptions import ClientError

def upload_files_to_s3(folder_path, bucket_name, prefix=""):
    
    s3_client = boto3.client('s3')

    
    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return

    
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            local_path = os.path.join(root, filename)
            
           
            relative_path = os.path.relpath(local_path, folder_path)
            s3_key = os.path.join(prefix, relative_path).replace("\\", "/")

            try:
                
                s3_client.upload_file(local_path, bucket_name, s3_key)
                print(f"Successfully uploaded {relative_path} to {bucket_name}/{s3_key}")
            except ClientError as e:
                print(f"Error uploading {relative_path}: {e}")

if __name__ == "__main__":
    
    folder_path = "project-root/spec-sheets"
    
    
    bucket_name = "bedrock-kb-704448598553"  
    
   
    prefix = "spec-sheets" 
    
    upload_files_to_s3(folder_path, bucket_name, prefix)
