---
name: email-triage-queries
description: Gmail query patterns for high-signal triage, newsletters, finance, reply pressure, and stale inbox review.
category: productivity
---

# Gmail Query Patterns

## Goal

Use Gmail search as routing, not as a dumb inbox dump.

## Core Queries

### 1. High-signal unread inbox
```bash
bash ~/.hermes/skills/productivity/google-workspace/scripts/gws.sh gmail messages list --maxResults=50 --q='in:inbox is:unread -category:promotions -category:social'
```

### 2. Potential newsletters / reading queue
```bash
bash ~/.hermes/skills/productivity/google-workspace/scripts/gws.sh gmail messages list --maxResults=50 --q='in:inbox is:unread (category:updates OR category:forums OR has:unsubscribe)'
```

### 3. Finance / billing / subscriptions
```bash
bash ~/.hermes/skills/productivity/google-workspace/scripts/gws.sh gmail messages list --maxResults=50 --q='(in:inbox OR label:triage/finance) (invoice OR receipt OR payment OR renewal OR contract OR subscription)'
```

### 4. Possible urgent replies
```bash
bash ~/.hermes/skills/productivity/google-workspace/scripts/gws.sh gmail messages list --maxResults=50 --q='in:inbox (reply OR review OR urgent OR deadline OR tomorrow OR today OR EOD)'
```

### 5. Stale unread review
```bash
bash ~/.hermes/skills/productivity/google-workspace/scripts/gws.sh gmail messages list --maxResults=50 --q='in:inbox is:unread older_than:7d'
```

### 6. Existing waiting items
```bash
bash ~/.hermes/skills/productivity/google-workspace/scripts/gws.sh gmail messages list --maxResults=50 --q='label:triage/waiting'
```

## Routing Advice

- Use query passes, not one giant fetch.
- High-signal pass goes first.
- Newsletters should be isolated on their own pass.
- Finance should be its own pass because the false-negative cost is high.
- Stale unread review should be periodic, not part of every triage pass.

## Anti-Patterns

- single giant `is:unread` fetch for everything
- reading full content for all search results
- mixing finance and promo in one undifferentiated batch
