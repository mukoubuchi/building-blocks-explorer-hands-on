# Open Building Blocks Explorer

**Time: 10 minutes · Elapsed: 20–30 minutes**

## Step 1: Download the official workspace

Download the [reviewed Explorer ZIP](https://raw.githubusercontent.com/ibm-self-serve-assets/building-blocks/f721f5ec1915225ade62d8d0e780fe6b19aa58b8/explore-BBs/building-blocks-explorer.zip). This link pins the official package reviewed for this workshop. The remote catalog is still live and can change. The [upstream Explorer guide](https://github.com/ibm-self-serve-assets/building-blocks/tree/main/explore-BBs) is the source for newer packages.

=== "macOS"

    In Finder, double-click the downloaded ZIP. Locate the extracted `building-blocks-explorer` folder. Finder normally hides its `.bob` subfolder; `Command` + `Shift` + `.` toggles hidden files if you need to inspect it.

=== "Windows"

    In File Explorer, right-click the ZIP and select **Extract All**. Open the extracted folder, not the compressed ZIP view. Extraction may create an extra outer folder: select the inner `building-blocks-explorer` folder containing `README.md` and `.bob`.

The workspace contains `.bob/custom_modes.yaml` and `.bob/mcp.json`. Use this fresh workshop workspace so experimental changes stay separate from customer work.

## Step 2: Open the folder in Bob

Use Bob's **Open Folder** action and select the extracted `building-blocks-explorer` folder. If prompted about workspace trust, review that it is the official package you downloaded and follow your organization's policy.

Choose **🧱 IBM Building Blocks Explorer** from the mode picker. If it is missing, check that you opened the folder containing `.bob`, then reload Bob. The exact location of the picker can vary with the Bob version.

## Step 3: Check the two connections

Open Bob's MCP server panel. Look for:

| Server | Role | What to check |
|---|---|---|
| `building-blocks` | Hosted catalog of blocks, skills, modes, and documentation | Connected; catalog tools are available |
| `building-blocks-installer` | Local helper run through uvx | Connected; first start may download Python and dependencies |

The official ZIP preconfigures these servers. No API key is requested for this discovery exercise. Individual product deployments may require credentials later.

Paste into Bob's chat:

```text
I am a beginner in Build Sales. Use the Building Blocks catalog tools
and show one available candidate for each of AI, Data, and Automation.
For each, include its name, the business problem it addresses, and a
source link. Keep the answer short. Do not install or deploy anything.
```

Check that the conversation shows catalog tool use, such as `list_building_blocks`, and includes source links. A fluent answer without a tool result does not confirm the connection. Open one link; if it is stale, use the [current overview](https://github.com/ibm-self-serve-assets/building-blocks) to locate the README and record the mismatch.

## Step 4: Prepare your notes

Use the worksheet provided by the instructor, or create `workshop-notes.md` in this workspace and copy the result headings from the exercises. Keep a separate section for each task. Saving locally does not send the file to the instructor.

## If something does not work

| Symptom | Next action |
|---|---|
| Explorer mode missing | Check the extracted inner folder and `.bob`; reload Bob |
| Installer cannot find uvx | Repeat the uv/uvx checks, then fully restart Bob |
| First local launch is slow | Allow the initial download; check the MCP error message if it stops |
| Catalog tools unavailable | Restart Bob once; have the instructor check access to the catalog URL in `.bob/mcp.json` |
| Catalog answer includes a dead link | Use the current upstream overview; retain the original answer and note the corrected source |
| Access is blocked by policy | Ask the instructor for the approved path; continue in a pair |

!!! note "A fallback is a different completion status"
    If only the installer is unavailable, continue the required catalog exercises and defer the optional installation. If the catalog is unavailable too, pair with a working participant. The instructor can lead a README-based exercise, but mark it as a source-reading fallback; Explorer operation has not been confirmed.

- [ ] I selected the Explorer mode in the correct folder.
- [ ] I received an answer backed by a catalog tool result, or recorded the fallback used.
- [ ] I can explain what each server does.

[Next: the two required exercises →](part2.md)
