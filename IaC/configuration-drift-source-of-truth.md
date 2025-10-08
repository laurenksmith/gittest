- [Source of Truth](#source-of-truth)
  - [ChatGPT Explanation](#chatgpt-explanation)
    - [Example with Terraform](#example-with-terraform)
  - [👉 In IaC best practice, the Terraform code is the source of truth.](#-in-iac-best-practice-the-terraform-code-is-the-source-of-truth)
  - [Analogy](#analogy)
  - [Why it matters](#why-it-matters)


# Source of Truth

## ChatGPT Explanation

**“Source of truth” in Infrastructure as Code (IaC)**

- In any system, you need one place that everyone trusts as the correct definition of how that system should look.
- In IaC, that trusted place is your code (e.g. Terraform files).

### Example with Terraform

- You might have real infrastructure running in AWS (EC2s, VPCs, SGs…).
- You might also have Terraform code that describes what should be running.
- If the AWS console and your Terraform code don’t match, you need to decide which one is the “source of truth.”

## 👉 In IaC best practice, the Terraform code is the source of truth.

**That means:**

- If something changes in AWS but isn’t reflected in your Terraform files, Terraform will detect a drift (difference).
- You then either update the code to reflect the real change, or re-apply the code to fix AWS back to what the code says.

## Analogy

**Think of it like a recipe 🥘:**

- The recipe is the source of truth.
- The dish in the oven is the real-world state.
- If someone adds salt directly to the oven dish without updating the recipe, the recipe and the food don’t match anymore.
- Next time you cook, you either:
- Add that salt to the recipe (so it’s consistent forever), or
- Follow the original recipe exactly and the “rogue salt” gets ignored.

## Why it matters

- Everyone on the team can trust the code as the official definition of infrastructure.
- Makes infrastructure reproducible (spin it up anywhere, same every time).
- Prevents hidden changes (like someone tweaking a security group in the AWS console at 2am).