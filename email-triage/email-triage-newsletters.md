---
name: email-triage-newsletters
description: Process newsletters separately from work email, summarize in Russian by default, and do full translation only for configured senders.
category: productivity
---

# Newsletter Handler

## Goal

Keep newsletters useful without letting them contaminate work triage.

## Default Behavior

Default newsletter behavior is:
- concise Russian summary
- 1-3 key topics
- 1 line on why it may matter
- no full translation unless sender is explicitly whitelisted

## Full Translation Is Allowed Only If

- sender is in config allowlist
- or user explicitly requested full translation for this sender/source

## Newsletter Detection Signals

Strong signals:
- unsubscribe footer
- multiple articles/sections
- editorial voice
- broad greeting
- many links
- no direct ask to user

## Output Modes

### summarize
Use for most newsletters.

Output:
- source/sender
- 2-5 topic bullets
- 1 compact Russian synthesis

### full_translate
Use only for configured senders.

Output:
- complete Russian translation
- preserve facts and links
- keep structure readable
- do not add external fact-checking

### deep_dive
Use when sender is configured or user asked for it.

Output:
- each article/case/topic as separate unit
- extracted tools, companies, techniques, arguments
- optional “what is actionable for user” section

## Compression Rules

Even good newsletters should be compressed.
Avoid:
- translating fluff
- preserving marketing filler
- repeating sponsor blocks unless important
- dumping huge walls of text into digest

## Good Digest Entry Example

- `Frontend Weekly` — статья про bundle-less dev server, заметка про CSS nesting, кейс по design tokens. Полезно из-за архитектурных trade-off и tooling direction.

## Anti-Patterns

- full translate everything
- mix newsletters with direct work items
- create Linear issues from newsletter content
- over-summarize until value is lost
