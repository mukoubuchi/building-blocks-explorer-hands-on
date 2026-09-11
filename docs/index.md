# BB Recap

Find the Building Blocks that best match your interests with IBM Bob in this hands-on workshop.

## Before you start

- IBM Bob installed, signed in, and usable
- A macOS or Windows computer with internet access
- Permission to install uv during the workshop

## Agenda

| Minutes | Activity |
| --- | --- |
| 00–10 | BB Recap |
| 10–20 | [Install uv](preparation.md) |
| 20–30 | [Open Explorer](part1.md) |
| 30–45 | [Three exercises](part2.md) |
| 45–50 | [Summary](summary.md) |

## Building Blocks

Building Blocks (BB) provide reusable IBM reference implementations and engineering patterns.

Without BBs, you need to prepare the design and implementation separately. With BBs, existing architecture examples and code provide a starting point for trying product combinations and adapting them to your needs. This can reduce research and prototyping effort, leaving more time to validate business requirements.

| Area | Groups | Area README |
| --- | --- | --- |
| AI | Agents, AI Engineering, AI Trust | [AI README](https://github.com/ibm-self-serve-assets/building-blocks/blob/main/ai/README.md) |
| Data | Context, Pipelines, Query Engines | [Data README](https://github.com/ibm-self-serve-assets/building-blocks/blob/main/data/README.md) |
| Automation | Operate, Secure, Optimize | [Automation README](https://github.com/ibm-self-serve-assets/building-blocks/blob/main/automation/README.md) |

Reference: [Building Blocks root README](https://github.com/ibm-self-serve-assets/building-blocks/blob/main/README.md)

## Building Blocks Explorer

Explorer is a Bob mode for finding Building Blocks through natural-language questions. It searches the catalog and related documentation to help explore their uses and solution designs.

| Term | Relationship to Explorer | Files under `.bob` |
| --- | --- | --- |
| Catalog | The searchable collection of Building Blocks, related documentation, skills, and modes | Hosted externally; its connection is defined in `.bob/mcp.json` |
| Mode | Settings that adapt Bob to a type of work. Explorer is one such mode | `.bob/custom_modes.yaml` defines names, behavioral instructions, and other settings |
| Skill | Instructions and knowledge for a specific task. Explorer can find related skills | When installed, instructions reside in `.bob/skills/<skill-name>/SKILL.md`, sometimes alongside supporting files |

The official Explorer ZIP includes `.bob/custom_modes.yaml` and `.bob/mcp.json`. Skill files are added when a skill is installed.

## References

- Building Blocks: <https://github.com/ibm-self-serve-assets/building-blocks>
- Building Blocks documentation: <https://ibm-self-serve-assets.github.io/building-blocks-docs/>
- Explorer: <https://github.com/ibm-self-serve-assets/building-blocks/tree/main/explore-BBs>

[Next →](preparation.md){ .workshop-next }
