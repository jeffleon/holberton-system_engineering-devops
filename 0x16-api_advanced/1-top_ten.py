#!/usr/bin/python
""" function that allow do a request in reddit to obtein titles"""
from sys import argv
import requests


def top_ten(subreddit):
    """ function that allow do a request in reddit to obtein titles """
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    try:
        response = requests.get(url, headers=headers)
        results = response.json()
        for result in results["data"]["children"]:
            print(result['data']['title'])
    except(e):
        print(None)
