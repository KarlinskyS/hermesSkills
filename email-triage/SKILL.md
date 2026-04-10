# Email Triage

Use this skill as the single entrypoint. Load only the reference files needed for the current pass.

Use it when the user wants inbox triage, reply prioritization, waiting follow-up tracking, finance or document review, newsletter compression, or task promotion from email.

## Operating Rules

- Never delete email automatically.
- Never create a Linear task automatically.
- Never create a task before duplicate check and a direct user command.
- Never convert reply-only work into project tracking.
- Never archive ambiguous important mail too early.
- Never use `waiting` as a parking lot for uncertainty.
- Never full-read every unread message by default.

## Default Execution Order

1. Read [references/configuration.md](references/configuration.md) before acting so labels, query passes, and sender-specific rules are applied.
2. Read [references/core-workflow.md](references/core-workflow.md) for the end-to-end triage flow.
3. Read [references/classification-rules.md](references/classification-rules.md) before assigning buckets or confidence.
4. Read [references/gmail-queries.md](references/gmail-queries.md) when choosing or refining Gmail search passes.
5. Read exactly one route file for each item that needs deeper handling:
   - [references/linear-routing.md](references/linear-routing.md) for durable work that may belong in Linear
   - [references/newsletter-handling.md](references/newsletter-handling.md) for newsletters, digests, and reading queues
   - [references/waiting-tracker.md](references/waiting-tracker.md) for threads where another party owes the next move
6. Read [references/digest-format.md](references/digest-format.md) before producing the final user-facing digest.

## Reference Map

- [references/core-workflow.md](references/core-workflow.md): orchestration, hard rules, routing model, archive policy
- [references/classification-rules.md](references/classification-rules.md): buckets, confidence thresholds, durable-vs-reply logic
- [references/gmail-queries.md](references/gmail-queries.md): candidate-selection queries and search strategy
- [references/linear-routing.md](references/linear-routing.md): promotion criteria, dedupe, title shaping, output contract
- [references/newsletter-handling.md](references/newsletter-handling.md): summary, translation, deep-dive rules
- [references/waiting-tracker.md](references/waiting-tracker.md): valid waiting states and follow-up timing
- [references/digest-format.md](references/digest-format.md): required Russian digest structure
- [references/configuration.md](references/configuration.md): labels, query passes, sender rules, and output preferences
- [references/calibration-playbook.md](references/calibration-playbook.md): calibration template for updating sender rules and overrides over time

## Routing Checklist

- Route to `action` only when the work is durable and should survive outside email.
- Keep `action` items as candidates until the user explicitly says to create or match a Linear task.
- Route to `reply` when the next move is primarily communication.
- Route to `waiting` only when another party owes a meaningful response.
- Route to `finance` for invoices, receipts, renewals, contracts, billing, and tax-related mail.
- Route to `read-later` for newsletters and non-urgent reading.
- Route to `reference` for useful information with no action.
- Route to `noise` for low-signal promo or automation that is not safe to auto-delete.

## Telegram References

Every digest item must have a short reference code so the user can act on it quickly in Telegram.

- `A1`, `A2` for `action`
- `R1`, `R2` for `reply`
- `W1`, `W2` for `waiting`
- `F1`, `F2` for `finance`
- `N1`, `N2` for `newsletter`
- `Z1`, `Z2` for `noise`

Use these refs consistently inside one digest. The visible ref is for the user; the agent should internally map it to the real Gmail message id and thread id.

## Calibration

When behavior needs tuning after a false positive or false negative, read [references/calibration-playbook.md](references/calibration-playbook.md) and convert the new lesson into a sender rule, classification override, Linear promotion rule, or digest preference.
