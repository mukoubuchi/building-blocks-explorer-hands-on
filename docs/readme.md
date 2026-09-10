# Documentation maintenance

English participant pages live directly under `docs/`; Japanese counterparts live under `docs/ja/`. Keep the seven page names aligned with `mkdocs.yml` and `docs/javascripts/site-config.js`.

The CSS and JavaScript modules were inherited from `vector-search-hands-on` at commit `7776c6227da1c006f8107790003855dd5b23fa8f`. `extra.css` imports the typography, navigation, code, components, feedback, and language-switcher modules. Use Material theme variables for extensions. The JavaScript namespace is `BuildingBlocksHandsOn`.

Use `Step N:` / `ステップ N:` headings for the numbered rail. Use matching `macOS` and `Windows` tab labels across pages so selection stays linked. English is the default language; Japanese uses `/ja/`. No remote fonts or analytics are configured. Feedback only composes text locally; the participant chooses whether and where to submit it.

For build commands, see the root README. Run the strict MkDocs build and `lib/validate_docs.py`, then inspect both languages at desktop and mobile sizes. Check language links under the actual GitHub Pages project prefix, not only at `/`.

Japanese prose uses full-width parentheses and spaces between Japanese and Latin text. Markdown delimiters must render correctly with a CommonMark parser; punctuation stays outside bold delimiters. Code and URL syntax are exempt.
