#!/usr/bin/python3
""" Prove API Rest"""
import csv
import requests
from sys import argv
 

if __name__ == "__main__":
    """ Print Tasks """
    Tasks = []
    CompleteTasks = []
    if len(argv) != 2:
        print("Command takes 2 arguments")
    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    res = requests.get(url)
    json = res.json()
    name = json['name']
    url2 = "https://jsonplaceholder.typicode.com/todos"
    req2 = requests.get(url2)
    json2 = req2.json()
    for usr in json2:
        if usr['userId'] == int(argv[1]):
            Tasks.append(usr)
    TasksDict = []
    for task in Tasks:
        TasksDict.append({'name': name,
                           'id': argv[1],
                           'completed': task['completed'],
                           'title': task['title']})
    with open('{}.csv'.format(argv[1]), mode='w') as fd:
        fnames = ['id', 'name', 'completed', 'title']
        writer = csv.DictWriter(fd, fieldnames=fnames, quotechar='"',
                                quoting=csv.QUOTE_ALL)
        for row in TasksDict:
            writer.writerow(row)