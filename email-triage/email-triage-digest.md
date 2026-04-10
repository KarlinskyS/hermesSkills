---
name: email-triage-digest
description: Produce a compact Russian digest from triaged email with separate sections for work, replies, waiting, finance, newsletters, and noise.
category: productivity
---

# Digest Generator

## Goal

Present only the decision-relevant output.

Digest should be:
- in Russian
- compact
- operational
- grouped by decision type
- free of filler

## Mandatory Sections

Use only sections that have items.

### Работа / задачи
Include:
- created or matched Linear issues
- sender
- deadline
- 1-2 line summary
- why it matters

### Нужно ответить
Include:
- sender
- reason reply is needed
- urgency
- whether reply is short or thoughtful

### Ждём ответа
Include:
- counterpart
- pending item
- since when
- recommended follow-up date

### Финансы / документы
Include:
- invoice / receipt / renewal / contract
- amounts and dates when explicit
- risk or required action if present

### Рассылки / почитать
Include:
- source
- topic bullets or 1-2 line summary
- only useful signal, not fluff

### Шум / на проверку
Include:
- sender/subject
- why classified as noise
- optional recommended action: ignore / unsubscribe / review later

## Style Rules

- no intros
- no motivational filler
- no verbose retelling of email content
- no category should become a wall of text
- sort by urgency inside sections

## Output Template

```text
🔥 Работа / задачи (N)
- [created] IEF-123 — Подготовить ответ по pricing для клиента X
  От: person@company.com
  Срок: 2026-04-10
  Суть: клиент просит финальный pricing breakdown и ответ по условиям.

✉️ Нужно ответить (N)
- Иван — подтвердить слот на созвон — сегодня
- Vendor X — ответить по renewal options — средний приоритет

⏳ Ждём ответа (N)
- Legal team — комментарии по договору — с 2026-04-07 — follow-up 2026-04-10

💳 Финансы / документы (N)
- Receipt from Stripe — списание $29 — действия не требует
- Contract renewal from Tool X — renewal window 2026-04-15

📰 Рассылки / почитать (N)
- AI Engineering Weekly — 3 материала про evals, agents, tooling; полезно из-за практических паттернов.

🗑 Шум / на проверку (N)
- random@promo.com — массовая промо-рассылка
```

## Anti-Patterns

- dump entire email bodies
- mix newsletters into work section
- hide deadlines inside paragraphs
- make the digest look like a diary
