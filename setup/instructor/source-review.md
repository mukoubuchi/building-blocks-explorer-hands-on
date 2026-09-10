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

`get_building_block` for `rag` returned metadata but `readme: null` with `README not found at expected path`. Its URL was `data/retrieval/RAG`; the independently fetched current README is under `data/pipelines/rag`.

The live `download_skill` results for `rag-pipeline-builder` and `infrastructure-as-code-terraform` returned URLs under earlier paths. HTTP GET requests to both returned 404. This verifies those two failures only, not that every installer asset is broken.

The official generated `agent` archive at the reviewed commit returned HTTP 200, passed ZIP CRC validation, and contained `agent/SKILL.md`. Download/archive validation does not establish successful installation inside Bob.

## Artifact identity

| Official artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| Explorer workspace ZIP | 14615 | `09d5e52deb6fabb6a4a272b81aed3027c7c1cbe77af476be1ab9e182aa518b47` |
| Generated agent skill ZIP | 633368 | `f9acd2a7491b41773761a3232a5097bcdb5e050cd6811920e77be66e63d10b31` |

The Explorer ZIP contains `README.md`, `.bob/custom_modes.yaml`, and `.bob/mcp.json` under `building-blocks-explorer/`. Its installer configuration pins a 0.1.2 wheel at commit `1ff4d793797f6b97d55cee67892d676c9159da66`. Workshop sources link to the official ZIP instead of embedding it.

## Exercise evidence

- [RAG README](https://github.com/ibm-self-serve-assets/building-blocks/blob/f721f5ec1915225ade62d8d0e780fe6b19aa58b8/data/pipelines/rag/README.md): custom/reference ingestion, retrieval, and generation; a separate managed OpenRAG recommendation; runnable assets have product/environment prerequisites.
- [Agent Builder README](https://github.com/ibm-self-serve-assets/building-blocks/blob/f721f5ec1915225ade62d8d0e780fe6b19aa58b8/ai/agents/agent-builder/README.md): watsonx Orchestrate ADK and agent-oriented modes/assets.
- [Secrets Management README](https://github.com/ibm-self-serve-assets/building-blocks/blob/f721f5ec1915225ade62d8d0e780fe6b19aa58b8/automation/secure/non-human-identity-and-secret-management/secrets-management/README.md): Vault-oriented secret detection, migration, and remediation material. Its parent README focuses on Security Verify; the workshop uses the child for Vault evidence.

## Design decisions

Teach the current overview first, and tell participants how to handle stale catalog links. Exercise 1 stops at research. Exercise 2 continues the same scenario by discovering a related skill or mode, reviewing prerequisites and workspace changes, installing a selected asset, and applying it to fictional product questions. No asset is prescribed; catalog availability and prerequisites must be checked at delivery time. Product deployment is excluded. Do not alter upstream modes or silently substitute unsupported commands.

The inherited site structure is retained. Product-specific Milvus services, credentials, and runtime scripts are omitted because this workshop does not run that application. Translation checks fail CI rather than automatically posting issue comments.

## Verification limits

- Official source retrieval and live catalog tool calls were checked independently.
- Windows command syntax was reviewed against the official uv guide; it has not been executed on a Windows machine in this preparation.
- Bob's actual GUI workflow, local helper startup, installation approval, and installed-skill activation have not been rehearsed on macOS or Windows.
- The 60-minute agenda is a planned facilitation budget, not a measured class duration.
- The initial release is a draft curriculum. Use the facilitator delivery record to close these gaps before class.

## Exercise 2 validation — September 10, 2026

The official Explorer README confirms workspace-local skill installation followed by a Bob reload. The non-human-identity-vault archive was fetched from the official main-branch skill-archives path with a User-Agent: 37,628 bytes, ZIP CRC validation passed. This is retrieval evidence only; no fixed skill is prescribed in the exercises. Instructors must rehearse selection of the most relevant BB, discovery of its associated skills or modes, installation, and actual use. Archive checks do not prove activation or completion within 15 minutes. A response that merely names an installed asset does not demonstrate use.
