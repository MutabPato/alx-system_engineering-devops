#!/usr/bin/python3
"""
API Advanced
"""

import json
import requests


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns the number of subscribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {'User-Agent': 'Mozilla/5.0'}

    params {'limit': 10}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:

        results = response.json()
        for index in results['data']['children']:
            print index['data']['title']

    else:
        return None
