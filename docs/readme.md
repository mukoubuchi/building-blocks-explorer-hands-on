# Documentation maintenance

English participant pages live directly under `docs/`; Japanese counterparts live under `docs/ja/`. Keep the five page names aligned with `mkdocs.yml` and `docs/javascripts/site-config.js`.

The CSS and JavaScript modules were inherited from `vector-search-hands-on` at commit `7776c6227da1c006f8107790003855dd5b23fa8f`, and its UI and search changes were synced at commit `6ca899a258f3937783929575c930e35f2ac36767`. Parts for its Part 3, feedback form, flow diagram, Python code, and SVG diagrams are not carried over. `extra.css` imports the typography, navigation, code, components and language-switcher modules. Use Material theme variables for extensions. The JavaScript namespace is `BuildingBlocksHandsOn`. `search.js` relies on internals of Material 9.7.6 (the result count and the search highlights); recheck it whenever `mkdocs-material` in `setup/instructor/requirements.txt` changes.

Use `Step N:` / `ステップ N:` headings for the numbered rail. Use matching `macOS` and `Windows` tab labels across pages so selection stays linked. English is the default language; Japanese uses `/ja/`. No remote fonts or analytics are configured.

For build commands, see the root README. Run the strict MkDocs build and `lib/validate_docs.py`, then inspect both languages at desktop and mobile sizes. Check language links under the actual GitHub Pages project prefix, not only at `/`.

Japanese prose uses full-width parentheses, half-width colons followed by a space, and half-width spaces between Japanese and Latin text (including across inline code and link boundaries). Put spaces around arrows. Follow the source workshop's OS tabs, numbered step rails, modular assets, and bilingual layout. Keep lessons focused on actions, prompts, and completion checks. Markdown delimiters must render correctly with a CommonMark parser; punctuation stays outside bold delimiters. Code and URL syntax are exempt.
