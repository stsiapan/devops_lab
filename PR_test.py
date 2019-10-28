#!/usr/bin/env python

import argparse
import getpass
import requests

link = 'https://api.github.com/repos/'

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-n', '--name', nargs='+', help='return input values')
parser.add_argument('-u', '--userID', nargs='+', help='used to enter repository user')
parser.add_argument('-r', '--repository', nargs='+', help='used to enter repository name')
parser.add_argument('-a', '--admin', nargs='+', help='must be a GIT nickname')
args = parser.parse_args()

username = args.admin[0]
password = getpass.getpass()

r = requests.get(link + args.userID[0] + '/' + args.repository[0] +
                 '/' + 'pulls', auth=(username, password)).json()

for i in args.name:
    if 'number' in i:
        print('amount of requests = {}'.format(r[0]['number']))
        continue
    if 'updated' in i:
        print('last updated = {}'.format(r[0]['updated_at']))
        continue
    if 'full' in i:
        print('full name of last PR user = {}'.format(r[0]['head']['repo']['full_name']))
        continue
    else:
        print('one or more invalid argument')
