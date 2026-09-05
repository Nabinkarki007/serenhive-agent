# Operating Policy

## Approval modes

`AUTO` may only be used for explicitly approved low-risk workflows.

`HUMAN_REVIEW_REQUIRED` is the default for new workflows, promotions, medium-risk content, and any uncertainty.

`BLOCKED` applies to prohibited claims and unsafe or unsupported content.

## Audit record
Every decision should record:

- timestamp
- workflow and content ID
- source knowledge references
- risk level
- decision
- reviewer when applicable

Do not store platform passwords in this repository. Use official OAuth/API integrations and deployment-managed secrets.
