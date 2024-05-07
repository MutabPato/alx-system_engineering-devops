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
    url =f"https://www.reddit.com/dev/api/r/{subreddit}/about.json"

    headers = {'User-Agent': 'Pato/1.0'} 

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        about = response.json()
        return about['data']['subscribers']

    else:
        return 0
