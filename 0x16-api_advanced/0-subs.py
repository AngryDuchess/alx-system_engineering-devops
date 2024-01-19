#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    gets the number of subscribers for the
    subreddit passed to the function
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.ok:
        data = response.json().get('data').get('subscribers')
        if data:
            return int(data)
        else:
            return 0
    else:
        return 0
