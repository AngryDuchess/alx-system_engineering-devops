#!/usr/bin/python3
"""
queries the Reddit API and returns a list containing
the titles of all hot articles  and prints a sorted count
of given keywords (case-insensitive, delimited by spaces
"""
import requests


def count_words(subreddit, word_list, after=None, count=None):
    """
    function that queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.
    """
    words = [word.lower() for word in word_list]
    if count is None:
        count = {}
    url = 'https://www.reddit.com/r/{}/hot.json?limit=100'.format(subreddit)
    if after:
        url = url + '&after={}'.format(after)
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        if response.ok:
            data = response.json()
            children = data.get('data').get('children')
            if children:
                if len(children) == 0:
                    print(count)
                    return
                for word in words:
                    for title in [sub['data']['title'] for sub in children]:
                        if word in title:
                            if count.get(word):
                                count[word] += 1
                            else:
                                count[word] = 1
                if data.get('data').get('after'):
                    after = data['data']['after']
                    return count_words(subreddit, word_list, after, count)
                else:
                    # for k, v in count.items():
                    # print('{}: {}'.format(k, v))
                    print(count)
                    return
    except requests.exceptions.HTTPError:
        print(None)
