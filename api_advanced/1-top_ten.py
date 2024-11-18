#!/usr/bin/python3
"""
A module to interact with the Reddit API and print the titles of the
first 10 hot posts for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid, it prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        res = requests.get(url, headers=headers, params={'limit': 10},
                           allow_redirects=False)
        if res.status_code != 200:
            print(None)
        else:
            posts = res.json().get('data', {}).get('children', [])
            for post in posts[:10]:  # Print only the first 10 titles
                print(post.get('data', {}).get('title'))
    except Exception:
        print(None)
