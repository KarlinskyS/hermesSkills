---
name: google-workspace
description: Gmail, Calendar, Drive, Contacts, Sheets, and Docs integration via Python. Uses OAuth2 with automatic token refresh. No external binaries needed — runs entirely with Google's Python client libraries in the Hermes venv.
version: 1.1.0
author: Nous Research
license: MIT
metadata:
  hermes:
    tags: [Google, Gmail, Calendar, Drive, Sheets, Docs, Contacts, Email, OAuth]
    homepage: https://github.com/NousResearch/hermes-agent
    related_skills: [himalaya]
---

# Google Workspace

Gmail, Calendar, Drive, Contacts, Sheets, and Docs — all through Python scripts in this skill. No external binaries to install.

## References

- `references/gmail-search-syntax.md` — Gmail search operators (is:unread, from:, newer_than:, etc.)

## Scripts

- `scripts/setup.py` — OAuth2 setup (run once to authorize)
- `scripts/google_api.py` — API wrapper CLI (agent uses this for all operations)

---

## First-Time Setup

The setup is fully non-interactive — you drive it step by step so it works
on CLI, Telegram, Discord, or any platform.

Define a shorthand first:

```bash
GSETUP="python ~/.hermes/skills/productivity/google-workspace/scripts/setup.py"
```

### Step 0: Check if already set up

```bash
$GSETUP --check
```

If it prints `AUTHENTICATED`, skip to the **gws CLI** section below — setup is already done.

### Step 1: Triage — ask the user what they need

Before starting OAuth setup, ask the user TWO questions:

**Question 1: "What Google services do you need? Just email, or also
Calendar/Drive/Sheets/Docs?"**

- **Email only** → They don't need this skill at all. Use the `himalaya` skill
  instead — it works with a Gmail App Password (Settings → Security → App
  Passwords) and takes 2 minutes to set up. No Google Cloud project needed.
  **Important:** Gmail requires 2FA to be enabled before App Passwords become
  available. Less Secure Apps (plain IMAP/SMTP with password) were permanently
  disabled by Google on March 14, 2025. If the user does not have 2FA enabled,
  they must enable it first, or use this skill's full OAuth flow instead.
  Load the himalaya skill and follow its setup instructions.

- **Calendar, Drive, Sheets, Docs (or email + these)** → Continue with this
  skill's OAuth setup below.

**Question 2: "Does your Google account use Advanced Protection (hardware
security keys required to sign in)? If you're not sure, you probably don't
— it's something you would have explicitly enrolled in."**

- **No / Not sure** → Normal setup. Continue below.
- **Yes** → Their Workspace admin must add the OAuth client ID to the org's
  allowed apps list before Step 4 will work. Let them know upfront.

### Step 2: Create OAuth credentials (one-time, ~5 minutes)

Tell the user:

> You need a Google Cloud OAuth client. This is a one-time setup:
>
> 1. Go to https://console.cloud.google.com/apis/credentials
> 2. Create a project (or use an existing one)
> 3. Click "Enable APIs" and enable: Gmail API, Google Calendar API,
>    Google Drive API, Google Sheets API, Google Docs API, People API
> 4. Go to Credentials → Create Credentials → OAuth 2.0 Client ID
> 5. Application type: "Desktop app" → Create
> 6. Click "Download JSON" and tell me the file path

Once they provide the path:

```bash
$GSETUP --client-secret /path/to/client_secret.json
```

### Step 3: Get authorization URL

```bash
$GSETUP --auth-url
```

This prints a URL. **Send the URL to the user** and tell them:

> Open this link in your browser, sign in with your Google account, and
> authorize access. After authorizing, you'll be redirected to a page that
> may show an error — that's expected. Copy the ENTIRE URL from your
> browser's address bar and paste it back to me.

### Step 4: Exchange the code

The user will paste back either a URL like `http://localhost:1/?code=4/0A...&scope=...`
or just the code string. Either works. The `--auth-url` step stores a temporary
pending OAuth session locally so `--auth-code` can complete the PKCE exchange
later, even on headless systems:

