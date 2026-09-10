# Install uv

**Time: 10 minutes · Elapsed: 10–20 minutes**

uv manages Python tools; `uvx` runs a tool in an isolated environment. Explorer's local installer uses uvx. Follow only the tab for your operating system. These commands belong in a terminal, not in Bob's chat box.

## Step 1: Open a terminal

=== "macOS"

    Open **Terminal** from Applications → Utilities, or use Spotlight to search for Terminal. The default shell is usually zsh.

=== "Windows"

    Open **PowerShell** from the Start menu or choose the PowerShell profile in Windows Terminal. Do not use Command Prompt for the PowerShell commands below.

## Step 2: Install uv

If `uv --version` and `uvx --version` already work, skip to Step 3. Otherwise run the command for your OS. Use your organization's approved installation method if these commands are restricted.

=== "macOS"

    ```bash
    curl -LsSf -A "BuildingBlocksWorkshop/0.1" https://astral.sh/uv/install.sh | sh
    ```

    This is the official standalone installer, with a User-Agent added to the download. If you already use Homebrew, `brew install uv` is an alternative; do not install both ways.

=== "Windows"

    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 -UserAgent 'BuildingBlocksWorkshop/0.1' | iex"
    ```

    This is the official standalone installer, with a User-Agent added. The command applies the execution policy to this process. If your organization restricts script execution, use an approved method, such as `winget install --id=astral-sh.uv -e` where available. Do not change machine-wide policy.

Source: [uv installation documentation](https://docs.astral.sh/uv/getting-started/installation/). You can inspect the installer before running it by opening [install.sh](https://astral.sh/uv/install.sh) or [install.ps1](https://astral.sh/uv/install.ps1) in your browser.

## Step 3: Reopen the terminal and check

Close the terminal and open a new one. Run both commands on either OS:

```text
uv --version
uvx --version
```

Each should print a version number, such as `uv 0.x.y` or `uvx 0.x.y`; the exact number may differ. Save any unsaved work, fully quit Bob, and reopen it so its processes pick up the updated PATH.

## If a command is not found

=== "macOS"

    Check the default standalone installation directly:

    ```bash
    "$HOME/.local/bin/uv" --version
    "$HOME/.local/bin/uvx" --version
    ```

=== "Windows"

    Check the default standalone installation directly:

    ```powershell
    & "$env:USERPROFILE\.local\bin\uv.exe" --version
    & "$env:USERPROFILE\.local\bin\uvx.exe" --version
    ```

If the direct path works but the short command does not, follow the installer's PATH guidance and restart the terminal and Bob. A custom or package-manager installation can use a different location. Share the error with the instructor if neither check works.

!!! tip "Keep moving at minute 20"
    If installation is blocked by network or device policy, pair with someone whose setup works and continue the exercises. Note the blocker for follow-up; do not spend the rest of the workshop changing security settings.

- [ ] Both version commands print a result, or I have joined a working pair.
- [ ] Bob has been restarted after installation.

[Next: open Explorer →](part1.md)
