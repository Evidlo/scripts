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
    #could this possibly be a valid entry?
    if len(line) >= 1:
        topen = datetime.strptime(line[0],'%Y-%m-%d_%H:%M')
        #if there's 2, get topen and tclose
        if len(line) >= 2:
            tclose = datetime.strptime(line[1],'%Y-%m-%d_%H:%M')
        #if it's the last line in the log, set tclose to now
        elif line == data[-1]:
            tclose = datetime.now()

        #check that either topen or tclose is today 
        #if topen not today, set topen to midnight
        if tclose.date() == datetime.now().date():
            if topen.date() != datetime.now().date():
                topen = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

            tdiff = tclose - topen
            mins = tdiff.seconds / 60 #how many minutes lid was open
            sum += mins

print "{0} hours, {1} minutes".format(sum / 60, sum % 60)
