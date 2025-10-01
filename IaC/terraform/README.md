# Terraform Learning

- [Terraform Learning](#terraform-learning)
  - [Intro to Terraform](#intro-to-terraform)
  - [What Is Terraform? What Is It Used For?](#what-is-terraform-what-is-it-used-for)
  - [Why Use Terraform? The Benefits?](#why-use-terraform-the-benefits)
  - [In IaC, What Is Orchestration? How Does Terraform Act As "Orchestrator"?](#in-iac-what-is-orchestration-how-does-terraform-act-as-orchestrator)
  - [Best Practice Supplying AWS Credentials to Terraform](#best-practice-supplying-aws-credentials-to-terraform)
  - [How Should AWS Credentials Never Be Passed To Terraform?](#how-should-aws-credentials-never-be-passed-to-terraform)
  - [Why Use Terraform For Different Environments (e.g. production, testing, etc)](#why-use-terraform-for-different-environments-eg-production-testing-etc)
  - [Useful Websites:](#useful-websites)

## Intro to Terraform

## What Is Terraform? What Is It Used For?

* Orchestration tool
* Best for infrastructure provisionsing
* Originally inspired by AWS CloudFormation
* Sees infrastructure as immutable (i.e. disposable)
  * Compare this to configure management tools, which usually see infrastructure as mutable/reusable
* Code in Hashicorp Configuration Language (HCL)
  * aims to give a balance between human and machine-readability
  * HCL can be perfectly converted to JSON and vice verse

## Why Use Terraform? The Benefits?

* Easy to use (learning curve not too steep)
* Sort-of open source
  * Since 2023, uses Business Source Licence (BSL) 
  * Some organisations are moving towards using OpenTofu (an open-source drop-in)
* Declarative
  * About the destination, not the journey (you tell it what you want at the end)
* Cloud-agnostic
  * Means not fussy - can use any cloud providers
    * to support a cloud provider, you need to first download the "provider" (plugin) for 

## In IaC, What Is Orchestration? How Does Terraform Act As "Orchestrator"?

* Process of automating and managing the entire lifecycle of infrastructure resource
* Takes care of order in which to create/modify/destroy

## Best Practice Supplying AWS Credentials to Terraform

Look for credentials in this order:
   1. Environment variables - AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY (OK if just for local use, and just you using)
   2. Terraform variables - should never do this because we NEVER hardcode credentials
   3. AWS CLI when you run `aws config`
   4. If using Terraform on EC2 instance, we can give an IAM role - this is best practice

## How Should AWS Credentials Never Be Passed To Terraform?
* Never hard-code them - and they must NEVER end up on a public Git repo

## Why Use Terraform For Different Environments (e.g. production, testing, etc)

Examples
* Testing environment
  * Easily/ quickly spin up infrastructure for testing purposes that mirrors production, easily/quickly bring it down at close of business (COB) or close of testing
  * Consistency between environments (this applies to other environments too, not just testing), reducing bugs caused by environment discrepancies

## Useful Websites:
* https://registry.terraform.io/providers/hashicorp/aws/latest/docs
* 