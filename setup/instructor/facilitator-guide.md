# Facilitator guide

## Audience and outcome

This is a 40-minute beginner workshop delivered in English or Japanese. Bob is already installed and usable. The goal is independent catalog questions and sourced answers, without installation or deployment. Complete three exercises.

## Before delivery

1. Read `source-review.md`. Check the current Building Blocks overview, the official Explorer ZIP, and the live catalog on the network participants will use.

1. Rehearse the exact participant instructions in Bob on at least one macOS and one Windows machine. Record OS, Bob, uv/uvx versions, date, connection results, and time to the first catalog-backed response. Static documentation checks are not a substitute for this rehearsal.

1. Verify both catalog and installer connections, then run the three prompts and review their sources. Check whether the known catalog path issues are still present.

1. Confirm attendees can sign in to Bob, download from GitHub/raw.githubusercontent.com, install uv, and reach the Code Engine catalog endpoint. The local helper may need Python/package downloads from the normal uv package sources. Use the organization's approved access process.

1. Provide an accessible workshop URL or a reviewed local/site export through an approved channel; do not assume private repository access for all participants.

1. Prepare to share your screen for participants who get blocked, and the README entry points in `source-review.md`. If the live catalog is unavailable, a source-reading exercise remains useful but must be recorded as a fallback, not a completed Explorer test.

## Run of show

| <div align="center">Clock</div> | Action | Stop rule |
| ---: | --- | --- |
| 0–5 | Recap AI, Data, Automation; distinguish block, mode, skill, Explorer | Avoid enumerating every block or promising ROI |
| 5–10 | Install uv in OS tabs; confirm uv and uvx; restart Bob | At minute 10 blocked participants follow the instructor's shared screen |
| 10–20 | Open ZIP workspace, trust the folder, select Explorer, check two MCP connections | Confirm an actual catalog tool result |
| 20–35 | Exercises 1–3: ask about data streaming, access and secrets management, and document search | At minute 35 retain the answers and sources |
| 35–40 | Review completion and save results | Review the three answers |

## Exercise coaching

Each exercise is one independent question. Participants paste the provided prompt; Bob generates the answer. The participant prompts currently contain only the questions; they do not prescribe an output format or Markdown recording. Do not add a fictional scenario, comparison, follow-up sequence, or manual output-writing task. The questions adapt the streaming and access/secrets topics from the official Explorer guide, restricting discovery to Building Blocks. Skills and modes are not exercise activities. No installation, configuration changes, or deployment is performed.

Accept different catalog results when backed by sources. Bob does not check the sources it cites: in the run on October 10, 2026, the GitHub links for blocks under `data/` returned 404, because the catalog still returns paths that upstream moved to `streamhouse/`. Have participants open a cited source to check it, and use the documentation link or the Building Blocks overview when a link fails. Rehearse the three questions within their shared 15-minute budget.

## Handling upstream inconsistencies

The root overview and the Explorer catalog can change at different times. Keep catalog results and current source evidence distinguishable. Do not patch the official Explorer configuration or invent replacement commands during class. A failed link should lead to source checking, a recorded uncertainty, and a bounded follow-up.

If the installer fails but the catalog works, all three exercises can continue. If the catalog fails, participants follow the instructor's shared screen or use the README fallback. Report how the exercise was completed.

## Completion

Check for understanding rather than identical output: each answer addresses the question and names its sources, and the participant has opened one of them to check it.

## Delivery record

Fill these fields before presenting this material as rehearsed:

- Date and workshop release:
- macOS / Bob / uv / uvx versions and result:
- Windows / Bob / uv / uvx versions and result:
- Remote catalog and local installer result:
- Actual time to finish each required exercise:
- Known issues and fallback used:

The initial v0.1.0 draft has documentation and service-level checks; an interactive Bob rehearsal on both operating systems remains required.
