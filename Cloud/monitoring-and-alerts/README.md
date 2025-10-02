# Monitoring & Alert Management

- [Monitoring \& Alert Management](#monitoring--alert-management)
  - [Overview](#overview)
  - [1. Why Monitor?](#1-why-monitor)
    - [Default AWS Monitoring](#default-aws-monitoring)
  - [2. Levels of Monitoring](#2-levels-of-monitoring)
  - [3. Practical Steps Covered](#3-practical-steps-covered)
  - [4. Key Takeaways](#4-key-takeaways)
  - [Why \& Benefits of Monitoring \& Alert Management](#why--benefits-of-monitoring--alert-management)
    - [Why We Do It](#why-we-do-it)
    - [Benefits for Me](#benefits-for-me)
    - [Benefits for the Home Office](#benefits-for-the-home-office)


## Overview
This README explains the importance of monitoring and alert management in AWS. It covers:  
- Why monitoring is essential.  
- The default monitoring AWS provides.  
- Levels of monitoring (dashboards → alarms → notifications → auto scaling).  
- Practical steps taken in CloudWatch.  
- Key lessons and testing approaches.  

---

## 1. Why Monitor?
Monitoring ensures you can track resource usage and respond to spikes before they cause failures.

### Default AWS Monitoring
- AWS provides **CloudWatch (CW)** by default.  
- Monitors metrics like CPU load, disk, and network.  
- By default → 5-minute intervals.  
- Can enable **Detailed Monitoring** → 1-minute intervals (extra cost).  

---

## 2. Levels of Monitoring
1. **Dashboard**  
   - Displays metrics as charts.  
   - Problem: only useful if someone is watching — easy to miss issues.  

2. **Alarms**  
   - Trigger when metrics exceed thresholds.  
   - Typically use averages (e.g. CPU > 50% for 5 mins).  
   - Reduce false positives from spikes.  

3. **Notifications**  
   - Delivered via email, SMS, apps.  
   - Allow remote response, but still manual.  

4. **Auto Scaling**  
   - Automates the response.  
   - Example: launch new instances when CPU is too high.  
   - Removes reliance on human intervention.  

---

## 3. Practical Steps Covered
1. **Create Dashboard**  
   - Use EC2 → Monitoring tab → *Add to Dashboard*.  
   - Charts: CPU, disk I/O, network traffic.  
   - Customisable metrics.  

2. **Enable Detailed Monitoring**  
   - Updates every 1 min.  
   - Extra cost, so used selectively.  

3. **Trigger Alarms & Notifications**  
   - Define threshold (e.g. CPU > 70%).  
   - Configure SNS to email alerts.  

4. **Load Testing & Stress Testing**  
   - **Load Testing:** simulate typical user load.  
   - **Stress Testing:** push system until it breaks.  
   - Tool: Apache Bench (`ab`)  
     ```
     ab -n 1000 -c 100 http://<PUBLIC-IP>/
     ab -n 10000 -c 200 http://<PUBLIC-IP>/
     ```  
   - Example: CPU spiked from ~2% → 11% with 10,000 requests.  

---

## 4. Key Takeaways
- Dashboards = visibility, but manual.  
- Alarms = proactive, but still human-dependent.  
- Notifications = flexible, but reactive.  
- Auto Scaling = automated resilience (best).  
- Load testing validates thresholds.  
- Stress testing reveals breaking points.  

---

## Why & Benefits of Monitoring & Alert Management

### Why We Do It  
Monitoring and alerts transform hidden issues into visible, actionable signals. They ensure we don’t wait until users complain to notice a failure. Load/stress testing validates that alerts and systems work under real-world pressure.  

### Benefits for Me
- Learned how to configure dashboards, alarms, and SNS in CloudWatch.  
- Gained experience with Apache Bench to generate realistic loads.  
- Saw the difference between proactive and reactive approaches.  
- Built confidence in handling system stress safely.  
- Understood the trade-off of costs (detailed monitoring) vs value.  

### Benefits for the Home Office
- **Operational resilience:** ensures systems are monitored and recover quickly.  
- **Scalable response:** metrics can trigger auto scaling, not just alerts.  
- **Efficiency:** teams don’t waste time manually checking dashboards.  
- **Incident management:** instant alerts reduce mean time to recovery (MTTR).  
- **Trust:** ensures reliability of critical government services.  
- **Cost control:** stress testing highlights inefficiencies and saves money.  


