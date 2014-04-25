#!/usr/bin/python

"""
Evan Widloski - 2014-04-08 - Usage Log Parser m.II
Parses logs created by some acpi scripts and displays them in a more usable format

Functions:

	minuteHist():
		calculates the total minutes the laptop was on for each hour of the day. Returns a 24
		element list representing minutes

"""

from datetime import datetime
import getopt, sys

def readFile(file_str):
	lines = []
	f = open(file_str,'r')

	line = 1
	while line:
		line = f.readline().split() #split by whitespace

		if len(line) == 2: #only add lines with 2 entries
			lines.append(line)
	return(lines)

def usage():
	print "usage: usagelog_parser <output arg> [input file]"
	print "       Output args:"
	print "            --hist :: a histogram of the total minutes in each our of the day"


def minuteHist(data):
	mins_hist = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

	for line in data:

#read in lid open and close time
		topen = datetime.strptime(line[0],'%Y-%m-%d_%H:%M')
		tclose = datetime.strptime(line[1],'%Y-%m-%d_%H:%M')
		
#if the object exists, then the data was valid 
		if topen and tclose:
			hopen = int(datetime.strftime(topen,'%H')) #hour that lid was opened (0 based)
			mopen = int(datetime.strftime(topen,'%M')) #min that lid was opened (0 based)

			tdiff = tclose - topen
			mins = tdiff.seconds / 60 #how many minutes lid was open
			hours = mins / 60	#how many hours lid was open
			hclose = (hopen + hours) % 24 #hour that lid was opened (0 based)

#add first and hours to mins_hist
			if mins < 60:
				mins_hist[hopen] += mins
			else:
				mins_hist[hopen] += 60 - mopen
				mins_hist[hclose] += (mins + mopen) % 60

#for each whole hour, add 60 to mins_hist
			for h in range(hopen + 1,hopen + hours):
				mins_hist[h % 24] += 60
	for h in mins_hist:
		print h,


if __name__ == '__main__':
	try:
		opts, args = getopt.getopt(sys.argv[1:], 'h',['hist'])
	except getopt.GetoptError as error:
		print str(error)
		usage()
		sys.exit()

	for opt in opts:
		if '-h' == opt[0]:
			usage()
		if '--hist' == opt[0]:
			if len(args) > 0:
				for f_str in args:
					minuteHist(readFile(args[0]))
			else:
				usage()

