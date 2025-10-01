# AWS S3

- [AWS S3](#aws-s3)
  - [Overview](#overview)
  - [1. What is S3?](#1-what-is-s3)
  - [2. Prerequisites](#2-prerequisites)
  - [3. Install and Configure AWS CLI](#3-install-and-configure-aws-cli)
  - [4. Create a Bucket](#4-create-a-bucket)
  - [5. View Contents of a Bucket](#5-view-contents-of-a-bucket)
  - [6. Create a File and Upload to Bucket](#6-create-a-file-and-upload-to-bucket)
  - [7. Download Files from a Bucket](#7-download-files-from-a-bucket)
  - [8. Delete a Single File](#8-delete-a-single-file)
  - [9. Delete Multiple Files](#9-delete-multiple-files)
  - [10. Delete a Bucket](#10-delete-a-bucket)
  - [Helpful Commands](#helpful-commands)
  - [Key Takeaways](#key-takeaways)
  - [Why \& Benefits of AWS S3](#why--benefits-of-aws-s3)
    - [Why We Do It](#why-we-do-it)
    - [Benefits for Me](#benefits-for-me)
    - [Benefits for the Home Office](#benefits-for-the-home-office)

## Overview
This README covers how to use **Amazon Simple Storage Service (S3)** with the AWS CLI:  
- What S3 is and why it’s used.  
- Setting up prerequisites.  
- Creating and managing buckets.  
- Uploading, downloading, and deleting files.  
- Cleaning up safely.  

---

## 1. What is S3?
**Amazon S3** is object storage in AWS.  
- Files are stored as **objects** inside **buckets**.  
- Buckets are globally unique.  
- S3 is durable, scalable, and accessible via Console, SDKs, or CLI.  

---

## 2. Prerequisites
- Ubuntu VM with internet access.  
- Python 3 & pip.  
- AWS Access Key ID + Secret Access Key (IAM user).  
- Default region: `eu-west-1` (Ireland).  
- Default output: `json`.  

---

## 3. Install and Configure AWS CLI

```bash
# Update system
sudo apt-get update && sudo apt-get -y upgrade

# Install pip
sudo apt-get -y install python3-pip

# Install AWS CLI
sudo pip3 install awscli

# Verify
aws --version

# Configure credentials
aws configure
# Access Key ID
# Secret Access Key
# Region: eu-west-1
# Output: json
```
Check:

```
aws s3 ls
```

---

## 4. Create a Bucket

 Bucket names must be globally unique.

```
aws s3 mb s3://tech511-lauren-first-bucket
aws s3 ls
```

---

## 5. View Contents of a Bucket

```
aws s3 ls s3://tech511-lauren-first-bucket/
```

---

## 6. Create a File and Upload to Bucket

```
echo "Hello S3" > test.txt
aws s3 cp test.txt s3://tech511-lauren-first-bucket/test.txt
aws s3 ls s3://tech511-lauren-first-bucket/
```

---

## 7. Download Files from a Bucket

```
mkdir -p ~/downloads && cd ~/downloads
aws s3 sync s3://tech511-lauren-first-bucket/ .
aws s3 cp s3://tech511-lauren-first-bucket/test.txt ./test.txt
```

---

## 8. Delete a Single File

```
aws s3 rm s3://tech511-lauren-first-bucket/test.txt
aws s3 ls s3://tech511-lauren-first-bucket/
```

---

## 9. Delete Multiple Files

⚠️ Removes all objects in the bucket.

```
aws s3 rm s3://tech511-lauren-first-bucket/ --recursive
aws s3 ls s3://tech511-lauren-first-bucket/
```

---

## 10. Delete a Bucket

*Empty bucket:*

```
aws s3 rb s3://tech511-lauren-first-bucket
```

*Force delete (bucket + contents):*

```
aws s3 rb s3://tech511-lauren-first-bucket --force
```

---

## Helpful Commands

```
aws help
aws s3 help
aws s3 rm help
aws s3 rb help
```

---

## Key Takeaways

* S3 provides scalable, reliable object storage.
* Buckets must be globally unique.
* CLI gives fine-grained control over bucket/file operations.
* Cleanup is critical to avoid costs or clutter.

---

## Why & Benefits of AWS S3

### Why We Do It

S3 removes the limitations of local/server storage. It provides a reliable, infinitely scalable, secure way to store files in the cloud, integrated with AWS services.

### Benefits for Me

* Learned to manage S3 via CLI (not just Console).
* Gained understanding of object vs block storage.
* Confidence handling bucket/file lifecycle (upload, download, delete).
* Awareness of cost implications and importance of cleanup.
* Built skills that are a foundation for many advanced AWS workflows.

### Benefits for the Home Office

* **Durability:** 99.999999999% durability ensures critical records aren’t lost.
* **Scalability:** Can handle vast datasets without redesign.
* **Security & compliance:** IAM, encryption, and bucket policies protect sensitive data.
* **Cost efficiency:** Pay-as-you-go avoids wasted spend.
* **Integration:** Works with many AWS services (Lambda, CloudFront, Athena).
* **Disaster recovery:** Supports quick recovery and backup for mission-critical services.
