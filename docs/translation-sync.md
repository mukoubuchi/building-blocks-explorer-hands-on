# Translation synchronization

Update English and Japanese participant pages together. A pair is `docs/<page>.md` and `docs/ja/<page>.md`.

CI checks both directions on pull requests and pushes. `lib/check_translation_sync.sh` follows the conventions inherited from `vector-search-hands-on`; it detects missing changed counterparts, not semantic equivalence. `lib/validate_docs.py` also checks page pair completeness on every build.

An intentional one-language correction may use the `translation-sync-skip` PR label and `[skip translation-sync]` in the merge commit. Explain why the counterpart does not need a change. Maintainer-only files `readme.md` and `translation-sync.md` are excluded from publication and do not need translated copies.

Preserve timing, prompts, expected results, troubleshooting, source links, and installation restrictions across languages. Review all of these before release.
