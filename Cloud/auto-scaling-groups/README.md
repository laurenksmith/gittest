# AWS Auto Scaling Groups (ASG)

- [AWS Auto Scaling Groups (ASG)](#aws-auto-scaling-groups-asg)
  - [Overview](#overview)
  - [1. Purpose of Scaling](#1-purpose-of-scaling)
    - [Vertical Scaling](#vertical-scaling)
    - [Horizontal Scaling](#horizontal-scaling)
  - [2. Auto Scaling Groups in AWS](#2-auto-scaling-groups-in-aws)
    - [Key Components](#key-components)
    - [How It Works](#how-it-works)
  - [3. Step-by-Step Process (What I Did)](#3-step-by-step-process-what-i-did)
    - [Step 1: Create a Launch Template](#step-1-create-a-launch-template)
    - [Step 2: Test the Launch Template](#step-2-test-the-launch-template)
    - [Step 3: Create the Auto Scaling Group](#step-3-create-the-auto-scaling-group)
    - [Step 4: Verify via Load Balancer](#step-4-verify-via-load-balancer)
    - [Step 5: Test Resilience](#step-5-test-resilience)
    - [Step 6: Clean Up](#step-6-clean-up)
  - [Key Takeaways](#key-takeaways)
  - [Why \& Benefits of Auto Scaling Groups](#why--benefits-of-auto-scaling-groups)
    - [Why We Do It](#why-we-do-it)
    - [Benefits for Me](#benefits-for-me)
    - [Benefits for the Home Office](#benefits-for-the-home-office)


## Overview
This README explains:
- The purpose of scaling (why we do it, what problems it solves).  
- The different types of scaling (vertical vs horizontal).  
- How ASGs work in practice — high availability and scalability.  
- The exact step-by-step process I followed to create an ASG from my tested AMI.  
- Key troubleshooting reminders.

This is written as if I’m explaining to my future self — so I can come back later and recreate this whole process confidently.

---

## 1. Purpose of Scaling
Scaling is all about making sure our application can handle changes in demand.  
There are **two types of scaling**:

### Vertical Scaling
- **Definition:** Increase/decrease the size of a single machine (VM).  
- **Example:** Move workload from a `t3.micro` to a `t3.large`.  
- **Steps:**  
  1. Move workload onto the bigger VM.  
  2. Remove the smaller VM.  
- **Downside:** At some point you hit the “ceiling” of the biggest VM type. Also, a single point of failure.

### Horizontal Scaling
- **Definition:** Add/remove multiple machines of the same type.  
- **Example:** Instead of one VM, run three app VMs in parallel.  
- **Steps:**  
  - Scale **out**: add more VMs.  
  - Scale **in**: remove VMs when demand drops.  
- **Benefit:** Improves fault tolerance (if one VM fails, others still serve traffic). It’s the basis of ASGs.

---

## 2. Auto Scaling Groups in AWS
An **Auto Scaling Group (ASG)** is an AWS service that ensures we always have the right number of EC2 instances running, spread across multiple Availability Zones for **High Availability (HA)** and **Scalability (SC)**.

### Key Components
- **AMI:** Snapshot of a working VM. Ensures new instances are identical.  
- **Launch Template (LT):** Blueprint storing AMI, instance type, key pair, SGs, user data.  
- **Auto Scaling Group (ASG):** Uses LT to create/manage instances across AZs.  
- **Scaling Policy:** Rules for when to add/remove instances (e.g., average CPU > 50%).  
- **Load Balancer (LB):** Front door routing traffic across multiple instances.  
- **Target Group (TG):** Instances the LB routes to, with health checks.

### How It Works
1. Start with a working app VM.  
2. Create an AMI.  
3. Build a Launch Template.  
4. Create an ASG with the LT.  
5. Attach an Application Load Balancer.  
6. Apply scaling policies.  
7. ASG automatically launches/replaces/terminates instances.

---

## 3. Step-by-Step Process (What I Did)

### Step 1: Create a Launch Template
- AMI: my tested “ready-to-run app” AMI.  
- Instance type: `t2.micro` / `t3.micro`.  
- Key pair: my key.  
- SG: allow HTTP (80), SSH (22), 3000 (optional).  
- User data: working app script (without temporary exports).  

**Why:** Ensures new VMs are consistent.

### Step 2: Test the Launch Template
- Launch instance from LT.  
- Check app loads at Public IP.  
- Terminate after success.  

**Why:** Prevents wasting time later.

### Step 3: Create the Auto Scaling Group
- Name: `la-sparta-app-asg`.  
- Attach LT (latest version).  
- Network: default VPC, 3 subnets (`eu-west-1a, 1b, 1c`).  
- LB: new ALB, HTTP:80, new Target Group, health checks.  
- Scaling policy: Desired=2, Min=2, Max=3, CPU target=50%, warm-up=120s.  
- Tag: `Name = la-sparta-app hasc`.

### Step 4: Verify via Load Balancer
- Use LB DNS.  
- Target Group shows 2 healthy instances.

### Step 5: Test Resilience
- Terminate 1 instance.  
- LB still serves traffic.  
- ASG launches replacement.

### Step 6: Clean Up
- Delete LB, Target Group, ASG.  
- Keep AMI + LT.

---

## Key Takeaways
- ASGs deliver HA + scalability.  
- If a VM fails, it’s replaced automatically.  
- If demand spikes, new VMs are added.  
- Traffic always routed via the Load Balancer.  

---

## Why & Benefits of Auto Scaling Groups

### Why We Do It
ASGs solve the problem of unpredictable demand and fragile infrastructure. They make sure the right number of healthy servers are always available.

### Benefits for Me
- Confidence in automation.  
- Practical understanding of resilience.  
- Reusable, industry-relevant skills.  
- Problem-solving mindset (systems, not just machines).  

### Benefits for the Home Office
- **High availability:** ensures critical services stay online.  
- **Scalability:** handles peak loads automatically.  
- **Cost efficiency:** scales down when demand is low.  
- **Security/consistency:** every instance from same AMI/template.  
- **Business continuity:** reduces outage risks that damage trust.  
