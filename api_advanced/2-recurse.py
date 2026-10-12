#!/usr/bin/python3
"""Recursively query the Reddit API and list all hot article titles."""
import requests

HEADERS = {"User-Agent": "linux:alu.api.advanced:v1.0 (by /u/kubanaherve)"}


def recurse(subreddit, hot_list=None, after=None):
    """Return a list of all hot article titles, or None if subreddit is bad."""
    if hot_list is None:
        hot_list = []
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 100}
    if after is not None:
        params["after"] = after
    response = requests.get(url, headers=HEADERS, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json().get("data", {})
    for post in data.get("children", []):
        hot_list.append(post.get("data", {}).get("title"))
    after = data.get("after")
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list if hot_list else None
