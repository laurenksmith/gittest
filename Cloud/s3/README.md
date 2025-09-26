# AWS S3

- [AWS S3](#aws-s3)
  - [What is S3?](#what-is-s3)
  - [Prerequisites](#prerequisites)
  - [1) Install and Configure AWS CLI](#1-install-and-configure-aws-cli)
  - [2) Create a Bucket](#2-create-a-bucket)
  - [3) View Contents of a Bucket](#3-view-contents-of-a-bucket)
  - [4) Create a File and Upload to Bucket](#4-create-a-file-and-upload-to-bucket)
  - [5) Download Files from a Bucket](#5-download-files-from-a-bucket)
  - [6) Delete a Single File](#6-delete-a-single-file)
  - [7) Delete Multiple Files](#7-delete-multiple-files)
  - [8) Delete a Bucket](#8-delete-a-bucket)
  - [Helpful Commands](#helpful-commands)


## What is S3?
**Amazon Simple Storage Service (S3)** is object storage in AWS.  
- Files are stored as **objects** inside **buckets**.  
- Buckets are globally unique containers.  
- S3 is durable, scalable, and can be accessed via the Console, SDKs, or the **AWS CLI**.


## Prerequisites
- Ubuntu VM with internet access
- Python 3 & pip
- AWS Access Key ID + Secret Access Key (from your IAM user)
- Default region: `eu-west-1` (Ireland)
- Default output format: `json`


## 1) Install and Configure AWS CLI

```bash
# Update system
sudo apt-get update && sudo apt-get -y upgrade

# Install pip (if not already installed)
sudo apt-get -y install python3-pip

# Install AWS CLI
sudo pip3 install awscli

# Verify installation
aws --version

# Configure credentials
aws configure
# Paste Access Key ID
# Paste Secret Access Key
# Default region: eu-west-1
# Default output format: json
````

Check it worked:

```bash
aws s3 ls   # lists all buckets you have access to
```

## 2) Create a Bucket

> **Bucket names must be globally unique. Change the placeholder below.**

```bash
aws s3 mb s3://tech511-lauren-first-bucket
aws s3 ls
```

## 3) View Contents of a Bucket

```bash
aws s3 ls s3://tech511-lauren-first-bucket/
```

## 4) Create a File and Upload to Bucket

```bash
# Create test file
echo "Hello S3" > test.txt

# Upload file to bucket
aws s3 cp test.txt s3://tech511-lauren-first-bucket/test.txt

# Verify upload
aws s3 ls s3://tech511-lauren-first-bucket/
```

## 5) Download Files from a Bucket

```
# Create downloads folder
mkdir -p ~/downloads && cd ~/downloads

# Download ALL files from the bucket
aws s3 sync s3://tech511-lauren-first-bucket/ .

# Download a single file
aws s3 cp s3://tech511-lauren-first-bucket/test.txt ./test.txt
```

## 6) Delete a Single File

```
aws s3 rm s3://tech511-lauren-first-bucket/test.txt
aws s3 ls s3://tech511-lauren-first-bucket/
```

## 7) Delete Multiple Files

⚠️ **Danger:** This removes **all objects** in the bucket.

```
aws s3 rm s3://tech511-lauren-first-bucket/ --recursive
aws s3 ls s3://tech511-lauren-first-bucket/
```

## 8) Delete a Bucket

* **Empty bucket:**

```
aws s3 rb s3://tech511-lauren-first-bucket
```

* **Bucket with files (force delete):**
  ⚠️ **Highly destructive – no confirmation prompts.**

```
aws s3 rb s3://tech511-lauren-first-bucket --force
```

## Helpful Commands

```
aws help
aws s3 help
aws s3 rm help
aws s3 rb help
```

