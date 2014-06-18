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
	try:
		f = open(file_str,'r')
	except IOError:
		print 'File not found!'
		sys.exit()

	line = 1
	while line:
		line = f.readline().split() #split by whitespace

		if len(line) == 2: #only add lines with 2 entries
			lines.append(line)
	return(lines)

def usage():
	print "usage: usagelog_parser <args> <input file>"
	print "Output args:"
	print "  --mins :: a histogram of the total minutes in each our of the day"
	print "  --days :: a histogram of the total minutes in each day of the week"
	print "  --log  :: print out the full log, with each line representing"
	print "            the hourly usage for one day"


#converts a single record into a list of minutes used each hour
def convertRecord(line):
	days= []

	mins_hist = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#read in lid open and close time
	topen = datetime.strptime(line[0],'%Y-%m-%d_%H:%M')
	tclose = datetime.strptime(line[1],'%Y-%m-%d_%H:%M')
	
#if the object exists, then the data was valid 
	if topen and tclose:
		mins_hist[24] = topen.replace(hour=0,minute=0) 
		hopen = int(datetime.strftime(topen,'%H')) #hour that lid was opened (0 based)
		mopen = int(datetime.strftime(topen,'%M')) #min that lid was opened (0 based)
		hclose = int(datetime.strftime(tclose,'%H')) #hour that lid was opened (0 based)

		tdiff = tclose - topen
		mins = tdiff.seconds / 60 #how many minutes lid was open
		hours = mins / 60	#how many hours lid was open

	if hopen + hours < 24: #if lid was opened and close in the same day
		if mopen + mins < 60: #if lid was opened and closed in the same hour
			mins_hist[hopen] = mins
		else:
			mins_hist[hopen] = 60 - mopen
			mins_hist[hclose] = (mins + mopen) % 60
		for h in range(hopen + 1,hopen + hours): #for each whole hour, add 60 to mins_hist
			mins_hist[h] = 60
		days.append(mins_hist)
	else:
		mins_hist[hopen] = 60 - mopen
		for h in range(hopen + 1,24):
			mins_hist[h] = 60
		days.append(mins_hist)
		a = tclose.replace(hour=0,minute=0).strftime('%Y-%m-%d_%H:%M')
		days += convertRecord([a,line[1]])

	return(days)

#returns a 2-dimensional list of the number of minutes in each hour of day for each day
def getMins(data):
	days = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,datetime(1,1,1)]]
	for line in data:
		record = convertRecord(line)
		for record_part in record:	
#if this record occured on the same day as a previous record (last element in 'days'
			if days[-1][-1] == record_part[24]:
#add values from new record into existing
				for hour in range(1,len(record_part) - 1):
					days[-1][hour] += record_part[hour]
			else:
				days.append(record_part)
	return(days[1:]) #dump first placeholder value

def avgMins(data):
	total = [0.0] * 24
	days = getMins(data)
	
	days_diff = datetime.strptime(data[len(data) - 1][0],'%Y-%m-%d_%H:%M') - datetime.strptime(data[0][0],'%Y-%m-%d_%H:%M')
	total_days = days_diff.days

	for day in days:
		total = [current + added for current,added in zip(total,day)]
	total = [val / total_days for val in total]	
	
	print "Log spans",total_days,"days"
	for mins in total:
		print mins,

def dumpLog(data):
	days = getMins(data)
	for day in days:
		for hour in day[:-1]:
			print hour,
		print day[-1].strftime('%Y-%m-%d')

def dayHist(data):
	weekdays = [[0.0] * 24] * 7
	num_entries = [0] * 7
	days = getMins(data)

	days_diff = datetime.strptime(data[len(data) - 1][0],'%Y-%m-%d_%H:%M') - datetime.strptime(data[0][0],'%Y-%m-%d_%H:%M')
	total_days = days_diff.days

	for day in days:
		weekday = int(day[-1].strftime('%w'))
		weekdays[weekday] = [current + added for current,added in zip(weekdays[weekday],day[:-1])]
		num_entries[weekday] +=1
	
	for weekday in range(0,len(weekdays)):
		for val in range(0,len(weekdays[weekday])):
			weekdays[weekday][val] /= num_entries[weekday] 
	
	for weekday in weekdays:
		for val in weekday:
			print val,
		print ''
			
		 


if __name__ == '__main__':
	try:
		opts, args = getopt.getopt(sys.argv[1:], 'h',['mins','days','log'])
	except getopt.GetoptError as error:
		print str(error)
		sys.exit()
	if len(args) < 1:
		usage()
		sys.exit()

	for opt in opts:
		if '-h' == opt[0]:
			usage()
		if '--mins' == opt[0]:
			for f_str in args:
				avgMins(readFile(f_str))
		if '--days' == opt[0]:
			for f_str in args:
				dayHist(readFile(f_str))
		if '--log' == opt[0]:
			for f_str in args:
				dumpLog(readFile(f_str))
