#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print the first 10 hot post titles, or None if the subreddit is bad."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:alu.api_advanced:v1.0 (by /u/alu_student)"
    }
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    data = response.json().get("data") or {}
    children = data.get("children") or []
    for post in children[:10]:
        print((post.get("data") or {}).get("title"))
