#!/usr/bin/python

"""
Evan Widloski - 2015-10-28 - minutes_today
Returns how many minutes have I used my laptop today
"""

from datetime import datetime
import getopt, sys

with open(sys.argv[1],'r') as f:
    data = [line.split() for line in f.readlines()]


sum = 0
for line in data:
    if len(line) >= 1:
        topen = datetime.strptime(line[0],'%Y-%m-%d_%H:%M')

    if topen.date() == datetime.now().date():
        if len(line) >= 2:
            tclose = datetime.strptime(line[1],'%Y-%m-%d_%H:%M')

            tdiff = tclose - topen
            mins = tdiff.seconds / 60 #how many minutes lid was open
            sum += mins

        elif line == data[-1]:
            tdiff = datetime.now() - topen
            mins = tdiff.seconds / 60 #how many minutes lid was open
            sum += mins

print "{0} hours, {1} minutes".format(sum / 60, sum % 60)
