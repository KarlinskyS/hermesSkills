# Calibration Playbook

This file exists for gradual tuning. After each bad triage decision, add a concrete rule here. Do not try to make the skill perfect in one pass. Build the playbook from real corrections.

## Sender Policies

Add entries in plain text using this shape:

- VIP sender: `<email>` because `<reason>`
- Newsletter for full translation: `<email>` because `<reason>`
- Newsletter for summary only: `<email>` because `<reason>`
- Always noise domain: `<domain>` because `<reason>`
- Always finance sender: `<email>` because `<reason>`

## Classification Overrides

When one sender or subject pattern should force a result, record it as:

- If sender is `<sender>` and subject contains `<text>`, force bucket `<bucket>`, confidence `<level>`, note `<why>`

## Linear Rules

Never promote subjects containing:

- `receipt`
- `invoice paid`
- `newsletter`
- `digest`
- `welcome`

Always consider promotion when subjects contain:

- `review needed`
- `deadline`
- `contract`
- `renewal`

Preferred title patterns:

- If subject contains `contract`, title as `Review contract terms for <entity>`
- If subject contains `renewal`, title as `Decide renewal for <entity>`

## Digest Preferences

- Show finance even if there is no action
- Show newsletters as compact summaries
- Do not hide low-value noise by default

## Retrospective Checklist

- Был ли создан мусорный task?
- Был ли пропущен реально важный email?
- Была ли рассылка слишком длинной?
- Не перепутали ли reply и action?
- Есть ли новый sender-specific rule, который надо закрепить?
