# Open Explorer

Time: 10 minutes (20–30)

## Step 1: Download and extract

Download the [official Explorer ZIP](https://raw.githubusercontent.com/ibm-self-serve-assets/building-blocks/f721f5ec1915225ade62d8d0e780fe6b19aa58b8/explore-BBs/building-blocks-explorer.zip).

=== "macOS"

    Double-click the ZIP in Finder to extract it.

=== "Windows"

    Right-click the ZIP → **Extract All**. Use the extracted folder, not the ZIP view.

## Step 2: Select the mode in Bob

Use **Open Folder** to open `building-blocks-explorer`, containing `README.md` and `.bob`. Choose **🧱 IBM Building Blocks Explorer** from the mode picker.

## Step 3: Check the connection

Check these servers in Bob's MCP panel:

| Server | Role |
| --- | --- |
| `building-blocks` | Searches the remote catalog |
| `building-blocks-installer` | Runs the local installer through uvx |

Paste into Bob's chat:

```text
Use the Building Blocks catalog tools to show one candidate each for AI, Data, and Automation.
Briefly give its name, purpose, and source URL.
Research only. Installation and deployment are out of scope.
```

Explorer can also perform installation actions, so limit this connection check to research.

Confirm a catalog tool result (such as `list_building_blocks`) and open a source link.

??? tip "Troubleshooting"
    | Symptom | Action |
    | --- | --- |
    | Mode missing | Check the extracted folder contains `.bob`; reload Bob |
    | Installer unavailable | Check uv/uvx and fully restart Bob; the catalog exercises can continue if the catalog works |
    | First start is slow | Wait for the initial dependency download |
    | Catalog unavailable | Restart Bob once; if still blocked, ask the instructor and work in a pair |
    | Source link is stale | Find the README from the [Building Blocks overview](https://github.com/ibm-self-serve-assets/building-blocks) and record the corrected URL or mark it unverified |

    If using READMEs without a working Explorer, record this as a source-reading fallback.

Reference: [official Explorer guide](https://github.com/ibm-self-serve-assets/building-blocks/tree/main/explore-BBs)

[Next →](part2.md){ .workshop-next }
