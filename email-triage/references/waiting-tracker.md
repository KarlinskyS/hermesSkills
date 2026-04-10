# Waiting / Follow-up Tracker

## Goal

Track pending external responses without faking certainty.

## Important Distinction

`waiting` is not a category for confusing email.
`waiting` means:
- the thread matters
- user side already acted or is blocked
- another party owes a response or deliverable

## Valid Waiting Cases

- proposal sent, awaiting answer
- invoice disputed, awaiting response
- meeting time suggested, awaiting confirmation
- doc shared for review, awaiting comments
- vendor promised update
- candidate/client/partner owes next step

## Invalid Waiting Cases

- random newsletter
- vague cold email
- thread you have not read enough to understand
- unresolved ownership
- “maybe important someday”

## Data to Track

For each waiting item store:
- counterpart
- topic
- thread id
- what exactly is pending
- last relevant date
- recommended follow-up date
- urgency
- confidence

## Follow-up Timing Heuristics

Suggested defaults:
- scheduling -> 1-2 business days
- invoice / finance -> 2-4 business days
- client / delivery / blocking request -> 1-3 business days
- general non-urgent thread -> 3-5 business days

## Output Format

For digest:
- `<counterpart>` — `<pending item>` — с `<date>` — follow-up: `<recommended date>`

## Escalation Logic

If waiting item crosses follow-up window:
- flag it in digest as overdue waiting
- optionally move into `needs-follow-up` note inside digest
- do not create Linear automatically; surface it as a candidate and wait for a direct user command

## Anti-Patterns

- mark everything unclear as waiting
- store no “pending item” text
- keep waiting list without follow-up dates
- convert every waiting item into a task
