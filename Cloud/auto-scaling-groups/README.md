- [AWS Auto Scaling Groups (ASG)](#aws-auto-scaling-groups-asg)
  - [1. Purpose of Scaling](#1-purpose-of-scaling)
    - [Vertical Scaling](#vertical-scaling)
    - [Horizontal Scaling](#horizontal-scaling)
  - [2. Auto Scaling Groups in AWS](#2-auto-scaling-groups-in-aws)
    - [Key Components](#key-components)
    - [How It Works](#how-it-works)
  - [3. Step-by-Step Process (What I Did)](#3-step-by-step-process-what-i-did)
    - [Step 1: Create a Launch Template (LT)](#step-1-create-a-launch-template-lt)
    - [Step 2: Test the Launch Template](#step-2-test-the-launch-template)
    - [Step 3: Create the Auto Scaling Group (ASG)](#step-3-create-the-auto-scaling-group-asg)
    - [Step 4: Verify via the Load Balancer](#step-4-verify-via-the-load-balancer)
    - [Step 5: Test Resilience](#step-5-test-resilience)
    - [Step 6: Clean Up](#step-6-clean-up)
  - [Final Thoughts](#final-thoughts)


# AWS Auto Scaling Groups (ASG)

This README explains:

- The purpose of scaling (why we do it, what problems it solves).  
- The different types of scaling (vertical vs horizontal).  
- How ASGs work in practice — high availability and scalability.  
- The exact step-by-step process I followed to create an ASG from my tested AMI.  
- Key troubleshooting reminders.

This is written as if I’m explaining to my future self — so that I can (hopefully!) come back later and recreate this whole process confidently.

---

## 1. Purpose of Scaling

Scaling is all about making sure our application can handle changes in demand.  
There are **two types of scaling**:

### Vertical Scaling
- **Definition:** Increase/decrease the size of a single machine (VM).  
- **Example:** Move workload from a `t2.micro` to a `t2.large`.  
- **Steps involved:**  
  1. Move the workload onto the bigger VM.  
  2. Remove the smaller VM.  
- **Downside:** At some point you hit the “ceiling” of the biggest VM type. Also, this approach is a single point of failure — if that one machine goes down, everything is down.

### Horizontal Scaling
- **Definition:** Add/remove multiple machines of the same type.  
- **Example:** Instead of one VM, run three app VMs in parallel.  
- **Steps involved:**  
  - Scale **out**: add more VMs.  
  - Scale **in**: remove VMs when demand drops.  
- **Benefit:** Improves fault tolerance (if one VM fails, the load balancer can send traffic to the healthy ones). It’s the basis of **Auto Scaling Groups**.

---

## 2. Auto Scaling Groups in AWS

An **Auto Scaling Group (ASG)** is an AWS service that ensures we always have the right number of EC2 instances running, spread across multiple Availability Zones for **High Availability (HA)** and **Scalability (SC)**.

### Key Components
- **AMI (Amazon Machine Image):** Snapshot of a working VM. Ensures every new instance is identical.  
- **Launch Template (LT):** Stores all the settings (AMI, instance type, key pair, security groups, user data). It’s a blueprint for launching VMs.  
- **Auto Scaling Group (ASG):** Uses the Launch Template to create/manage instances across AZs.  
- **Scaling Policy:** Rules that tell ASG when to add/remove instances (e.g., if average CPU > 50%).  
- **Load Balancer (LB):** Front door that routes traffic across multiple instances. Users connect to the LB, not directly to the instances.  
- **Target Group (TG):** Collection of instances the LB routes traffic to. Health checks ensure only healthy instances get traffic.

### How It Works
1. Start with a **working app VM**.  
2. Create an **AMI** from it.  
3. Build a **Launch Template** that points to that AMI and includes all config.  
4. Create an **Auto Scaling Group** using the Launch Template.  
5. Attach an **Application Load Balancer** to distribute traffic.  
6. Apply a **Scaling Policy** (e.g., keep CPU around 50%).  
7. ASG automatically **launches/replaces/terminates instances** as needed.  

---

## 3. Step-by-Step Process (What I Did)

### Step 1: Create a Launch Template (LT)
- From the **EC2 console**, choose **Launch Templates → Create**.  
- Fill in:
  - **AMI:** My “ready-to-run app” AMI (tested and working).  
  - **Instance type:** `t2.micro` / `t3.micro`.  
  - **Key pair:** my key pair.  
  - **Security group:** allow **HTTP (80)** and **SSH (22)** (3000 optional for testing).  
  - **User data:** paste in my working app script (without any temporary `export` lines).  
- Save the LT.

**Why:** A Launch Template is reusable and ensures every new VM is consistent.

---

### Step 2: Test the Launch Template
- **Actions → Launch instance from template.**  
- Do not edit anything.  
- Wait for the instance to boot (takes ~30–90 seconds: VM creation → Linux boot → app start).  
- Visit the instance’s **Public IP** in the browser (make sure to use `http://`, not `https://`).  
- If the app works, **terminate the test VM**.  
- If not, fix the user data / paths / SG rules in the LT and retest.

**Why:** Testing prevents wasting time later when creating the ASG.

---

### Step 3: Create the Auto Scaling Group (ASG)
1. **EC2 → Auto Scaling Groups → Create ASG.**  
2. Give it a **name** (follow convention, e.g., `la-sparta-app-asg`).  
3. Attach the **Launch Template** (latest version).  
4. **Network:** choose the **default VPC**, then pick 3 subnets (one in each AZ: `eu-west-1a, 1b, 1c`).  
5. **Load balancing:**  
   - Attach to a **new Application Load Balancer**.  
   - **Internet-facing**, listener on **HTTP:80**.  
   - Create a **new Target Group** (short name, e.g., `app-tg`).  
   - Turn on **health checks** (HTTP 200 on port 80).  
   - Set **Health check grace period**: 120 seconds (gives time for app to boot before first check).  
6. **Scaling policy:**  
   - Desired: **2**  
   - Min: **2**  
   - Max: **3**  
   - Policy: **Target tracking**, average CPU at **50%**.  
   - Instance warm-up: 120 seconds (matches grace period).  
7. **Tags:** Add a `Name` tag (capital N), e.g., `la-sparta-app hasc`. Apply to instances.  
8. **Review & create.**

---

### Step 4: Verify via the Load Balancer
- Go to the **Load Balancer → DNS name** (looks like `my-lb-123456.eu-west-1.elb.amazonaws.com`).  
- Paste into browser with `http://`.  
- Front page should load.  
- In the Target Group, check **2 healthy instances**.

---

### Step 5: Test Resilience
- In **EC2 → Instances**, terminate one of the ASG instances.  
- Refresh the LB DNS — service should still work.  
- ASG quickly launches a replacement instance to maintain the desired capacity (2).  

---

### Step 6: Clean Up
1. Delete the **Load Balancer**.  
2. Delete the **Target Group**.  
3. Delete the **ASG** (instances terminate automatically).  
4. Keep your **AMI** and **Launch Template** for future reuse.

---
## Final Thoughts

This learning showed me how ASGs deliver **high availability** and **scalability**:  
- If a VM fails, it’s replaced automatically.  
- If demand spikes, new VMs are added.  
- Users connect through the Load Balancer, not individual VMs, so traffic is always balanced.
