---
name: email-triage-core
description: Orchestrate Gmail triage in batches, classify messages, route them to the right processing path, and produce a compact Russian digest.
category: productivity
---

# Email Triage Core

## Objective

Convert Gmail inbox into a decision pipeline.

This skill must:
- fetch high-signal email batches
- avoid expensive full reads unless necessary
- classify email into operational buckets
- route durable work into Linear only when justified
- keep reply-only work out of project tracking
- isolate newsletters from real work
- track external waiting states
- produce a compact Russian digest

## Hard Rules

- Never delete email automatically.
- Never create Linear tasks before duplicate check.
- Never treat every actionable sentence as a task.
- Never translate every newsletter in full by default.
- Never archive ambiguous important mail too early.
- Never use `waiting` as a parking lot for uncertainty.
- Never read full bodies for all unread messages by default.

## Operating Model

Email is processed in 4 layers:

1. **Candidate selection**
   Pull candidate emails from Gmail using focused queries.

2. **Lightweight triage**
   Inspect subject, sender, snippet, date, thread info, category.

3. **Deep inspection**
   Only for potentially important messages:
   - real requests
   - ambiguous important threads
   - finance/legal items
   - selected newsletters
   - anything with deadlines or documents

4. **Routing**
   Send email into one of these paths:
   - action / project work -> Linear path
   - reply-only -> reply bucket
   - waiting -> waiting tracker
   - newsletter -> newsletter handler
   - finance -> finance/reference bucket
   - noise -> review-only, never auto-delete

## Primary Buckets

| Bucket | Meaning | Typical outcome |
|---|---|---|
| action | durable work item | create or match Linear issue |
| reply | user needs to respond | keep visible, include in digest |
| waiting | another party owes response | track follow-up |
| read-later | newsletter/article | summarize, optionally archive |
| reference | useful info, no action | archive |
| finance | invoice/receipt/contract | summarize and preserve |
| noise | low-value automation/promo | flag for review |

## Batch Strategy

Process in the following order:

### Pass 1 — high signal inbox
```bash
bash ~/.hermes/skills/productivity/google-workspace/scripts/gws.sh gmail messages list --maxResults=50 --q='in:inbox is:unread -category:promotions -category:social'
```

### Pass 2 — updates / forums / newsletter candidates
```bash
bash ~/.hermes/skills/productivity/google-workspace/scripts/gws.sh gmail messages list --maxResults=50 --q='in:inbox is:unread (category:updates OR category:forums OR has:unsubscribe)'
```

### Pass 3 — finance / billing / receipts / contracts
```bash
bash ~/.hermes/skills/productivity/google-workspace/scripts/gws.sh gmail messages list --maxResults=50 --q='in:inbox (is:unread OR newer_than:7d) (invoice OR receipt OR billing OR payment OR contract OR subscription)'
```

## Lightweight Triage Fields

Do not fetch full content yet. First capture:
- message id
- thread id
- from
- subject
- snippet
- internal date
- labels/category if available

## Full Read Triggers

Fetch full body only if one or more are true:
- sender is VIP or known collaborator
- email contains explicit request
- email likely implies project work
- deadline/date is visible or suspected
- legal/finance context
- attachment or document review request
- newsletter is configured for full translation
- ambiguity is too high to classify safely

Example:
```bash
bash ~/.hermes/skills/productivity/google-workspace/scripts/gws.sh gmail messages get <message_id> --format=full
```

## Extraction Schema

For important emails extract:

- sender
- sender_type: human | automated | newsletter | unknown
- subject
- short_summary
- explicit_asks[]
- deadlines[]
- mentioned_links[]
- mentioned_docs[]
- recommended_bucket
- confidence: high | medium | low
- rationale

## Routing Rules

### Route to `email-triage-linear` if:
- work is durable
- this belongs in project tracking
- not just a quick reply
- there is enough clarity to write a task title
- dedupe check is possible

### Route to `email-triage-newsletters` if:
- sender matches newsletter pattern
- message has unsubscribe header or digest structure
- no direct ask to user

### Route to `email-triage-waiting` if:
- another party owes a response
- the thread is worth tracking
- there is a meaningful pending item

### Keep as `reply` if:
- answer is needed
- task should stay inside email, not in Linear

### Keep as `reference` if:
- useful information only
- no user action required

### Keep as `finance` if:
- invoice, billing, contract, payment, tax, receipt, renewal

### Keep as `noise` if:
- low-value automation, promo, irrelevant broadcast
- uncertain deletability

## Archive Policy

Safe to archive after classification:
- reference
- finance
- read-later
- matched action item already captured elsewhere

Keep in inbox:
- reply
- medium/low confidence important items
- anything needing user decision now

## Final Output Contract

Always produce a Russian digest grouped as:
- Работа / задачи
- Нужно ответить
- Ждём ответа
- Финансы / документы
- Рассылки / почитать
- Шум / на проверку

If no items in a group, omit the group.
