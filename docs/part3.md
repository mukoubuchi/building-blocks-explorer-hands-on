# Optional challenge: install one skill

**Optional · 5–10 minutes after the workshop or for early finishers**

The two required exercises are complete without this challenge. Here you inspect and, if appropriate, install the `agent` skill for the assistant scenario from Exercise 1. Installing guidance does not deploy an agent, provision a product, or prove the solution works.

!!! note "Use a working, reviewed package"
    On September 10, 2026 the official generated `agent` archive downloaded successfully and contained `agent/SKILL.md`. Some other catalog download links returned 404. Recheck the live result before installing; if it fails, record the failure and stop this optional task.

## Step 1: Inspect before approving

In a new Explorer conversation, paste:

```text
For the fictional document-assistant scenario, use get_skill and
download_skill to inspect the agent skill. Show its purpose, official
download URL, prerequisites, and the workspace files it would add.
Do not install yet. Do not add modes, configure products, or deploy.
```

Read the description and confirm that the guidance is useful for your assistant scenario. The package must come from the official `ibm-self-serve-assets/building-blocks` repository. A download URL is not proof of a successful download.

## Step 2: Install only the selected skill

If the recommendation and scope are acceptable, send:

```text
Install only the agent skill from the reviewed official URL into this
workshop workspace. Do not install modes or other skills, configure
services, or deploy. Use the installer and report the verification result.
```

The expected folder is `.bob/skills/agent/`, with `SKILL.md` inside. Review the installer result and the file. Reload Bob afterward, as described by the official Explorer guide.

=== "macOS"

    In Finder, `Command` + `Shift` + `.` shows hidden folders if needed. You can also inspect the `.bob/skills/agent/SKILL.md` file in Bob's file tree.

=== "Windows"

    In File Explorer, use **View → Show → Hidden items** if needed. You can also inspect `.bob/skills/agent/SKILL.md` in Bob's file tree.

## Step 3: Record the difference

Write one sentence each about what Explorer did, what was installed, and what still requires engineering work. If the install failed, record the actual error and do not report success.

- [ ] I reviewed purpose, source, and installation scope before approving.
- [ ] I checked the installed file and result, or recorded why the optional task stopped.
- [ ] I understand that installing a skill is different from deploying a working application.

[Return to the review →](summary.md)