```bash
$GSETUP --auth-code "THE_URL_OR_CODE_THE_USER_PASTED"
```

### Step 5: Verify

```bash
$GSETUP --check
```

Should print `AUTHENTICATED`. Setup is complete — token refreshes automatically from now on.

### Notes

- Token is stored at `~/.hermes/google_token.json` and auto-refreshes.
- Restrict file permissions immediately after setup: `chmod 600 ~/.hermes/google_token.json`
- Pending OAuth session state/verifier are stored temporarily at `~/.hermes/google_oauth_pending.json` until exchange completes.
- To revoke: `$GSETUP --revoke`

---

## Usage

## gws CLI (Preferred Method)

`gws` is the Google Workspace CLI (~11.6k stars on GitHub) — auto-refreshes token via wrapper, covers ALL APIs dynamically from Google Discovery Service.

> **Note:** gws is not an officially supported Google product (as stated in its own `--version` output), but is actively maintained by a Google team.

Install: `npm install -g @google/gws-cli`

Wrapper: `bash ~/.hermes/skills/productivity/google-workspace/scripts/gws.sh`

```bash
GWS="bash ~/.hermes/skills/productivity/google-workspace/scripts/gws.sh"

# Gmail — list, read, send
$GWS gmail users messages list --params '{"userId":"me","maxResults":10}'
$GWS gmail users messages get --params '{"userId":"me","id":"MESSAGE_ID","format":"full"}'

# Calendar — list events, create
$GWS calendar events list --params '{"calendarId":"primary","maxResults":10,"orderBy":"startTime","singleEvents":true}'

# Drive — list files
$GWS drive files list --params '{"pageSize":10,"fields":"files(id,name,mimeType,modifiedTime)"}'

# Sheets — read range (single quotes required due to !)
$GWS sheets spreadsheets values get --params '{"spreadsheetId":"ID","range":"Sheet1!A1:C10"}'

# Auto-pagination (streams NDJSON)
$GWS gmail users messages list --params '{"userId":"me"}' --page-all

# Inspect schema of any method
$GWS schema gmail.users.messages.get
```

The wrapper auto-refreshes the token via `scripts/refresh_token.py` before each call.
New tokens saved back to `~/.hermes/google_token.json` automatically.

---

## Python API (Fallback)

All commands go through the API script. Set `GAPI` as a shorthand:

```bash
GAPI="python ~/.hermes/skills/productivity/google-workspace/scripts/google_api.py"
```

### Gmail

```bash
# Search (returns JSON array with id, from, subject, date, snippet)
$GAPI gmail search "is:unread" --max 10
$GAPI gmail search "from:boss@company.com newer_than:1d"
$GAPI gmail search "has:attachment filename:pdf newer_than:7d"

# Read full message (returns JSON with body text)
$GAPI gmail get MESSAGE_ID

# Send
$GAPI gmail send --to user@example.com --subject "Hello" --body "Message text"
$GAPI gmail send --to user@example.com --subject "Report" --body "<h1>Q4</h1><p>Details...</p>" --html

# Send with attachment
$GAPI gmail send --to user@example.com --subject "Report" --body "See attached" --attachment /path/to/file.pdf

# Reply (automatically threads and sets In-Reply-To)
$GAPI gmail reply MESSAGE_ID --body "Thanks, that works for me."
$GAPI gmail reply MESSAGE_ID --body "<b>Works!</b>" --html

# Labels
$GAPI gmail labels
$GAPI gmail modify MESSAGE_ID --add-labels LABEL_ID
$GAPI gmail modify MESSAGE_ID --remove-labels UNREAD
```

### Calendar

