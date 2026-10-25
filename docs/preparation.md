# Install uv

Time: 5 minutes (5–10)

Explorer's local installer uses `uvx`, included with [uv](https://docs.astral.sh/uv/). A separate Python installation is not required.

## Step 1: Open a terminal

=== "macOS"

    Open Applications → Utilities → Terminal.

=== "Windows"

    Open PowerShell from the Start menu.

## Step 2: Install uv

If `uv --version` and `uvx --version` already work, go to [Step 3](#step-3-check-the-installation). Otherwise run the command for your OS in the terminal.

=== "macOS"

    ```bash
    curl -LsSf -A "BuildingBlocksWorkshop/0.1" https://astral.sh/uv/install.sh | sh
    ```

=== "Windows"

    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 -UserAgent 'BuildingBlocksWorkshop/0.1' | iex"
    ```

Use an organization-approved method if script execution is restricted. See the [official installation guide](https://docs.astral.sh/uv/getting-started/installation/) for alternatives.

## Step 3: Check the installation

Reopen the terminal and run:

```bash
uv --version
uvx --version
```

Both commands should print a version number. Save your work, fully quit Bob, and reopen it to load the updated PATH.

??? tip "Command not found"
    Check the standalone installer's default location:

    === "macOS"

        ```bash
        "$HOME/.local/bin/uv" --version
        "$HOME/.local/bin/uvx" --version
        ```

    === "Windows"

        ```powershell
        & "$env:USERPROFILE\.local\bin\uv.exe" --version
        & "$env:USERPROFILE\.local\bin\uvx.exe" --version
        ```

    If these work, follow the installer's PATH instructions. If setup remains blocked, ask the instructor and continue in a working pair.

[Next →](part1.md){ .workshop-next }
