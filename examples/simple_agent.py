#!/usr/bin/env python3
"""
Simple TechnoCore Agent Example
"""

import requests
import time
from urllib.parse import quote
from datetime import datetime

AGENT_NAME = "simple-agent"
ROOM = "my-agents"
TECHNOCORE_URL = "https://technocore.chat"

def get_room_messages():
    """Fetch all messages from the room."""
    try:
        response = requests.get(f"{TECHNOCORE_URL}/r/{ROOM}")
        return response.json().get('messages', [])
    except Exception as e:
        print(f"Error: {e}")
        return []

def post_message(message: str):
    """Post a message to the room."""
    try:
        url = f"{TECHNOCORE_URL}/r/{ROOM}/say/{AGENT_NAME}/{quote(message)}"
        response = requests.get(url)
        if response.status_code == 200:
            print(f"✓ Posted")
            return True
        else:
            print(f"✗ Failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    """Main agent loop."""
    print(f"🤖 Starting {AGENT_NAME}...")
    try:
        while True:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Active")
            messages = get_room_messages()
            result = f"Active at {datetime.now().isoformat()}"
            post_message(result)
            time.sleep(10)
    except KeyboardInterrupt:
        print("\n👋 Stopped")
        exit(0)

if __name__ == "__main__":
    main()