```bash
# List events (defaults to next 7 days)
$GAPI calendar list
$GAPI calendar list --start 2026-03-01T00:00:00Z --end 2026-03-07T23:59:59Z

# Create event (ISO 8601 with timezone required)
$GAPI calendar create --summary "Team Standup" --start 2026-03-01T10:00:00-06:00 --end 2026-03-01T10:30:00-06:00
$GAPI calendar create --summary "Lunch" --start 2026-03-01T12:00:00Z --end 2026-03-01T13:00:00Z --location "Cafe"
$GAPI calendar create --summary "Review" --start 2026-03-01T14:00:00Z --end 2026-03-01T15:00:00Z --attendees "alice@co.com,bob@co.com"

# Delete event
$GAPI calendar delete EVENT_ID
```

### Drive

```bash
$GAPI drive search "quarterly report" --max 10
$GAPI drive search "mimeType='application/pdf'" --raw-query --max 5
```

### Contacts

```bash
$GAPI contacts list --max 20
```

### Sheets

```bash
# Read
$GAPI sheets get SHEET_ID "Sheet1!A1:D10"

# Write
$GAPI sheets update SHEET_ID "Sheet1!A1:B2" --values '[["Name","Score"],["Alice","95"]]'

# Append rows
$GAPI sheets append SHEET_ID "Sheet1!A:C" --values '[["new","row","data"]]'
```

### Docs

```bash
$GAPI docs get DOC_ID
```

---

## Output Format

All commands return JSON. Parse with `jq` or read directly. Key fields:

- **Gmail search**: `[{id, threadId, from, to, subject, date, snippet, labels}]`
- **Gmail get**: `{id, threadId, from, to, subject, date, labels, body}`
- **Gmail send/reply**: `{status: "sent", id, threadId}`
- **Calendar list**: `[{id, summary, start, end, location, description, htmlLink}]`
- **Calendar create**: `{status: "created", id, summary, htmlLink}`
- **Drive search**: `[{id, name, mimeType, modifiedTime, webViewLink}]`
- **Contacts list**: `[{name, emails: [...], phones: [...]}]`
- **Sheets get**: `[[cell, cell, ...], ...]`

---

## Rules

1. **Never send email or create/delete events without confirming with the user first.** Show the draft content and ask for approval.
2. **Check auth before first use** — run `setup.py --check`. If it fails, guide the user through setup.
3. **Use the Gmail search syntax reference** for complex queries — load it with `skill_view("google-workspace", file_path="references/gmail-search-syntax.md")`.
4. **Calendar times must include timezone** — always use ISO 8601 with offset (e.g., `2026-03-01T10:00:00-06:00`) or UTC (`Z`).
5. **Respect rate limits** — avoid rapid-fire sequential API calls. Batch reads when possible.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `NOT_AUTHENTICATED` | Run setup Steps 2–5 above |
| `REFRESH_FAILED` | Token revoked or expired — redo Steps 3–5 |
| `Error refreshing token: invalid_grant` | Refresh token invalidated (password change, manual revoke, or 6 months of inactivity). Delete `~/.hermes/google_token.json` and redo Steps 3–5 |
| `HttpError 403: Insufficient Permission` | Missing API scope — `$GSETUP --revoke` then redo Steps 3–5 |
| `HttpError 403: Access Not Configured` | API not enabled — user needs to enable it in Google Cloud Console |
| `HttpError 429: Too Many Requests` | Rate limit hit — add delay between calls or batch requests where possible |
| `ModuleNotFoundError` | Run `$GSETUP --install-deps` |
| Advanced Protection blocks auth | Workspace admin must allowlist the OAuth client ID |

### When does a refresh token become invalid?

A refresh token can be invalidated at any time for these reasons:
- User changed their Google account password
- User manually revoked access via Google Account → Security → Third-party apps
- Token unused for 6+ months
- More than 100 active refresh tokens exist for this OAuth client + account pair
- Workspace admin revoked app access

When this happens, `refresh_token.py` will exit with `invalid_grant`. Delete the token file and re-authenticate from Step 3.

---

## Revoking Access

```bash
$GSETUP --revoke
```
