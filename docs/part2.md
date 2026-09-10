# Two practical exercises

**Time: 25 minutes · Elapsed: 30–55 minutes**

Use the Explorer mode for both tasks. The scenarios are fictional. Record the actual answer and sources; different candidates can be valid when the reasoning fits. Do not deploy a product or supply customer credentials.

## Exercise 1: a document-based assistant {#exercise-1}

**12 minutes · Elapsed: 30–42 minutes**

A software partner wants to show a retail customer how store employees could find product and policy answers in approved documents. This is a discovery demo, not a production launch. The assistant should show its source and admit when the documents do not answer the question.

### Step 1: Start a discovery conversation

Start a new conversation in the Explorer mode and paste:

```text
I am in Build Sales and new to Building Blocks. A fictional software
partner is preparing a discovery demo for a retailer. Store employees
need answers from approved product and policy documents, with sources;
when no source supports an answer, the assistant should say so.
Use the current catalog tools. Ask at most two clarifying questions,
one at a time. Propose at most two Building Blocks and explain each
in business language, with a source URL and one point to validate.
Do not install skills, change modes, or deploy anything.
```

Suggested answers if Bob asks: the users are store employees; the inputs are fictional PDF/text documents; success means a source-backed answer or a clear “not found.” Do not add real customer content.

### Step 2: Check the recommendation

Open the links for both candidates. Read the README sections describing purpose, available assets, and prerequisites. If an Explorer link is stale, locate the corresponding page from the [current upstream overview](https://github.com/ibm-self-serve-assets/building-blocks) and record both paths. If you cannot verify it, label it “unverified.”

Ask this follow-up:

```text
Separate what the source explicitly provides from what you infer.
For each candidate, identify an available asset and a prerequisite.
If the catalog and README disagree, show the difference and leave it
as an open question. Do not claim measured ROI or production readiness.
```

### Step 3: Write the result

Record these fields in your worksheet:

| Field | What to write |
|---|---|
| Business problem | One sentence about the employee's task |
| Candidate 1 and 2 | Name and why each helps |
| Evidence | Source URL, checked date, and an actual asset or documented capability |
| Validation | One question about answer quality, permissions, or prerequisites |
| Pitch | A 30-second explanation: problem → capability → next test |

??? example "Example direction, not a fixed answer"
    RAG can be a candidate for retrieving document evidence; Agent Builder can be a candidate for an assistant interface or task flow. Check their current READMEs rather than assuming they form a ready-to-run bundle. “We should test whether the answer cites the right policy” is a useful validation step. “This guarantees accurate answers” is not supported by the exercise.

    Current entry points: [RAG](https://github.com/ibm-self-serve-assets/building-blocks/tree/main/data/pipelines/rag) and [Agent Builder](https://github.com/ibm-self-serve-assets/building-blocks/tree/main/ai/agents/agent-builder).

**Done when:** you can explain two candidates, show their evidence or mark an unresolved source, and name the next test. Finding a stale catalog entry is a valid observation; do not invent a working asset.

## Exercise 2: an engineering handoff for secrets management {#exercise-2}

**13 minutes · Elapsed: 42–55 minutes**

A fictional partner repeatedly copies credentials into integration scripts while preparing demos. They want a repeatable way to manage secrets and machine access. You are preparing a discovery discussion with an engineer. You are not authorized to change systems or rotate credentials.

### Step 1: Compare the right kind of capability

Start a new conversation, keeping Exercise 1 notes. Paste:

```text
I am a beginner in Build Sales. A fictional partner copies credentials
into integration scripts for demos and wants repeatable secret and
machine-access management. This is a discovery discussion only.
Use the current catalog to find a relevant Building Block. Ask at most
two clarifying questions, one at a time. Explain why a secrets or
identity capability is relevant, and why a document-answering pattern
alone would not meet this need. Include source links and prerequisites.
Do not request secrets, install anything, rotate keys, or deploy.
```

Suggested answers: the users are the partner's demo engineering team; the current scripts connect to test APIs; no real credentials will be used; success means agreeing on a small validation plan, not implementing the integration today.

### Step 2: Prepare the handoff

After checking the source, paste:

```text
Create a short use_case_summary.md at the workspace root for an engineer.
Include the business problem, users, scope, candidate and rationale,
verified source URL, prerequisites, two open questions, and a small
next validation step with a success criterion. Clearly separate facts
from assumptions. Use only this fictional scenario. Do not install,
configure services, or deploy. A diagram is optional.
```

Approve only the requested local document write if Bob asks. If the file cannot be written, copy the answer into your worksheet. A text-only handoff is sufficient; a diagram or installed product is not required.

### Step 3: Review and share a pitch

| Check | Passing result |
|---|---|
| Problem and scope | Describes secrets/machine access and a discovery discussion |
| Candidate and source | Explains the fit and cites a readable source, or flags uncertainty |
| Prerequisites | Names a requirement actually documented in the source |
| Open questions | Two questions an engineer or customer must resolve |
| Next step | A small test with an observable success criterion |
| Language | A colleague without implementation experience can explain it |

??? example "A possible handoff"
    A secrets-management candidate may use Vault. Check the current [Secrets Management README](https://github.com/ibm-self-serve-assets/building-blocks/tree/main/automation/secure/non-human-identity-and-secret-management/secrets-management). Do not infer that an operational Vault environment is included.

    Open questions: which system issues the identity, and who owns the secret lifecycle? A proposed next test could use a dummy secret in an approved sandbox and verify that the script retrieves it without hardcoding it. This is a plan for engineering, not an instruction to run the test during this workshop.

**Done when:** your handoff includes a rationale, evidence, two open questions, and a next test. Read a 30-second pitch to a partner or the instructor.

- [ ] I completed the document-assistant recommendation.
- [ ] I completed the secrets-management handoff.
- [ ] I separated verified facts from assumptions and recorded failures honestly.

[Next: review at minute 55 →](summary.md)

If you finished early, try the [optional installation challenge](part3.md).
