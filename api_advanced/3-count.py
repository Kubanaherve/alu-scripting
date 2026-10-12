#!/usr/bin/python3
"""Recursively count keyword occurrences in a subreddit's hot titles."""
import requests

HEADERS = {"User-Agent": "linux:alu.api.advanced:v1.0 (by /u/kubanaherve)"}


def count_words(subreddit, word_list, counts=None, after=None):
    """Print a sorted, case-insensitive count of keywords in hot titles."""
    if counts is None:
        counts = {}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 100}
    if after is not None:
        params["after"] = after
    response = requests.get(url, headers=HEADERS, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json().get("data", {})
    for post in data.get("children", []):
        title = post.get("data", {}).get("title", "")
        for word in title.lower().split():
            for keyword in word_list:
                if word == keyword.lower():
                    key = keyword.lower()
                    counts[key] = counts.get(key, 0) + 1
    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, counts, after)
    ordered = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    for word, total in ordered:
        print("{}: {}".format(word, total))
