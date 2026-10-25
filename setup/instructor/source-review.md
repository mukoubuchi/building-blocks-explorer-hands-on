# Source review

Reviewed on September 10, 2026. This file separates upstream observations from workshop design decisions and from verification still required.

## Sources

| Purpose | Source | Review scope |
| --- | --- | --- |
| Layout and repository conventions | [vector-search-hands-on at 7776c62](https://github.com/mukoubuchi/vector-search-hands-on/tree/7776c6227da1c006f8107790003855dd5b23fa8f) | MkDocs, modular UI assets, instructor/participant layout, translation checker, CI, release packaging |
| Current portfolio | [Building Blocks at f721f5e](https://github.com/ibm-self-serve-assets/building-blocks/tree/f721f5ec1915225ade62d8d0e780fe6b19aa58b8) | Main-branch head returned by the GitHub API; commit dated September 9, 2026 |
| Explorer setup | [Explorer README](https://github.com/ibm-self-serve-assets/building-blocks/blob/f721f5ec1915225ade62d8d0e780fe6b19aa58b8/explore-BBs/README.md) and official ZIP at that commit | Download, open workspace, select mode, remote catalog, local uvx helper |
| uv | [Official installation guide](https://docs.astral.sh/uv/getting-started/installation/) | macOS and Windows standalone commands, Homebrew/WinGet alternatives |
| Pages visibility | [GitHub access control](https://docs.github.com/en/enterprise-cloud%40latest/pages/getting-started-with-github-pages/changing-the-visibility-of-your-github-pages-site) | Source privacy and site privacy are separate |

HTTP downloads used a User-Agent and checked status and nontrivial response size. ZIP CRC checks passed. The repository tree API reported `truncated: false`; no portfolio total is inferred from the overview prose or displayed in the lessons.

## Observations from independent paths

The current GitHub root README groups the portfolio under AI, Data, and Automation with newer subgroups and paths. Separately, direct requests to the hosted MCP endpoint configured in the official ZIP succeeded for initialization, tool listing, block listing, and a Terraform skill query. The returned catalog still used earlier group names and paths. This was observed from the live service, not inferred from the local snapshot.

Rechecked on October 9, 2026 at [`5c61097`](https://github.com/ibm-self-serve-assets/building-blocks/tree/5c610971dc72f9e9035821b3cb2c3edea868f8b4): the root README groups the portfolio under AI Control Plane (Agents, Control, Engineering), Automation (Operate, Secure, Optimize), and Streamhouse (Real-Time, Pipelines, Lakehouse). At `f721f5e` the areas were AI (Agents, AI Engineering, AI Trust), Data (Context, Pipelines, Query Engines), and Automation. Commit [`163597c`](https://github.com/ibm-self-serve-assets/building-blocks/commit/163597c04eb56c45eaf1ce8ec844f8ebf12f6ecd) (September 30, 2026) restructured AI as the AI Control Plane, and commit [`257f055`](https://github.com/ibm-self-serve-assets/building-blocks/commit/257f0556f3d14240d5f0a1ecc5a26c33a5b4a642) (October 7, 2026) renamed Data to Streamhouse in the root README and moved `data/pipelines/text2sql/` to `streamhouse/pipelines/text2sql/`. `data/README.md` on the main branch returns 404; the root README links `streamhouse/README.md` instead. The recap table in the lessons follows `5c61097` and links to that commit. The Part 1 prompt still names AI, Data, and Automation for the catalog tools; the names the live catalog uses now were not rechecked.

`get_building_block` for `rag` returned metadata but `readme: null` with `README not found at expected path`. Its URL was `data/retrieval/RAG`; the independently fetched current README is under `data/pipelines/rag`.

The live `download_skill` results for `rag-pipeline-builder` and `infrastructure-as-code-terraform` returned URLs under earlier paths. HTTP GET requests to both returned 404. This verifies those two failures only, not that every installer asset is broken.

The official generated `agent` archive at the reviewed commit returned HTTP 200, passed ZIP CRC validation, and contained `agent/SKILL.md`. Download/archive validation does not establish successful installation inside Bob.

## Artifact identity

| Official artifact | <div align="center">Bytes</div> | SHA-256 |
| --- | ---: | --- |
| Explorer workspace ZIP | 14615 | `09d5e52deb6fabb6a4a272b81aed3027c7c1cbe77af476be1ab9e182aa518b47` |
| Generated agent skill ZIP | 633368 | `f9acd2a7491b41773761a3232a5097bcdb5e050cd6811920e77be66e63d10b31` |

The Explorer ZIP contains `README.md`, `.bob/custom_modes.yaml`, and `.bob/mcp.json` under `building-blocks-explorer/`. Its installer configuration pins a 0.1.2 wheel at commit `1ff4d793797f6b97d55cee67892d676c9159da66`. Workshop sources link to the official ZIP instead of embedding it.

## Exercise evidence

- [RAG README](https://github.com/ibm-self-serve-assets/building-blocks/blob/f721f5ec1915225ade62d8d0e780fe6b19aa58b8/data/pipelines/rag/README.md): custom/reference ingestion, retrieval, and generation; a separate managed OpenRAG recommendation; runnable assets have product/environment prerequisites.
- [Agent Builder README](https://github.com/ibm-self-serve-assets/building-blocks/blob/f721f5ec1915225ade62d8d0e780fe6b19aa58b8/ai/agents/agent-builder/README.md): watsonx Orchestrate ADK and agent-oriented modes/assets.
- [Secrets Management README](https://github.com/ibm-self-serve-assets/building-blocks/blob/f721f5ec1915225ade62d8d0e780fe6b19aa58b8/automation/secure/non-human-identity-and-secret-management/secrets-management/README.md): Vault-oriented secret detection, migration, and remediation material. Its parent README focuses on Security Verify; the workshop uses the child for Vault evidence.

## Design decisions

Teach the current overview first and explain how to handle stale catalog links. The three exercises use short questions without prescribed output formatting or file recording. The exercises are independent questions about data streaming, access/secrets management, and document search, adapted from the official Explorer guide. Bob produces each answer. Installation, configuration changes, and deployment are excluded. Do not alter upstream modes or silently substitute unsupported commands.

The inherited site structure is retained. Product-specific Milvus services, credentials, and runtime scripts are omitted because this workshop does not run that application. Translation checks fail CI rather than automatically posting issue comments.

On October 25, 2026, uv left the workshop flow: the exercises use only the hosted catalog, and the local installer, the only part that needs uv, fails to start (upstream #262; re-checked that day with the same ImportError). The Install uv page and its header tab stay for a planned revision that checks and uses installed Building Blocks once the bug is fixed. The same day, three additional exercises for the installer (install a skill, install a mode, draw a diagram) were added to the Exercises page, marked as requiring uv and blocked by #262; they have not been run with Bob.

## Verification limits

- Official source retrieval and live catalog tool calls were checked independently.
- Windows command syntax was reviewed against the official uv guide; it has not been executed on a Windows machine in this preparation.
- Bob's actual GUI workflow, local helper startup, installation approval, and installed-skill activation have not been rehearsed on macOS or Windows.
- The 35-minute agenda is a planned facilitation budget, not a measured class duration.
- The initial release is a draft curriculum. Use the facilitator delivery record to close these gaps before class.

## Historical asset validation — September 10, 2026

The official Explorer README confirms workspace-local skill installation followed by a Bob reload. The non-human-identity-vault archive was fetched from the official main-branch skill-archives path with a User-Agent: 37,628 bytes, ZIP CRC validation passed. This is retrieval evidence only; no fixed skill is prescribed in the exercises. Instructors must rehearse the revised research-only exercises. Archive checks do not validate the proposed answer behavior or completion within the five-minute exercise budgets.
