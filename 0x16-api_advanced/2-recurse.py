#!/usr/bin/python3
"""This script queries the reddit api for a given subreddit"""

import requests


def recurse(subreddit, hot_list=[]):
    """recursively queries a subreddit for all hot topics"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64;\
                rv:109.0) Gecko/20100101 Firefox/118.0'}

    def get_more_posts(after):
        if after is None:
            return hot_list
        res = requests.get(url, headers=headers, params={'after': after})
        data = res.json().get('data', {})
        posts = data.get('children', None)
        if posts is None:
            return None
        for post in posts:
            hot_list.append(post.get('data', {}).get('title'))
        after = data.get('after')
        return get_more_posts(after)

    res = requests.get(url, headers=headers)
    data = res.json().get('data', {})
    posts = data.get('children', None)
    if posts is None:
        return None
    for post in posts:
        hot_list.append(post.get('data', {}).get('title'))
    after = data.get('after')
    return get_more_posts(after)
