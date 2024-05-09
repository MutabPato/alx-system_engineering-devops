#!/usr/bin/python3
"""
API Advanced
"""

import json
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    queries the Reddit API and returns a list  containing titles
    of all hot articles for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {'User-Agent': 'Mozilla/5.0'}

    params = {'limit': 2000}

    if after:
        params['after'] = after

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:

        results = response.json()
        posts = results['data']['children']

        if not posts:
            return hot_list

        for post in posts:
            hot_list.append(post['data']['title'])

        after = results['data']['after']

        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list

    else:
        return None
