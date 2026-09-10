# Exercises

Time: 25 minutes (30–55)

Use Explorer with the fictional scenarios below. Record sources and distinguish facts from assumptions. Do not enter real credentials or deploy products; creating the local handoff document is part of Exercise 2.

## Exercise 1: document assistant {#exercise-1}

10 minutes

### Step 1: Find candidates

Start a new conversation and paste:

```text
A fictional retailer needs an assistant that answers employees' product and policy questions from approved documents.
It must cite sources and say when an answer cannot be found.

Use the catalog tools to propose two Building Blocks.
For each, give the reason, source URL, available assets, prerequisites, and one point to validate.

Ask at most two clarifying questions, one at a time.
Do not install anything or deploy.
```

If asked, use fictional PDF/text documents as inputs and store employees as users.

### Step 2: Check the sources

Open each README and check the assets and prerequisites. If a link fails, search from the [Building Blocks overview](https://github.com/ibm-self-serve-assets/building-blocks). Mark anything you cannot confirm as unverified.

Possible candidates: [RAG](https://github.com/ibm-self-serve-assets/building-blocks/tree/main/data/pipelines/rag) and [Agent Builder](https://github.com/ibm-self-serve-assets/building-blocks/tree/main/ai/agents/agent-builder). Other choices are acceptable with evidence.

### Step 3: Record the result

| Record | Content |
| --- | --- |
| Problem | One sentence |
| Two candidates | Names and reasons |
| Evidence | Source URLs, checked date, assets, and prerequisites |
| Next test | One point to validate |

## Exercise 2: secrets-management handoff {#exercise-2}

15 minutes

### Step 1: Find a suitable block

Start a new conversation and paste:

```text
A fictional team copies credentials into demo scripts and wants to manage secrets and machine access consistently.

Use the catalog tools to find a suitable Building Block.
Give the reason, source URL, and prerequisites.
Explain why document retrieval alone is insufficient.

Ask at most two clarifying questions, one at a time.
Do not request credentials, install anything, rotate keys, or deploy.
```

If asked, the users are a demo development team and the scripts connect to test APIs. Check the source; one entry point is [Secrets Management](https://github.com/ibm-self-serve-assets/building-blocks/tree/main/automation/secure/non-human-identity-and-secret-management/secrets-management).

### Step 2: Create a handoff

```text
Create use_case_summary.md in the workspace root for an engineer.

Include the problem, users, scope, candidate and rationale, source URL, prerequisites, two open questions, and a next test with a success criterion.

Separate verified facts from assumptions.
Use only the fictional scenario.
Do not install anything, configure services, or deploy.
```

Approve the requested local document write if prompted. If Bob cannot write it, copy the answer into the worksheet.

### Step 3: Review the result

Check the source supports the recommendation and the handoff includes two open questions and an observable success criterion. For example, plan to test retrieval of a dummy secret without hardcoding it; do not run that test during this workshop.

[Next →](summary.md){ .workshop-next }
