#!/usr/bin/python3
"""This script queries the reddit api for a given subreddit"""

import requests
after = None


def count_words(subreddit, word_list=[]):
    """recursively queries a subreddit for all hot topics"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'the_ethan_hunt'}
    global after
    params = {'after': after}

    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    data = res.json().get('data', {})
    posts = data.get('children', None)
    if posts is None:
        return None
    for post in posts:
        word_list.append(post.get('data', {}).get('title'))
    after = data.get('after')
    if after is None:
        return word_list
    return count_words(subreddit, word_list)
