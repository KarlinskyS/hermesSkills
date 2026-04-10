#!/usr/bin/env python3
"""
Refresh Google OAuth2 token if expired and print current access token to stdout.
Used by gws.sh wrapper.
"""
import json
import sys
import datetime
from pathlib import Path

TOKEN_FILE = Path('/root/.hermes/google_token.json')

def get_token():
    with open(TOKEN_FILE) as f:
        data = json.load(f)

    # Check if token is still valid (with 60s buffer)
    expiry_str = data.get('expiry', '')
    if expiry_str:
        # Parse expiry
        expiry_str = expiry_str.replace('Z', '+00:00')
        try:
            expiry = datetime.datetime.fromisoformat(expiry_str)
            if expiry.tzinfo is None:
                expiry = expiry.replace(tzinfo=datetime.timezone.utc)
            now = datetime.datetime.now(datetime.timezone.utc)
            if (expiry - now).total_seconds() > 60:
                # Token still valid
                print(data['token'])
                return
        except Exception:
            pass

    # Need to refresh
    try:
        from google.oauth2.credentials import Credentials
        from google.auth.transport.requests import Request

        creds = Credentials(
            token=data['token'],
            refresh_token=data['refresh_token'],
            token_uri=data['token_uri'],
            client_id=data['client_id'],
            client_secret=data['client_secret'],
            scopes=data['scopes'],
        )
        creds.refresh(Request())

        # Save refreshed token
        data['token'] = creds.token
        if creds.expiry:
            data['expiry'] = creds.expiry.isoformat() + 'Z'
        with open(TOKEN_FILE, 'w') as f:
            json.dump(data, f, indent=2)

        print(creds.token)
    except Exception as e:
        print(f"Error refreshing token: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    get_token()
