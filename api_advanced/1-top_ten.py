#!/usr/bin/python3
"""
This module queries the Reddit API and prints the titles of the first
10 hot posts for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid or an error occurs, it prints 'OK'.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'My-User-Agent'}
    try:
        response = requests.get(url, headers=headers, params={'limit': 10},
                                allow_redirects=False)
        if response.status_code != 200:
            print("OK")
            return
        posts = response.json().get("data", {}).get("children", [])
        if not posts:
            print("OK")
            return
        for post in posts[:10]:
            print(post.get("data", {}).get("title", ""))
    except Exception:
        print("OK")
