# Exercises

Time: 25 minutes (30–55)

Use a fictional document assistant to explore candidates, then discover and use a related skill or mode.

Exercise 1 covers research and recording results; Exercise 2 adds, configures, and uses a skill or mode. Product deployment is out of scope.

## Exercise 1: find all related Building Blocks {#exercise-1}

10 minutes

### Step 1: Find candidates

Start a new conversation and paste:

```text
A fictional retailer needs an assistant that answers employees' product and policy questions from approved documents.
It must cite sources and say when an answer cannot be found.

Search the entire catalog for all Building Blocks related to this scenario.
Do not limit the number of results; retrieve any remaining result pages and remove duplicates.
List each BB with its purpose, relevance to the scenario, and source URL.
State the search coverage and any unchecked areas.

Ask at most two clarifying questions, one at a time.
Research only. Installation and deployment are out of scope.
```

If asked, use fictional PDF/text documents as inputs and store employees as users.

### Step 2: Check the sources

Open each candidate Building Block's README and check the assets and prerequisites. If a link fails, search from the [Building Blocks overview](https://github.com/ibm-self-serve-assets/building-blocks). Mark anything you cannot confirm as unverified.

### Step 3: Record the result

```text
Create a Markdown file at the workspace root and record the research results.
Under “Exercise 1”, include the problem, related BBs, source URLs, checked date, assets, prerequisites, search coverage, and unchecked areas.
Separate verified facts from assumptions and preserve existing notes.
```

## Exercise 2: use a skill or mode from the most relevant BB {#exercise-2}

15 minutes

### Step 1: Find candidates

Continue the Exercise 1 conversation and paste the following:

```text
Select the single BB most relevant to this scenario from the results and explain why.
Search the catalog for skills or modes associated with that BB.
Propose one for exploring fictional questions and response policies. Show its association with the BB, purpose, source URL, prerequisites, and files to add or change.
Explain what to try after adding it.
Do not add or configure anything yet.
```

Check the association between the selected BB and the skill or mode, its official source, and prerequisites. If none is usable, record why and consult the instructor.

### Step 2: Add the selected candidate

Review the purpose, prerequisites, destination, and changes, then paste:

```text
Use the official installer to add and configure only the reviewed candidate in this workshop workspace.
Preserve existing settings. Show the official source URL, destination, validation result, and how to start using it.
Stop and report if additional credentials or external services are needed.
Product installation and deployment are out of scope.
```

Check the installer result and added files, then reload Bob. For a skill, check `SKILL.md` under `.bob/skills/`. For a mode, select the added mode in the mode picker. Use Bob on either macOS or Windows.

### Step 3: Use the added candidate

Name the skill explicitly or select the mode, then continue the Exercise 1 scenario. Replace “selected candidate name” below before pasting:

```text
Use “selected candidate name” to explore store-assistant questions and response policies from these fictional product documents.

Source A: The Travel Mug holds 350 mL. It is not dishwasher-safe.
Source B: Unused products can be returned within 30 days of purchase. Proof of purchase is required.

Give two questions the documents can answer and one they cannot.
For each, provide an example answer and source, or explain why no answer is available.
Explain which procedures or considerations from the skill or mode you used.
Append the selected BB and reason, added skill or mode, source URL, destination, procedures used, questions and answers, and incomplete operations under “Exercise 2” in the Markdown file created in Exercise 1.
Preserve existing notes, including Exercise 1.
Code execution and product deployment are out of scope.
```

Check the link between sources and answers, handling of missing evidence, and the procedures or considerations used from the skill or mode. Confirm actual use in the answer, not merely installation.

If download or use fails, check another skill or mode associated with the same BB, or ask the instructor to work in a functioning pair. Record incomplete operations as such.

[Next →](summary.md){ .workshop-next }
