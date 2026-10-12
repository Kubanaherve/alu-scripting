#!/usr/bin/python3
"""Query the Reddit API and return a subreddit's subscriber count."""
import requests

HEADERS = {"User-Agent": "linux:alu.api.advanced:v1.0 (by /u/kubanaherve)"}


def number_of_subscribers(subreddit):
    """Return the number of subscribers of a subreddit, or 0 if invalid."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=HEADERS, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json().get("data", {}).get("subscribers", 0)
