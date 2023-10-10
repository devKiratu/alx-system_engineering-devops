#!/usr/bin/python3
"""This script queries the reddit api for subreddits data"""

import requests


def number_of_subscribers(subreddit):
    """gets the number of subscribers of the given `subreddit`"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64;\
                rv:109.0) Gecko/20100101 Firefox/118.0'}
    res = requests.get(url, headers=headers)
    data = res.json().get('data', {})
    subs = data.get('subscribers', 0)
    return subs
