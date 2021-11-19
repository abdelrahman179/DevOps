terraform {
  backend "s3" {
    bucket         = "terraform-sprints"
    key            = "terraform.tfstate"
    region         = "us-east-2"
    dynamodb_table = "terraform_sprints"
  }
}