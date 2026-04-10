---
name: email-triage-linear
description: Promote only durable email work into Linear, with deduplication, issue shaping, and safe escalation rules.
category: productivity
---

# Linear Promotion Skill

## Goal

Protect Linear from inbox trash.

This skill exists to ensure that only durable, track-worthy work becomes an issue.

## Never Create a Linear Issue For

- quick reply-only emails
- pure FYI messages
- newsletters
- receipts / payment confirmations without follow-up work
- automated notifications
- vague or low-confidence requests
- work already tracked in an existing issue

## Promotion Criteria

Promote to Linear only if:
- there is a concrete outcome or decision
- the work is non-trivial
- it deserves visibility outside Gmail
- it may span multiple steps or time
- the owner is effectively the user / user team
- duplicate check is completed

## Required Inputs

Before creation, gather:
- sender
- subject
- thread id
- concise summary
- explicit asks
- deadlines
- important links
- attachments or docs mentioned
- reason this belongs in Linear

## Dedupe Strategy

Always search existing Linear issues before creating new one.

Search using:
- normalized subject keywords
- entity/topic names
- sender/domain if relevant
- delivery or deadline phrase
- related project nouns

If open issue already exists:
- do not create new issue
- mark result as `matched`
- attach email context to the digest output

If multiple possible matches:
- mark as `possible-duplicate`
- avoid automatic creation unless evidence strongly favors a new issue

## Issue Title Rules

Good title:
- starts with outcome
- concrete
- short
- independent of email subject wording

Bad:
- “Re: quick question”
- “Fwd: update”
- “Need your input”
- “Following up”

Good:
- “Review contract renewal terms for Tool X”
- “Send pricing answer to <client/company>”
- “Approve design feedback for onboarding flow”
- “Prepare response to billing discrepancy from vendor”

## Issue Description Template

Use structure:

- **Source:** email
- **Sender:** <name/email>
- **Received:** <date>
- **Subject:** <subject>
- **Summary:** <2-5 lines>
- **Explicit asks:** <bullet list>
- **Deadline:** <date or none>
- **Links / docs:** <list>
- **Why in Linear:** <reason this is durable work>

## Priority Heuristics

Raise urgency if:
- deadline is within 48 hours
- sender is VIP
- financial / legal / client risk exists
- blocking dependency exists
- explicit escalation language is present

## Output Contract

Return one of:
- `created`
- `matched`
- `possible-duplicate`
- `rejected` with reason

Include:
- recommended title
- short rationale
- issue id/link if available

## Anti-Patterns

- creating issue from every human request
- copying the subject line as task title
- skipping dedupe
- creating issues for “reply and done” work
- turning newsletters into backlog
