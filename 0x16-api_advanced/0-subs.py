#!/usr/bin/python3
""" function to find a subredict """
import requests


def number_of_subscribers(subreddit):
    """ function to find a subredict """
    url = "https://www.reddit.com/api/search_subreddits.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    data = {"query": subreddit, "exact": True}
    response = requests.post(url, headers=headers,
                             data=data, allow_redirects=False)
    if response.status_code == 200:
        results = response.json()
        return results['subreddits'][0]['subscriber_count']
    else:
        return 0
