terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  # Terraform Cloud configuration for GitHub Actions
  #  cloud {
  #    organization = "escobarana"
  #
  #    workspaces {
  #      name = "gh-actions-datapipelines"
  #    }
  #  }
}

# Configure the AWS Provider
provider "aws" {
  region = var.region
}
