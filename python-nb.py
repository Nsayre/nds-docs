# Python snippets

# Data Sourcing

# CSV

import csv

with open('data/addresses.csv') as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    for row in reader:
        # row is a `list`
        print(row)

# API

# requests package is "HTTP for Humans"
import requests

url = 'https://api.github.com/users/ssaunier'
response = requests.get(url).json()

print(response['name'])

# SQL

# SQL in Python

import sqlite3

conn = sqlite3.connect('data/soccer.sqlite')
c = conn.cursor()
c.execute("SELECT * FROM Country")
rows = c.fetchall()
rows
