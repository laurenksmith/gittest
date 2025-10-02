terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }
  }
}

provider "github" {
  token = var.github_token
  owner = "laurenksmith"
}

resource "github_repository" "my_first_tf_gh_repo" {
    name = var.repo_name
    description = var.repo_description
    visibility = "public"
}


