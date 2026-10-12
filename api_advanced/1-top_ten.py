#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts of a given subreddit."""
import requests


def top_ten(subreddit):
    """Prints the first 10 hot post titles, or None if the subreddit is bad."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "PostmanRuntime/7.35.0"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        posts = response.json().get("data").get("children")
        for post in posts:
            print(post.get("data").get("title"))
    except Exception:
        print(None)
