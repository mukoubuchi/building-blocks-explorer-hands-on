# Building Blocks Explorer Hands-on

A **60-minute workshop for beginner Build Sales participants**, available in English and Japanese. Use IBM Bob and the Building Blocks Explorer to turn a fictional business need into a sourced recommendation and an engineering handoff.

IBM Bob must already be installed and usable. Participants install **uv during the session**; no separate Python, Git, Node.js, Docker, cloud account, or product deployment is required for the core exercises.

## Workshop flow

| Time | Activity | Result |
|---|---|---|
| 00–10 | Current Building Blocks recap | Explain the roles of Building Blocks, Explorer, Bob modes, and skills |
| 10–20 | Install uv on macOS or Windows | `uv --version` and `uvx --version` succeed |
| 20–30 | Open the official Explorer workspace | Query the catalog from Bob |
| 30–42 | Exercise 1: document-based assistant | Two candidate blocks, evidence, and a business pitch |
| 42–55 | Exercise 2: secrets-management discovery | A short engineering handoff with open questions |
| 55–60 | Review and feedback | Explain the next customer conversation |

A third, optional skill-installation challenge takes 5–10 additional minutes. Keep it outside the core hour unless a participant finishes early; completing the first two exercises is sufficient.

## Materials

| Audience | English | Japanese |
|---|---|---|
| Participants | [Start the workshop](docs/index.md) | [教材を開く](docs/ja/index.md) |
| Participants | [Worksheet](setup/participant/en/worksheet.md) | [ワークシート](setup/participant/ja/worksheet.md) |
| Instructors | [Facilitator guide](setup/instructor/facilitator-guide.md) | The English guide supports either delivery language |
| Maintainers | [Source review](setup/instructor/source-review.md) | [Translation rules](docs/translation-sync.md) |

The official Explorer ZIP is downloaded directly from the upstream repository. Workshop ZIPs contain only the localized worksheet and participant README; they do not redistribute Bob modes or credentials.

## Repository structure

This repository follows [vector-search-hands-on](https://github.com/mukoubuchi/vector-search-hands-on): Material for MkDocs, English at `docs/`, Japanese at `docs/ja/`, modular CSS/JavaScript, instructor/participant separation, translation checks, and release ZIP assets.

```text
.github/workflows/       # CI, translation checks, Pages, and releases
lib/                     # Shared validation helpers
setup/instructor/        # Facilitation, sources, build and package tools
setup/participant/en/    # English participant package
setup/participant/ja/    # Japanese participant package
docs/                    # English teaching pages and shared UI assets
docs/ja/                 # Japanese teaching pages
mkdocs.yml               # Bilingual navigation and site configuration
```

The inherited layout includes language switching, search, linked OS tabs, numbered step rails, code-copy buttons, persistent checklists, and feedback message composition. Existing Milvus runtime services are not part of this Explorer workshop.

## Build and preview

Run these commands from the repository root after installing [uv](https://docs.astral.sh/uv/getting-started/installation/).

### macOS

```bash
uv venv
uv pip install --python .venv/bin/python -r setup/instructor/requirements.txt
.venv/bin/mkdocs build --strict
.venv/bin/python lib/validate_docs.py
.venv/bin/mkdocs serve --dev-addr 127.0.0.1:8000
```

### Windows PowerShell

```powershell
uv venv
uv pip install --python .venv/Scripts/python.exe -r setup/instructor/requirements.txt
.venv/Scripts/mkdocs.exe build --strict
.venv/Scripts/python.exe lib/validate_docs.py
.venv/Scripts/mkdocs.exe serve --dev-addr 127.0.0.1:8000
```

Open `http://127.0.0.1:8000/` or `http://127.0.0.1:8000/ja/`. The preview binds only to the local machine.

## Distribution and Pages visibility

The source repository is **private on github.com**. Private repositories do not automatically create private Pages sites. Pages deployment is disabled until the owner approves its audience and sets the repository variable `PAGES_ENABLED` to `true`; the workflow can then be dispatched. On personal accounts, Pages is public and a plan supporting Pages from private repositories is required. See [GitHub Pages access control](https://docs.github.com/en/enterprise-cloud%40latest/pages/getting-started-with-github-pages/changing-the-visibility-of-your-github-pages-site).

Private release assets also require repository access. Instructors distribute the localized worksheet ZIP through an approved channel to participants without repository access. Until Pages is approved, use the local preview or provide a site export through an approved channel. Do not change the repository to public to make Pages work.

## Maintenance conventions

- Keep this README, maintainer documentation, code comments, filenames, commit messages, and release notes in English. Japanese teaching content is intentional.
- Update corresponding English and Japanese teaching files in the same change. CI checks changed pairs; it does not certify translation meaning.
- Use Conventional Commits and explicit paths for staging. Review staged filenames and content before committing.
- Keep local tool configuration, credentials, conversation logs, and generated files out of Git.
- Review the current upstream sources and run the instructor preflight before each workshop. The recap is checked against upstream commit `f721f5ec1915225ade62d8d0e780fe6b19aa58b8` dated September 9, 2026; catalog results remain dynamic.
- Use system fonts, existing Material CSS variables, and the inherited modular UI. Keep participant flows free of maintainer setup details.
- Before a release, run CI, review both languages and OS tabs in a headless browser, and rehearse the actual Bob flow on macOS and Windows. Documentation build success is not a Bob runtime test.
- Consider an annotated semantic-version tag for every pushed change. Reader-visible teaching changes warrant a release; release notes summarize behavior and materials, not a list of commits.

Build localized ZIPs with `python setup/instructor/build_participant_zips.py`. The release workflow attaches the two packages to an existing release; create it as a draft before pushing its annotated tag, then publish it after the workflow succeeds. Initial version `v0.1.0` is a teaching draft pending a facilitated rehearsal.

## License

[Apache License 2.0](LICENSE). Shared site assets are adapted from `vector-search-hands-on` under the same license. Vendored Mermaid retains its upstream license notice.
