#!/usr/bin/python3
""" function to find a subredict """
from sys import argv
import requests


def number_of_subscribers(subreddit):
    """ function to find a subredict """
    url = "https://www.reddit.com/api/search_subreddits.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    data = {"query": subreddits}
    response = requests.post(url, headers=headers, data=data)
    try:
        results = response.json()
        print(results['subreddits'][0]['subscriber_count'])
    except(e):
        print(0)
