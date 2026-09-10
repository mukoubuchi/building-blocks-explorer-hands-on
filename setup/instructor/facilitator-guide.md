# Facilitator guide

## Audience and outcome

This is a 60-minute beginner workshop delivered in English or Japanese. Bob is already installed and usable. The goal is a sourced business recommendation and a small engineering handoff, not a product deployment. Complete two exercises.

## Before delivery

1. Read `source-review.md`. Check the current Building Blocks overview, the official Explorer ZIP, and the live catalog on the network participants will use.

1. Rehearse the exact participant instructions in Bob on at least one macOS and one Windows machine. Record OS, Bob, uv/uvx versions, date, connection results, and time to the first catalog-backed response. Static documentation checks are not a substitute for this rehearsal.

1. Verify both catalog and installer connections, then run the two prompts and review their sources. Check whether the known catalog path issues are still present.

1. Confirm attendees can sign in to Bob, download from GitHub/raw.githubusercontent.com, install uv, and reach the Code Engine catalog endpoint. The local helper may need Python/package downloads from the normal uv package sources. Use the organization's approved access process.

1. Build the participant ZIPs and share the appropriate language through an approved channel. Private release URLs require repository access. Provide an accessible workshop URL or a reviewed local/site export; do not assume private repository access for all participants.

1. Prepare a pairing arrangement and the three verified README entry points below. If the live catalog is unavailable, a source-reading exercise remains useful but must be recorded as a fallback, not a completed Explorer test.

## Run of show

| Clock | Action | Stop rule |
| --- | --- | --- |
| 00–10 | Recap AI, Data, Automation; distinguish block, mode, skill, Explorer | Avoid enumerating every block or promising ROI |
| 10–20 | Install uv in OS tabs; confirm uv and uvx; restart Bob | At minute 20 pair blocked participants |
| 20–30 | Open ZIP workspace, select Explorer, check two MCP connections | Confirm an actual catalog tool result |
| 30–40 | Exercise 1: document assistant | At minute 40 retain two candidates and sources, even if one source is unresolved |
| 40–55 | Exercise 2: secrets-management handoff | At minute 55 stop at a short document; no deployment |
| 55–60 | Review completion and save results | Save both exercise results |

## Exercise 1 coaching

Use fictional product/policy documents. If participants are stuck, supply these clarifications: store employees, discovery demo, answers with citations, explicit refusal when no source supports the answer.

Possible candidates are [RAG](https://github.com/ibm-self-serve-assets/building-blocks/tree/main/data/pipelines/rag) and [Agent Builder](https://github.com/ibm-self-serve-assets/building-blocks/tree/main/ai/agents/agent-builder). Accept other choices with a clear rationale. The RAG README describes a custom/reference implementation and distinguishes it from managed OpenRAG. Preserve that distinction in any explanation.

A satisfactory record has two named candidates, source URLs, a verified capability or explicitly unresolved source, and a next validation. Example next question: how will we check that each answer cites an accessible, relevant document? No exact architecture or identical model answer is required.

## Exercise 2 coaching

Use the [Secrets Management README](https://github.com/ibm-self-serve-assets/building-blocks/tree/main/automation/secure/non-human-identity-and-secret-management/secrets-management) for the Vault-related material, under the broader identity block. The parent README focuses on IBM Security Verify, so do not treat the parent alone as evidence of the Vault workflow.

Keep the setting at discovery. No participant should enter a real secret, run a migration, rotate a key, or deploy a service. They may write the requested local handoff. A valid handoff states the problem and scope, candidate and rationale, evidence, prerequisites, two open questions, and a next test with an observable result.

Illustrative questions: who owns the identity, and who owns the secret lifecycle? A next-step proposal can test retrieving a dummy secret in an approved sandbox. It is a future engineering task, not part of the class.

## Handling upstream inconsistencies

The root overview and the Explorer catalog can change at different times. Keep catalog results and current source evidence distinguishable. Do not patch the official Explorer configuration or invent replacement commands during class. A failed link should lead to source checking, a recorded uncertainty, and a bounded follow-up.

If the installer fails but the catalog works, both required exercises can continue. If the catalog fails, pair participants or use the README fallback. Report how the exercise was completed.

## Completion

Check for understanding rather than identical output: participants can explain the business problem, why the candidate fits, what the source proves, and the next validation.

## Delivery record

Fill these fields before presenting this material as rehearsed:

- Date and workshop release:
- macOS / Bob / uv / uvx versions and result:
- Windows / Bob / uv / uvx versions and result:
- Remote catalog and local installer result:
- Actual time to finish each required exercise:
- Known issues and pairing/fallback used:

The initial v0.1.0 draft has documentation and service-level checks; an interactive Bob rehearsal on both operating systems remains required.
