# Facilitator guide

## Audience and outcome

This is a 60-minute beginner workshop delivered in English or Japanese. Bob is already installed and usable. The goal is catalog research followed by discovering and using a related skill or mode, without product deployment. Complete two exercises.

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
| 30–40 | Exercise 1: find all related Building Blocks | At minute 40 record all discovered related BBs, sources, and unchecked areas |
| 40–55 | Exercise 2: discover and use a related skill or mode | At minute 55 retain evidence of use or record incomplete steps; no deployment |
| 55–60 | Review completion and save results | Save both exercise results |

## Exercise 1 coaching

Use fictional product/policy documents. If participants are stuck, supply these clarifications: store employees, discovery demo, answers with citations, explicit refusal when no source supports the answer.

Possible candidates are [RAG](https://github.com/ibm-self-serve-assets/building-blocks/tree/main/data/pipelines/rag) and [Agent Builder](https://github.com/ibm-self-serve-assets/building-blocks/tree/main/ai/agents/agent-builder). Accept other choices with a clear rationale. The RAG README describes a custom/reference implementation and distinguishes it from managed OpenRAG. Preserve that distinction in any explanation.

A satisfactory Markdown record lists all discovered related BBs, source URLs, verified capabilities or explicitly unresolved sources, and search coverage. Example next question: how will we check that each answer cites an accessible, relevant document? No exact architecture or identical model answer is required.

## Exercise 2 coaching


Continue the Exercise 1 document-assistant scenario. Search all catalog results without a fixed candidate count and record unchecked areas. Select the most relevant BB, then discover an associated skill or mode; do not add a comparison activity. Let participants discover related skills or modes through the catalog and review purpose, official source, prerequisites, and workspace changes before selecting one. Do not prescribe an asset name. Prefer a candidate usable without additional credentials or services. After installation and Bob reload, explicitly name the skill or select the mode and apply it to the supplied fictional product documents. Check evidence that its procedures informed the answer. Installation alone is not completion. If downloads or prerequisites block use, try another candidate or a working pair and record incomplete steps. Rehearse discovery, installation, and use within the 15-minute budget.


## Handling upstream inconsistencies

The root overview and the Explorer catalog can change at different times. Keep catalog results and current source evidence distinguishable. Do not patch the official Explorer configuration or invent replacement commands during class. A failed link should lead to source checking, a recorded uncertainty, and a bounded follow-up.

If the installer fails but the catalog works, Exercise 1 can continue. For Exercise 2, use a working pair and record any incomplete installation or skill-use step. If the catalog fails, pair participants or use the README fallback. Report how the exercise was completed.

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
