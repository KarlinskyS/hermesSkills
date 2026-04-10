# Digest Format

## Goal

Present only the decision-relevant output.

Digest should be:
- in Russian
- compact
- operational
- grouped by decision type
- free of filler
- optimized for quick follow-up from Telegram

## Reference Codes

Every item must start with a short reference code:

- `A#` for action
- `R#` for reply
- `W#` for waiting
- `F#` for finance
- `N#` for newsletters
- `Z#` for noise

These refs are required because the user may respond from Telegram with commands such as:

- `details R2`
- `reply R1`
- `archive Z1`
- `summarize N1`
- `create task A2`
- `check linear A1`

## Mandatory Sections

Use only sections that have items.

### Работа / задачи
Include:
- action candidates, plus any matched or created Linear issues if the user explicitly requested it
- reference code
- sender
- deadline
- 1-2 line summary
- why it matters

### Нужно ответить
Include:
- reference code
- sender
- reason reply is needed
- urgency
- whether reply is short or thoughtful

### Ждём ответа
Include:
- reference code
- counterpart
- pending item
- since when
- recommended follow-up date

### Финансы / документы
Include:
- reference code
- invoice / receipt / renewal / contract
- amounts and dates when explicit
- risk or required action if present

### Рассылки / почитать
Include:
- reference code
- source
- topic bullets or 1-2 line summary
- only useful signal, not fluff

### Шум / на проверку
Include:
- reference code
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
Работа / задачи
- [A1] Client X — подготовить ответ по pricing
  От: person@company.com
  Срок: 2026-04-10
  Суть: клиент просит финальный pricing breakdown и ответ по условиям.
  Linear: candidate only, не создавать без прямой команды

Нужно ответить
- [R1] Иван — подтвердить слот на созвон — сегодня
- [R2] Vendor X — ответить по renewal options — средний приоритет

Ждём ответа
- [W1] Legal team — комментарии по договору — с 2026-04-07 — follow-up 2026-04-10

Финансы / документы
- [F1] Receipt from Stripe — списание $29 — действия не требует
- [F2] Contract renewal from Tool X — renewal window 2026-04-15

Рассылки / почитать
- [N1] AI Engineering Weekly — 3 материала про evals, agents, tooling; полезно из-за практических паттернов.

Шум / на проверку
- [Z1] random@promo.com — массовая промо-рассылка
```

## Anti-Patterns

- dump entire email bodies
- mix newsletters into work section
- hide deadlines inside paragraphs
- make the digest look like a diary
- use plain numbering with no bucket prefix
- create Linear tasks without a direct user command
