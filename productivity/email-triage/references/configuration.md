# Configuration

Apply these defaults unless the user explicitly overrides them.

## User Profile

- Language: Russian
- Digest language: Russian
- Time zone: Asia/Jerusalem

## Triage Defaults

- Batch size: 50 messages per pass
- Archive safe items after classification: yes
- Never delete automatically: yes
- Read full bodies only when needed: yes
- Never create Linear automatically: yes
- Confidence handling:
  - high: act
  - medium: review conservatively
  - low: ask or keep for review

## Gmail Labels

- `action`: `triage/action`
- `reply`: `triage/reply`
- `waiting`: `triage/waiting`
- `read-later`: `triage/read-later`
- `reference`: `triage/reference`
- `finance`: `triage/finance`
- `noise`: `triage/noise`

## Gmail Query Passes

- High signal: `in:inbox is:unread -category:promotions -category:social`
- Newsletters: `in:inbox is:unread (category:updates OR category:forums OR has:unsubscribe)`
- Finance: `in:inbox (is:unread OR newer_than:7d) (invoice OR receipt OR billing OR payment OR contract OR subscription)`
- Stale review: `in:inbox is:unread older_than:7d`

## Linear Defaults

- Linear integration: enabled
- Workspace: `Ieffai`
- Team: `IEF`
- Create issues only for durable work
- Always require duplicate check
- Always require a direct user command before any create or match action
- Reject reply-only items

## Newsletter Defaults

- Default mode: summarize
- Full-translate senders: none configured yet
- Deep-dive senders: none configured yet
- Deep-dive topics:
  - AI engineering
  - Frontend architecture
  - Startups
- Suppress sponsor blocks: yes

## Waiting Defaults

Default follow-up timing in business days:

- Scheduling: 2
- Finance: 3
- Legal: 3
- Client: 2
- Generic: 4

## Sender Rules

No sender-specific overrides are configured yet for these groups:

- VIP senders
- Always-reference domains
- Always-noise domains
- Always-finance senders
- Newsletter senders

## Output Defaults

- Include empty sections: no
- Max newsletters in digest: 5
- Max noise items in digest: 10
- Compact mode: yes
- Use Telegram-friendly refs: yes
- Ref prefixes:
  - `A` for action
  - `R` for reply
  - `W` for waiting
  - `F` for finance
  - `N` for newsletters
  - `Z` for noise
