# Open Explorer

Time: 10 minutes (15–25)

## Step 1: Download and extract

Download the [official Explorer ZIP](https://raw.githubusercontent.com/ibm-self-serve-assets/building-blocks/f721f5ec1915225ade62d8d0e780fe6b19aa58b8/explore-BBs/building-blocks-explorer.zip).

=== "macOS"

    Double-click the ZIP in Finder to extract it.

=== "Windows"

    Right-click the ZIP → **Extract All**. Use the extracted folder, not the ZIP view.

## Step 2: Select the mode in Bob

1. Launch IBM Bob.
1. Open the `building-blocks-explorer` folder, which contains `README.md` and `.bob`.

    === "macOS"

        Select <kbd>File</kbd> → <kbd>Open...</kbd> and choose the `building-blocks-explorer` folder, or press <kbd>⌘</kbd> + <kbd>O</kbd>.

    === "Windows"

        Select <kbd>File</kbd> → <kbd>Open Folder...</kbd> and choose the `building-blocks-explorer` folder.

1. If a Restricted Mode banner appears, select **Manage** in the banner, then **Trust**, and close the trust editor.
1. In the IBM Bob panel, open the mode picker below the chat input and choose **🧱 IBM Building Blocks Explorer**.

## Step 3: Check the connection

Select the small gear icon (Settings) at the top right of the IBM Bob panel. It is not the gear at the bottom left of the window (Manage). **Bob Settings** at the bottom right of the window opens the same settings. In the settings that open, select **MCP** in the list on the left, and check these servers:

| Server | Role |
| --- | --- |
| `building-blocks` | Searches the remote catalog |
| `building-blocks-installer` | Runs the local installer through uvx |

!!! warning "Installer bug"
    `building-blocks-installer` does not start because of an upstream bug ([#262](https://github.com/ibm-self-serve-assets/building-blocks/issues/262)), and the MCP screen shows it as **Disconnected**. [Exercises 1–3](part2.md) use only the catalog, so continue. The [additional exercises](part2.md#extra) need the installer.

Paste into Bob's chat:

```text
Use the Building Blocks catalog tools to show one candidate each for AI Control Plane (formerly AI), Data, and Automation.
Briefly give its name, purpose, and source URL.
Research only. Installation is out of scope.
```

Bob asks to approve each catalog tool call, such as `List Building Blocks (building-blocks)`. Select **Approve once**.

Explorer can also perform installation actions, so limit this connection check to research.

Confirm a catalog tool result (such as `list_building_blocks`) and open a source link.

??? tip "Troubleshooting"
    | Symptom | Action |
    | --- | --- |
    | Mode missing | Check the extracted folder contains `.bob`; reload Bob |
    | Installer unavailable | Check uv/uvx and fully restart Bob; [exercises 1–3](part2.md) can continue if the catalog works |
    | First start is slow | Wait for the initial dependency download |
    | Catalog unavailable | Restart Bob once; if still blocked, ask the instructor and follow the instructor's shared screen |
    | Source link is stale | Find the README from the [Building Blocks overview](https://github.com/ibm-self-serve-assets/building-blocks/tree/031ceebaed354fddab43b5ff4ef53bff0ed9ffc5) and record the corrected URL or mark it unverified |

    If using READMEs without a working Explorer, record this as a source-reading fallback.

Reference: [official Explorer guide](https://github.com/ibm-self-serve-assets/building-blocks/tree/f721f5ec1915225ade62d8d0e780fe6b19aa58b8/explore-BBs)

[Next →](part2.md){ .workshop-next }
