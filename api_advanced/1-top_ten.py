#!/usr/bin/python3
"""
1-top_ten
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit

    If the subreddit is invalid, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "top-ten-subreddit-titles"}

    try:
        response = requests.get(url, headers=headers, params={"limit": 10}, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data", {}).get("children", [])
            if data:
                for post in data:
                    print(post["data"].get("title"))
            else:
                print("None")
        else:
            print("None")
    except requests.RequestException:
        print("None")

