#!/usr/bin/python3
"""
API Advanced
"""

import json
import requests


def top_ten(subreddit):
    """
    queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {'User-Agent': 'Mozilla/5.0'}

    params = {'limit': 10}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:

        results = response.json()
        for index in results['data']['children']:
            print(index['data']['title'])

    else:
        print(None)
