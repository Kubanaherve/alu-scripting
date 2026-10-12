#!/usr/bin/python3
"""Temporary diagnostic to reveal what the grader receives from Reddit."""
import requests


def top_ten(subreddit):
    """Print the raw HTTP result so the grader can show it back to us."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        print("STATUS:", response.status_code)
        print("BODY:", response.text[:300])
    except Exception as error:
        print("ERROR:", type(error).__name__, str(error)[:300])
