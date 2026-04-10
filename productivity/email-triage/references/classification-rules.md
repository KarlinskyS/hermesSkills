# Email Classifier

## Goal

Avoid fake precision and avoid garbage task creation.

The classifier is not trying to guess “what feels important”.
It must decide:
- is this work?
- is it reply-only?
- is it waiting?
- is it newsletter/reference/finance/noise?
- how confident is the classification?

## Core Dimensions

### 1. Sender importance
- VIP human
- known collaborator
- internal system / service
- newsletter sender
- unknown external

### 2. Message type
- direct request
- follow-up
- scheduling
- review request
- invoice/receipt
- contract/legal
- automated notification
- newsletter/digest
- marketing/promo

### 3. Actionability
- explicit ask present?
- user is the owner?
- deadline present?
- attachment/doc review needed?
- should this survive outside email?

### 4. Durability
Durable means it deserves a place in a task system.
Non-durable means it should remain in email.

Examples of durable work:
- prepare proposal
- review PRD / contract / spec
- send deliverable by date
- fix / decide / approve something project-related

Examples of non-durable work:
- answer a short question
- acknowledge receipt
- accept/reject invite
- skim update with no follow-up

### 5. Time sensitivity
- today
- tomorrow
- this week
- explicit exact date
- no timing signal

## Buckets and Decision Tests

### action
Put into `action` only if all are true:
- non-trivial work exists
- user owns the next move
- work is durable
- the task should be visible outside email
- not already obviously tracked elsewhere

### reply
Put into `reply` if:
- user should answer
- work is primarily communication
- no separate project task is needed

### waiting
Put into `waiting` if:
- someone else owes the next response
- the thread matters
- follow-up may be needed later

### read-later
Put into `read-later` if:
- digest / newsletter / article
- no direct action requested

### reference
Put into `reference` if:
- information is useful
- no action or reply required

### finance
Put into `finance` if:
- invoice / payment / receipt / renewal / subscription / tax / contract

### noise
Put into `noise` if:
- low-signal automation
- promotional or irrelevant
- likely safe to ignore, but not safe to auto-delete

## Confidence Thresholds

### High
Evidence is explicit and unambiguous.
Allowed actions:
- classify
- label
- route
- archive if safe
- prepare a Linear recommendation if relevant, but wait for a direct user command before create/match

### Medium
Important but partially ambiguous.
Allowed actions:
- classify conservatively
- summarize for review
- keep in inbox if needed
- do not create a new Linear issue; at most prepare a candidate and note duplication risk

### Low
Unclear sender intent, unclear ownership, unclear value.
Allowed actions:
- no task creation
- no archiving
- ask one focused clarification or keep in review bucket

## Heuristics

### Strong action signals
- “can you”
- “please review”
- “need your input”
- “deadline”
- “by EOD / tomorrow / Friday”
- explicit deliverable or decision request

### Strong reply-only signals
- “does this work for you?”
- “confirm”
- “let me know”
- short logistical question
- “thanks / acknowledged?” style threads

### Strong waiting signals
- user already replied earlier in thread
- external party promised an update
- proposal / invoice / approval / scheduling response pending

### Strong newsletter signals
- unsubscribe footer
- multiple stories/articles
- editorial format
- broad audience style
- no direct addressability

### Strong finance signals
- invoice number
- tax / VAT / renewal / billing date
- amount charged
- subscription receipt
- contract / agreement attachment

### Strong noise signals
- mass marketing
- cold outreach with no relevance
- social digest with no useful information
- repeated automated alerts without action value

## Anti-Patterns

Do not:
- classify every “please” as durable action
- convert every human email into Linear
- call a newsletter “important” just because the topic is interesting
- use waiting for vague uncertainty
- treat finance emails as noise
- archive medium-confidence legal/finance mail without summary
