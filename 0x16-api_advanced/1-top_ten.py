#!/usr/bin/python3
"""This script queries the reddit api for a given subreddit"""

import requests


def top_ten(subreddit):
    """Returns the top ten hot posts' titles of a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=9".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64;\
                rv:109.0) Gecko/20100101 Firefox/118.0'}
    res = requests.get(url, headers=headers, allow_redirects=False)
    posts = res.json().get('data', {}).get('children', None)
    if posts is None:
        print("None")
    else:
        for post in posts:
            print(post.get('data', {}).get('title'))
