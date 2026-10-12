# API advanced

Python scripts that query the [Reddit API](https://www.reddit.com/dev/api/)
using the `requests` module, with a custom `User-Agent` and redirects disabled.

| File | Description |
|---|---|
| `0-subs.py` | `number_of_subscribers(subreddit)` returns the total subscriber count, or `0` if invalid |
| `1-top_ten.py` | `top_ten(subreddit)` prints the titles of the first 10 hot posts, or `None` |
| `2-recurse.py` | `recurse(subreddit)` recursively walks pagination and returns all hot titles (or `None`) |
| `3-count.py` | `count_words(subreddit, word_list)` recursively counts keyword occurrences in hot titles and prints them sorted |

## Usage

```bash
./0-subs.py            # via a main that imports number_of_subscribers
python3 0-main.py programming
```
