
variable "project_name" {
  type        = string
  default     = "idqs"
  description = "The name of the project used in resource naming."
}


variable "region" {
  type        = string
  default     = "us-east-1"
  description = "AWS region to deploy the resources in."
}


variable "db_username" {
  type        = string
  default     = "Amadmin"
  description = "Username for the Aurora database."
}



variable "db_password" {
  type        = string
  description = "Password for the Aurora database."
  sensitive   = true
}


variable "db_name" {
  type        = string
  default     = "idqsdb"
  description = "Database name for Aurora."
}
