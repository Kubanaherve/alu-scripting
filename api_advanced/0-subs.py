#!/usr/bin/python3
"""Return the number of subscribers of a subreddit using the Reddit API."""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers, or 0 if the subreddit is invalid."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json().get("data", {}).get("subscribers", 0)
