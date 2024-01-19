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
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    for i in range(10):
        children = response.json().get('data').get('children')
        print(children[i].get('data').get('title'))
    # for i in range(10):
    #    print(response.json().get('data').get('children')[i].get('data').get('title'))
