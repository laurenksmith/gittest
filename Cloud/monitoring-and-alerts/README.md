- [Monitoring \& Alert Management](#monitoring--alert-management)
  - [Why Monitor?](#why-monitor)
    - [Default AWS Monitoring](#default-aws-monitoring)
  - [Levels of Monitoring](#levels-of-monitoring)
  - [Practical Steps Covered](#practical-steps-covered)
  - [Key Takeaways](#key-takeaways)

# Monitoring & Alert Management

## Why Monitor?

Monitoring ensures you can track resource usage and respond to spikes before they cause failures.

### Default AWS Monitoring

- AWS provides **CloudWatch (CW)** by default.
    
- Monitors metrics like CPU load, disk, network.
    
- By default → 5-minute intervals.
    
- Can enable **Detailed Monitoring** → 1-minute intervals (extra cost).
    

---

## Levels of Monitoring

1. **Dashboard**
    
    - Displays metrics (e.g. CPU load) as charts.
        
    - Problem: only useful if someone is watching. Easy to miss issues.
        
2. **Alarms**
    
    - Triggered when metrics exceed thresholds.
        
    - Typically use averages (e.g. CPU > 50% for 5 minutes).
        
    - Reduce false positives from momentary spikes.
        
3. **Notifications**
    
    - Delivered via channels (email, SMS, apps, etc.).
        
    - Allow remote response, e.g. on holiday with your phone.
        
    - Still manual — someone must act.
        
4. **Auto Scaling**
    
    - Automates the response.
        
    - Example: when CPU load too high, launch new instances.
        
    - Removes reliance on human intervention.
        

---

## Practical Steps Covered

1. **Create Dashboard**
    
    - Use EC2 → Monitoring tab → _Add to Dashboard_.
        
    - Charts include CPU, disk I/O, network traffic.
        
    - Can customise which metrics to show.
        
2. **Enable Detailed Monitoring**
    
    - Updates every 1 minute.
        
    - Extra cost, so used selectively.
        
3. **Trigger Alarms & Notifications**
    
    - Define threshold (e.g. CPU > 70%).
        
    - Configure SNS to send alerts to email.
        
4. **Load Testing & Stress Testing**
    
    - **Load Testing** = simulate typical user load.
        
    - **Stress Testing** = push system until it breaks.
        
    - Tool: **Apache Bench (ab)**
        
        `ab -n 1000 -c 100 http://<PUBLIC-IP>/`
        
        - `-n` = total requests
            
        - `-c` = concurrency (requests at a time)
            
    - Use AB to deliberately spike CPU and test alarm thresholds.
        
    - Example: CPU spiked from ~2% → 11% with 10,000 requests.
        

---

## Key Takeaways

- Dashboards = visibility, but manual.
    
- Alarms = proactive, but still human-dependent.
    
- Notifications = flexible, but still reactive.
    
- Auto Scaling = automated resilience (best).
    
- Load testing tools (like Apache Bench) help validate thresholds.
    
- Stress testing reveals breaking points.


ab -n 1000 -c 100 http://54.217.111.62/ #command for apache testing
ab -n 10000 -c 200 http://54.217.111.62/

