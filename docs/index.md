# Building Blocks Explorer Hands-on

From a business need to an evidence-based recommendation in **60 minutes**.

This workshop is for **Build Sales colleagues who are new to Building Blocks**. You will use IBM Bob to explore reusable capabilities and prepare the next conversation with an engineer or partner. Coding experience is not required.

!!! info "Before the session"
    IBM Bob is already installed, signed in, and usable. Bring a macOS or Windows computer with internet access and permission to install uv. A browser and Bob are sufficient to start; uv installation is included in the hour. Use the fictional scenarios provided here.

## Your route through the hour

| Elapsed time | Activity | Completion check |
|---|---|---|
| 00–10 | Recap on this page | Explain what Explorer helps you do |
| 10–20 | [Install uv](preparation.md) | Confirm uv and uvx versions |
| 20–30 | [Open Explorer](part1.md) | Get a catalog-backed answer |
| 30–42 | [Exercise 1](part2.md#exercise-1) | Explain two candidate blocks and their evidence |
| 42–55 | [Exercise 2](part2.md#exercise-2) | Prepare an engineering handoff |
| 55–60 | [Review](summary.md) and [feedback](feedback.md) | Deliver a 30-second pitch |

The [third challenge](part3.md) is optional, taking 5–10 extra minutes or time left after the required exercises. Two completed exercises meet the workshop goal.

## Recap: what are Building Blocks?

**Building Blocks** are reusable reference implementations and engineering patterns from IBM's Build Engineering team. They help teams explore how IBM capabilities can fit a solution. Their contents vary: documentation, runnable assets, Bob skills, or Bob modes may be available. Start with the actual README to see what a candidate provides.

The current upstream overview is organized around these areas:

| Area | Current groups in the upstream overview | A question a seller might hear |
|---|---|---|
| AI | Agents, AI Engineering, AI Trust | “How can we support a user task and evaluate the result?” |
| Data | Context, Pipelines, Query Engines | “How do we make our documents and data usable?” |
| Automation | Operate, Secure, Optimize | “How do we improve operations, security, or cost?” |

Checked September 10, 2026 against the [upstream overview at the reviewed commit](https://github.com/ibm-self-serve-assets/building-blocks/blob/f721f5ec1915225ade62d8d0e780fe6b19aa58b8/README.md). Follow the [current overview](https://github.com/ibm-self-serve-assets/building-blocks) for changes after this workshop version. Do not memorize a block count: the portfolio changes.

!!! note "The catalog and the overview may differ"
    On the review date, the live Explorer catalog still used some earlier group names and paths. If a returned link fails, open the current overview and locate the relevant README. Record an unresolved difference as a follow-up; a catalog recommendation alone is not proof that an asset can be installed.

## Four terms to recognize

| Term | In this workshop |
|---|---|
| Building Block | A reusable capability or implementation pattern to investigate |
| Explorer | A Bob mode that searches the catalog and helps shape a solution |
| Bob mode | The working context you select in Bob |
| Bob skill | Task-specific guidance that can be installed in a workspace |

**MCP** connects Bob to tools. Explorer uses a remote catalog service to discover materials and a local installer to add selected skills or modes. **uv** runs that local helper and can supply its Python runtime. You do not need to install Python separately for this workshop.

Source: [official Explorer guide](https://github.com/ibm-self-serve-assets/building-blocks/blob/f721f5ec1915225ade62d8d0e780fe6b19aa58b8/explore-BBs/README.md).

## What to say in a sales conversation

Use this sequence: **business problem → candidate capability → evidence → next validation**.

For example: “A support team spends time finding answers in policy documents. We can explore a document-retrieval pattern and an assistant interface. We will check their available assets and agree with engineering how to test answer quality and access control.”

A reference implementation does not establish a customer's ROI, deployment readiness, licensing, or support terms. You can use it to make a proposal concrete and identify what must be validated. Keep those two parts together when you explain its value.

- [ ] I can distinguish a Building Block, Explorer, a mode, and a skill.
- [ ] I can explain why a recommendation needs a source and a next check.

[Next: install uv →](preparation.md)
