#!/usr/bin/python3
"""Recursively count keywords in a subreddit's hot post titles."""
import requests


def count_words(subreddit, word_list, counts={}, after=None):
    """Print keyword counts from hot titles, sorted by count then word."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting"}
    params = {"after": after} if after else {}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json().get("data", {})
    for post in data.get("children", []):
        title = post.get("data", {}).get("title", "").lower()
        for word in title.split():
            for keyword in word_list:
                if word == keyword.lower():
                    key = keyword.lower()
                    counts[key] = counts.get(key, 0) + 1
    after = data.get("after")
    if after:
        return count_words(subreddit, word_list, counts, after)
    for word, total in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
        print("{}: {}".format(word, total))
