# Monitoring and Alerts Task

- [Monitoring and Alerts Task](#monitoring-and-alerts-task)
  - [Overview](#overview)
  - [1. Setup a Dashboard](#1-setup-a-dashboard)
    - [Steps](#steps)
  - [2. Create a CPU Usage Alarm](#2-create-a-cpu-usage-alarm)
    - [Steps](#steps-1)
  - [](#)
  - [3. Trigger the Alarm](#3-trigger-the-alarm)
    - [Steps to Spike CPU](#steps-to-spike-cpu)
  - [4. What Happens When The Alarm is Triggered](#4-what-happens-when-the-alarm-is-triggered)
  - [](#-1)
  - [5. Clean Up](#5-clean-up)
  - [Key Takeaways](#key-takeaways)
  - [Why \& Benefits of Monitoring and Alerts](#why--benefits-of-monitoring-and-alerts)
    - [Why We Do It](#why-we-do-it)
    - [Benefits for Me](#benefits-for-me)
    - [Benefits for the Home Office](#benefits-for-the-home-office)

## Overview
This README explains how to set up monitoring and alerts for an EC2 instance using **Amazon CloudWatch**.  
The goal was to:  
- Create a dashboard.  
- Configure alarms.  
- Test them by spiking CPU load.  
- Understand the automated response flow.  

---

## 1. Setup a Dashboard

### Steps
1. AWS Console → CloudWatch → Dashboards → **Create dashboard**.  
2. Name: `tech511-lauren-sparta-test-dashboard`.  
3. Add a **Line widget**.  
4. Configure widget:  
   - Metrics → EC2 → Per-Instance Metrics.  
   - Select instance ID.  
   - Metric: **CPUUtilization**.  
5. Enable **Detailed Monitoring** if not already enabled (Monitoring tab in EC2).  
6. Save dashboard.  


![alt text](Dashboard.png)

## 2. Create a CPU Usage Alarm

### Steps
1. CloudWatch → Alarms → All alarms → **Create alarm**.  
2. Metric: EC2 → Per-Instance Metrics → **CPUUtilization**.  
3. Condition:  
   - Threshold type: **Static**.  
   - Whenever CPUUtilization >= 5 (percent).  
   - Period: 60 seconds.  
4. Notifications:  
   - Create new SNS topic (e.g., `lauren-test-alarm`).  
   - Enter email + confirm subscription.  
5. Name: `tech511-lauren-sparta-alarm-test`.  
6. Create alarm.  
   
![alt text](<../images/Screenshot 2025-09-25 171544.png>)
---

## 3. Trigger the Alarm

### Steps to Spike CPU
- SSH into instance:

  `ssh -i ~/.ssh/my-key.pem ubuntu@<public-ip>`


* Run CPU-intensive commands:

  * `sudo apt update && sudo apt upgrade`
  * Or use Apache Bench (`ab`) for load testing.

---

## 4. What Happens When The Alarm is Triggered

* Alarm state: **OK → ALARM**.
* SNS sends email notification.
* Dashboard shows the spike visually.

![alt text](<../images/Screenshot 2025-09-25 171431.png>)
---

## 5. Clean Up

* Delete dashboard in CloudWatch.
* Delete CPU alarm.
* Stop or terminate EC2 instance.

---

## Key Takeaways

* Dashboards provide **visibility** into system health.
* Alarms ensure **proactive notification**.
* SNS delivers notifications by email/SMS.
* Cleaning up avoids ongoing costs.

---

## Why & Benefits of Monitoring and Alerts

### Why We Do It

Monitoring and alerts provide visibility into hidden issues. They let us catch problems early, respond before users are impacted, and maintain confidence that systems are running as expected.

### Benefits for Me

* Practical skills with CloudWatch dashboards, alarms, and SNS.
* Experience with triggering alarms in a controlled way.
* Understanding proactive monitoring instead of reactive firefighting.
* Confidence in automation (AWS watches metrics so I don’t have to manually).

### Benefits for the Home Office

* **Proactive detection:** stop issues before they hit critical services.
* **Operational efficiency:** free up teams from manual monitoring.
* **Cost control:** catch runaway processes that waste resources.
* **Security:** unusual CPU spikes can indicate intrusions/misconfigurations.
* **Trust:** ensures government services (passports, immigration, etc.) remain reliable.


