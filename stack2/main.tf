provider "aws" {
  region = "us-east-1"  
}

module "bedrock_kb" {
  source = "../modules/bedrock_kb" 

  knowledge_base_name        = "my-bedrock-kb"
  knowledge_base_description = "Knowledge base connected to Aurora Serverless database"

  aurora_arn        = "arn:aws:rds:us-east-1:704448598553:cluster:my-aurora-serverless" 
  aurora_db_name    = "ISQSDATA"
  aurora_endpoint   = "my-aurora-serverless.cluster-c89k4w88skvu.us-east-1.rds.amazonaws.com" 
  aurora_table_name = "bedrock_integration.bedrock_kb"
  aurora_primary_key_field = "id"
  aurora_metadata_field = "metadata"
  aurora_text_field = "chunks"
  aurora_verctor_field = "embedding"
  aurora_username   = "AMadmin"
  aurora_secret_arn = "arn:aws:secretsmanager:us-east-1:704448598553:secret:my-aurora-serverless-sgKrJh"
  s3_bucket_arn = "arn:aws:s3:::bedrock-kb-704448598553" 

}

