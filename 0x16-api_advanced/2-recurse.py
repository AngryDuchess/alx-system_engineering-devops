#!/usr/bin/python3
"""
queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """
    function that queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit. 
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if after:
        url = url + '?after={}'.format(after)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    params = {'after': after, 'count': count, 'limit': 100}
    if response.status_code != 200:
        return None
    after = response.json().get('data').get('after')
    count = response.json().get('data').get('count')
    for children in response.json().get('data').get('children'):
        hot_list.append(children.get('data').get('title'))
    if after:
        return recurse(subreddit, hot_list, after, count)
    else:
        return hot_list
