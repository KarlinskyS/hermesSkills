#!/bin/bash
# Wrapper для gws CLI с авто-рефрешем токена
# Usage: gws.sh <gws args...>
# Example: gws.sh gmail users messages list --params '{"userId":"me","maxResults":5}'

VENV="/root/.hermes/hermes-agent/venv/bin/python3"
TOKEN_FILE="/root/.hermes/google_token.json"
REFRESH_SCRIPT="/root/.hermes/skills/productivity/google-workspace/scripts/refresh_token.py"

# Получить свежий токен (рефрешит если надо)
TOKEN=$($VENV "$REFRESH_SCRIPT" 2>/dev/null)
if [ -z "$TOKEN" ]; then
    echo '{"error": "Failed to get/refresh Google token"}' >&2
    exit 1
fi

GOOGLE_WORKSPACE_CLI_TOKEN="$TOKEN" gws "$@"
