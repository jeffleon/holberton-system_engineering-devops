#!/usr/bin/python3
""" function that allow do a request in reddit to obtein titles"""
import requests


def top_ten(subreddit):
    """ function that allow do a request in reddit to obtein titles """
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        results = response.json()
        for result in results["data"]["children"]:
            print(result['data']['title'])
    else:
        print(None)
