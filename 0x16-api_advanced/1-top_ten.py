#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first 10 hot posts
"""
import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles of the
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(None)
    if response.ok:
        children = response.json().get('data').get('children')
        if children:
            [print(sub['data']['title']) for sub in children]
        else:
            print(None)
