# Exercises

Time: 30 minutes (25–55)

Paste a question into Explorer and receive an answer.

## Exercise 1: ask about system modernization for a public sector client {#exercise-1}

Paste and run the following:

```text
Are there Building Blocks to propose to a public sector client that wants to modernize its legacy systems?
```

If Bob asks a question with choices, pick one. If Bob asks to approve creating a file or installing something, select **Reject**; once Bob has named candidates, move on.

## Exercise 2: ask about security for a financial services client {#exercise-2}

Paste and run the following:

```text
Are there Building Blocks to propose to a financial services client with strict security requirements?
```

If Bob asks a question with choices, pick one. If Bob asks to approve creating a file or installing something, select **Reject**; once Bob has named candidates, move on.

## Exercise 3: ask about a manufacturing client {#exercise-3}

Paste and run the following:

```text
Are there Building Blocks to propose to a manufacturing client?
```

If Bob asks a question with choices, pick one. If Bob asks to approve creating a file or installing something, select **Reject**; once Bob has named candidates, move on.

## Additional exercises (uv required) {#extra}

Use Explorer's local installer to add the Building Blocks you find to this workspace and to draw an architecture diagram. Bob asks for approval for each installer operation; check it and approve.

!!! warning "uv is required"
    These exercises require [installing uv](preparation.md). The installer does not start because of an upstream bug ([#262](https://github.com/ibm-self-serve-assets/building-blocks/issues/262)), so they cannot run until it is fixed.

### Exercise 4: install a skill {#exercise-4}

Paste and run the following:

```text
Choose one Bob skill for document search or RAG and install it in this workspace. Then show the skills and modes in this workspace.
```

Check that `.bob/skills/` has a folder for the skill with `SKILL.md`.

### Exercise 5: install a mode and switch to it {#exercise-5}

Paste and run the following:

```text
Choose one Bob mode for asking a database in plain language and install it in this workspace.
```

Check that the installed mode appears in the mode picker. If it does not, reload Bob. Once you can switch to it, switch back to the Explorer mode.

### Exercise 6: draw an architecture diagram {#exercise-6}

Paste and run the following:

```text
A retail store wants an assistant that answers questions from its product and policy documents. Choose the Building Blocks to use and draw an architecture diagram.
```

If Bob asks a question with choices, pick one.

Check that a diagram image (PNG) appears in the workspace and opens. Drawing the diagram sends its contents to an external service (mermaid.ink).

Reference: [Official Explorer guide](https://github.com/ibm-self-serve-assets/building-blocks/tree/f721f5ec1915225ade62d8d0e780fe6b19aa58b8/explore-BBs)

[Next →](summary.md){ .workshop-next }
