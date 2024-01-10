# Configure the Terraform Cloud as a backend for remote state
data "terraform_remote_state" "lambda_layers" {
  backend = "remote"

  config = {
    organization = "spike-spiegel"
    workspaces = {
      name = "lambda-layers-playground-dev"
    }
  }
}

# Create S3 Bucket - Testing
resource "aws_s3_bucket" "lambda_layer_storage" {
  bucket_prefix = "learn-project-infra-s3-test"
  force_destroy = true
}

resource "aws_s3_bucket_server_side_encryption_configuration" "lambda_layer_storage" {
  bucket = aws_s3_bucket.lambda_layer_storage.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}