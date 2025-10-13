# Sparta Projects

A collection of my learning from the **Sparta Global Academy** — culminating in my role as a **Level 2 Support Engineer**.
This repo gathers hands-on exercises, mini-projects, and full pipelines across:

* **Python** (scripts, small apps, testing, packaging)
* **Linux & Bash** (CLI, file ops, SSH, process mgmt)
* **Cloud (AWS)** (EC2, networking/VPC, AMIs, security groups)
* **Infrastructure as Code (Terraform)** (modular VPC, EC2, userdata)
* **Configuration Management (Ansible)** (controller + app/db nodes, idempotent playbooks)
* **CI/CD (Jenkins)** (three-job pipeline: test → merge → deploy)

> My focus: reliable, supportable systems with clear runbooks, troubleshooting notes, and an “ops-first” mindset.

---

## Table of Contents

- [Sparta Projects](#sparta-projects)
  - [Table of Contents](#table-of-contents)
  - [Repo Structure](#repo-structure)
  - [Highlights by Area](#highlights-by-area)
    - [Python](#python)
    - [Linux \& Bash](#linux--bash)
    - [Cloud (AWS)](#cloud-aws)
    - [Terraform](#terraform)
    - [Ansible](#ansible)
    - [CI/CD with Jenkins](#cicd-with-jenkins)
  - [End-to-End Pipeline (Two-Tier App)](#end-to-end-pipeline-two-tier-app)
  - [How to Use This Repo](#how-to-use-this-repo)
  - [Evidence \& Screens](#evidence--screens)
  - [Troubleshooting \& KEDB](#troubleshooting--kedb)
  - [Roadmap / Next Steps](#roadmap--next-steps)
  - [About Me](#about-me)
    - [Quick Links (replace with actual paths/URLs)](#quick-links-replace-with-actual-pathsurls)

---

## Repo Structure

```
Sparta-Projects/
├─ python/                  # Scripts, small apps, unit tests
│  ├─ README.md
│  └─ ...
├─ linux-bash/              # CLI, file ops, SSH, process mgmt
│  ├─ README.md
│  └─ ...
├─ cloud-aws/               # EC2, AMIs, SGs, networking fundamentals
│  ├─ README.md
│  └─ ...
├─ terraform/               # IaC: VPC, subnets, EC2, userdata
│  ├─ modules/
│  ├─ envs/
│  ├─ README.md
│  └─ ...
├─ ansible/                 # Controller + app-node + db-node
│  ├─ controller/
│  ├─ app-node/
│  ├─ db-node/
│  ├─ playbooks/
│  ├─ inventory/
│  ├─ README.md
│  └─ ...
├─ cicd-jenkins/            # 3-job pipeline: test → merge → deploy
│  ├─ job1-ci-test/
│  ├─ job2-merge/
│  ├─ job3-cd-deploy/
│  ├─ README.md
│  └─ ...
├─ diagrams/                # Mermaid/Canva diagrams for pipelines & VPCs
├─ kedb-runbooks/           # Known Error DB + runbooks & SOPs
└─ README.md                # ← you are here
```

---

## Highlights by Area

### Python

* Small utilities and learning exercises (functions, OOP, files, CLI tools).
* **Testing** with `unittest`/`pytest`, basic mocking, and CI integration.
* Packaging basics and virtual environments for reproducible runs.

**Start here:** `python/README.md`
**Try:** `python/<project>/` and run instructions inside each subfolder.

---

### Linux & Bash

* Everyday ops: navigation, permissions, `mv/cp/grep/sed/awk`, service mgmt.
* SSH workflows with keys; SCP/rsync for deployments.
* Useful snippets you actually run in support scenarios.

**Start here:** `linux-bash/README.md`

---

### Cloud (AWS)

* **EC2** lifecycle, AMIs, key pairs, Security Groups, userdata bootstrapping.
* **Networking** foundations: subnets, IGW vs NAT, route tables.
* “Source of truth” mindset: record actual infra states and changes.

**Start here:** `cloud-aws/README.md`

---

### Terraform

* From single-VM to **modular** IaC: VPC, public/private subnets, SGs, EC2.
* Using **variables**, **outputs**, and environment-specific `*.tfvars`.
* Userdata to bootstrap app instances consistently.

**Start here:** `terraform/README.md`
**Look at:** `terraform/modules/` and `terraform/envs/`

---

### Ansible

* **Controller + targets** pattern: inventory, groups, SSH connectivity.
* **Idempotent** roles/playbooks for:

  * App node: Node.js app service (front page), env vars.
  * DB node: MongoDB 7.x install/config (`bindIp 0.0.0.0`), service enable/restart.
* Ad-hoc commands for verification (status, config checks).

**Start here:** `ansible/README.md`
**Playbooks:** `ansible/playbooks/*.yml`

---

### CI/CD with Jenkins

* Three-job pipeline used in class and extended for my projects:

  1. **Job 1 (CI/Test):** pull code, install deps, run unit tests.
  2. **Job 2 (Merge/Promote):** gated merge `dev → main` after passing tests.
  3. **Job 3 (CD/Deploy):** deliver build to EC2 via **SCP/rsync**, restart service.
* Credentials hygiene (SSH keys), logs, and post-build actions.

**Start here:** `cicd-jenkins/README.md`

---

## End-to-End Pipeline (Two-Tier App)

> The “capstone” flow showing how the pieces fit:

1. **Code** → Commit to GitHub (`dev` branch).
2. **CI** → Jenkins Job 1 runs tests on push.
3. **Promote** → Jenkins Job 2 merges `dev → main` on green builds.
4. **Infra** → Terraform ensures app/db infra exists and is correct.
5. **Config** → Ansible configures app and database nodes idempotently.
6. **Deploy** → Jenkins Job 3 syncs the app build to EC2 and restarts the service.
7. **Verify** → Health checks + basic smoke tests (front page, `/posts` backed by MongoDB).

**Diagrams:** see `diagrams/` for CI/CD and VPC topology.

---

## How to Use This Repo

* Each top-level folder has its **own `README.md`** with prerequisites and commands.
* Most projects are **Linux-first**; use a terminal with Bash/Zsh or WSL.
* For AWS/Terraform/Ansible sections you’ll need:

  * An AWS account + key pair
  * `awscli`, `terraform`, `ansible`, and `ssh` installed
  * Environment variables or profiles configured for AWS auth

> Tip: Follow the order **Terraform → Ansible → Jenkins** if you want to reproduce the full pipeline.

---

## Evidence & Screens

* Key screenshots, diagrams, and notes live in:

  * `diagrams/`
  * `cicd-jenkins/job*/`
  * `kedb-runbooks/`

You’ll also find links in sub-`README.md` files to demo URLs (when live) and logs/output snippets.

---

## Troubleshooting & KEDB

Production thinking from day one. I log:

* **Symptoms** → **Root cause** → **Fix** → **Prevention**
* Common Jenkins failures (agent labels, credentials, workspace paths)
* SSH/SCP issues (permissions, known_hosts, file paths)
* Terraform drift vs source-of-truth notes
* Ansible idempotency and handler gotchas

See `kedb-runbooks/` for Known Error Database entries and printable runbooks.

---

## Roadmap / Next Steps

* Add **CloudWatch** metrics/alarms and basic log shipping.
* Parameterise Jenkins jobs for **blue/green** or **canary** style demos.
* Extend Terraform modules for **ALB + Target Groups + ASG**.
* Convert Ansible tasks into **roles** with Molecule tests.
* Add GitHub Actions examples alongside Jenkins.

---

## About Me

I’m **Lauren**, now a **Level 2 Support Engineer** (ex-primary teacher). I love building reliable systems, documenting clearly, and leaving things better than I found them. I’ve been **investing in myself**, and I’m now looking to **add value and use all the skills I’ve learnt to date** in real-world teams.

* **Focus areas:** Supportability, CI/CD, Infra as Code, clear runbooks.
* **Connect:** *(add your LinkedIn/GitHub profile links here)*

---

### Quick Links (replace with actual paths/URLs)

* Two-tier app overview → `diagrams/`
* Jenkins pipeline → `cicd-jenkins/README.md`
* Terraform VPC module → `terraform/modules/vpc/`
* Ansible DB playbook → `ansible/playbooks/prov-db.yml`
* KEDB & runbooks → `kedb-runbooks/`

---

If you want, I can also tailor this with **direct links to your actual folders/files** (once you confirm your exact paths), or add a small badge section at the top.
