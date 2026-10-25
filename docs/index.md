# Introduction

## Overview

- **Objective**: Understand how to find the Building Blocks that match a business need, with their sources, through questions in plain language with IBM Bob and the Building Blocks Explorer mode.
- **Audience**: Beginners. IBM Bob must be installed, signed in, and usable.
- **Learning outcomes**:
    - The structure of the Building Blocks: areas, groups, and their READMEs
    - The relation of the catalog, modes, and skills to Explorer
    - How Explorer searches the catalog through MCP and returns candidates with their sources
- **Exercises**:
    - [Open Explorer](part1.md): extract the official Explorer ZIP, select the mode in Bob, and confirm the connection to the catalog.
    - [Exercises](part2.md): enter three questions (data streaming, access and secrets management, document search) and review the answers.
- **Time**: 35 minutes
- **Environment**: Bob runs on each participant's computer, and the catalog is a remote service reached over the internet. No cloud API key is used.

## Scenario

Consider someone planning a solution who wants to know whether IBM already offers reference implementations for a need such as real-time data streaming or secrets management. The Building Blocks span three areas and nine groups, and each area has its own README. In this workshop, they ask IBM Bob with the Building Blocks Explorer mode in plain language, and Explorer searches the catalog and returns candidates with their sources. Starting from these candidates, they can try product combinations from existing examples and code instead of preparing the design and implementation separately.

## Before you start

- IBM Bob installed, signed in, and usable
- A macOS or Windows computer with internet access

## Agenda

| Minutes | Activity |
| ---: | --- |
| 0–5 | [Introduction](index.md) |
| 5–15 | [Open Explorer](part1.md) |
| 15–30 | [Three exercises](part2.md) |
| 30–35 | [Summary](summary.md) |

## Building Blocks

Building Blocks provide reusable IBM reference implementations and engineering patterns.

Without Building Blocks, you need to prepare the design and implementation separately. With Building Blocks, existing architecture examples and code provide a starting point for trying product combinations and adapting them to your needs. This can reduce research and prototyping effort, leaving more time to validate business requirements.

| Area | Groups | Area README |
| --- | --- | --- |
| AI Control Plane | Agents, Control, Engineering | [AI Control Plane README](https://github.com/ibm-self-serve-assets/building-blocks/blob/5c610971dc72f9e9035821b3cb2c3edea868f8b4/ai/README.md) |
| Streamhouse | Real-Time, Pipelines, Lakehouse | [Streamhouse README](https://github.com/ibm-self-serve-assets/building-blocks/blob/5c610971dc72f9e9035821b3cb2c3edea868f8b4/streamhouse/README.md) |
| Automation | Operate, Secure, Optimize | [Automation README](https://github.com/ibm-self-serve-assets/building-blocks/blob/5c610971dc72f9e9035821b3cb2c3edea868f8b4/automation/README.md) |

Reference: [Building Blocks root README](https://github.com/ibm-self-serve-assets/building-blocks/blob/5c610971dc72f9e9035821b3cb2c3edea868f8b4/README.md)

## Building Blocks Explorer

Explorer is a Bob mode for finding Building Blocks through natural-language questions. It searches the catalog and related documentation to help explore their uses and solution designs.

| Term | Relationship to Explorer | Files under `.bob` |
| --- | --- | --- |
| Catalog | The searchable collection of Building Blocks, related documentation, skills, and modes | Hosted externally; its connection is defined in `.bob/mcp.json` |
| Mode | Settings that adapt Bob to a type of work. Explorer is one such mode | `.bob/custom_modes.yaml` defines names, behavioral instructions, and other settings |
| Skill | Instructions and knowledge for a specific task. Explorer can find related skills | When installed, instructions reside in `.bob/skills/<skill-name>/SKILL.md`, sometimes alongside supporting files |

The official Explorer ZIP includes `.bob/custom_modes.yaml` and `.bob/mcp.json`. Skill files are added when a skill is installed.

??? info "Differences from the official Building Block"
    The Explorer mode and its connection settings come from the official Explorer ZIP (as of September 9, 2026) as they are. This workshop does not hand out a ZIP; participants download the official one. The text you paste into Bob was written for this workshop.

    - **[Connection check](part1.md#step-3-check-the-connection)**: it says "Research only. Installation and deployment are out of scope." because Explorer can also install.
    - **[The three exercise questions](part2.md)**: short questions based on the three examples in the official Explorer guide (real-time data streaming, access management and secrets, and an in-store assistant that answers from documents).

## References

- Building Blocks: <https://github.com/ibm-self-serve-assets/building-blocks/tree/5c610971dc72f9e9035821b3cb2c3edea868f8b4>
- Building Blocks documentation: <https://ibm-self-serve-assets.github.io/building-blocks-docs/>
- Explorer: <https://github.com/ibm-self-serve-assets/building-blocks/tree/f721f5ec1915225ade62d8d0e780fe6b19aa58b8/explore-BBs>

[Next →](part1.md){ .workshop-next }
