---
name: arsenal
description: Central inventory of all connected integrations, discovered tools, and active workflows.
category: productivity
version: 1.0.0
---

# 🧰 ARSENAL

**Last Updated:** 2026-04-05
**Maintainer:** Hermes Agent

This is the single source of truth for all capabilities available to the user.

---

## 🔌 INTEGRATIONS (Connected & Active)

| Tool | Type | Status | Capabilities |
|------|------|--------|--------------|
| **Linear** | Task Tracker | ✅ Connected (MCP) | Create issues, projects, sync status. `linear_search_issues`, `linear_create_issue`. |
| **GitHub** | Code/Dev | ✅ Connected (MCP) | Repo management, PRs, CI/CD. `gh` CLI available. |
| **Google Workspace** | Email/Data | ✅ OAuth2 Active | Gmail (search, read, send), Calendar, Drive, Sheets. Wrapper: `gws.sh`. |
| **Notion** | Knowledge Base | ✅ Connected (MCP) | Create pages, update databases, search. `notion` MCP tools. |
| **Cron** | Scheduling | ✅ Native | Schedule recurring tasks/jobs. `cronjob`. |
| **Telegram** | Comms | ✅ Connected | DM with user, notifications, delivery channel. |

---

## 🛠 discovered tools / external apps

| Tool | Category | Use Case | Status | Notes |
|------|----------|----------|--------|-------|
| **Moda** | Design/AI | **Marketing assets & Pitch Decks.** AI agent that generates editable designs (slides, social posts) and "learns" your brand style over time. Built by ex-Dropbox/Heap founders. | 🟡 Interested (Not setup) | $7.5M raised. Uses "Cursor-style" agent interface. Good for Blessly launch marketing later. |
| **Enrich Labs (Helena)** | Marketing/AI | **Autonomous Marketer.** Inputs: URL. Outputs: Research + Strategy + Asset creation + Posting. | 🟡 Interested (Check later) | 3M views on launch video. Covers SEO, social listening, email. |

---

## 🔄 active workflows / skills

### 📬 Newsletter Deep Dive
**Trigger:** User says "Digest X" or "Read [Newsletter Name]".
**Process:**
1.  **Fetch:** Get latest email/URL content (e.g., via Gmail API or `web_extract`).
2.  **Parse:** Extract **all** bullet points/features (not just top 3).
3.  **Output:**
    *   **Standard:** Simple summary of each point (current mode for backlog).
    *   **Deep Mode (New Letters):** Summary + minimal research per point + user evaluation (Cool/Useless/Must-Try).
4.  **Archive:** Mark email as read after review.

### 🗑️ Email Triage
**Trigger:** "Clean inbox" or "Triage".
**Process:**
1.  **Categorize:** Group by sender/topic.
2.  **Action:**
    *   `Trash`: Spam, old promos, security alerts from kids (Roblox), NAS logs.
    *   `Keep`: Actionable items → Linear issues.
    *   `Read`: Superhuman/React digests (Summarize).
3.  **Rulebook:** (See `memory` for specific sender rules).

---

## 🚀 ROADMAP / TO DO

| Item | Category | Priority | Notes |
|------|----------|----------|-------|
| **Moda Setup** | Marketing | Low | Create account, ingest Blessly brand assets. Do this when Blessly is live. |
| **Blessly Launch Marketing** | Business | TBA | Use Moda for social media/banners once site is live. |
| **NAS IP Config** | DevOps | High | Find exact local IP for `karlinskyNas` (scan 192.168.1.x failed). |
