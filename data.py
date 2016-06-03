#!/usr/bin/python


import MySQLdb
import datetime
import csv


# open connection to database
# fill up with needed credentials

db = MySQLdb.connect(host="localhost", user="root", passwd="001831",
db="ProductHunt")



# Executing queries 
try:
	cursor = db.cursor() # cursor to manipulate database

# sql query
	cursor.execute("""
	select * from Posts;
	""")


#fetch | save the result
	rows = cursor.fetchall()
						# Mon, Tu, Wed, Th, Fri, Sat, Sun
	weekdays_count = 	[  0,  0,   0,  0,   0,   0,   0] #Posts
	votes_count 	= 	[  0,  0,   0,  0,   0,   0,   0] 
	comments_count = 	[  0,  0,   0,  0,   0,   0,   0] 




##########
#Processing data from database
##########


	for row in rows: 

	# Days of Week

		day_of_week = row[1].weekday()

		if day_of_week == 0:
			weekdays_count[0] += 1
			votes_count[0] += row[6]
			comments_count[0] += row[7]

		elif day_of_week == 1:
			weekdays_count[1] += 1
			votes_count[1] += row[6]
			comments_count[1] += row[7]

		elif day_of_week == 2:
			weekdays_count[2] += 1
			votes_count[2] += row[6]
			comments_count[2] += row[7]

		elif day_of_week == 3:
			weekdays_count[3] += 1
			votes_count[3] += row[6]
			comments_count[3] += row[7]

		elif day_of_week == 4:
			weekdays_count[4] += 1
			votes_count[4] += row[6]
			comments_count[4] += row[7]

		elif day_of_week == 5:
			weekdays_count[5] += 1
			votes_count[5] += row[6]
			comments_count[5] += row[7]

		elif day_of_week == 6:
			weekdays_count[6] += 1
			votes_count[6] += row[6]
			comments_count[6] += row[7]
	




##########
# Storing data in .csv file
##########			
	

	out = open('out.csv', 'w')
	for i in range(-1,7):
		if (i == -1):
			out.write('Day;')
			out.write('Posts;')
			out.write('Votes;')
			out.write('Comments')
			out.write('\n')

		else:
			#if i == 0:
			#	out.write('Monday;')
			#elif i == 1:
			#	out.write('Tuesday;')
			#elif i == 2:
			#	out.write('Wednesday;')
			#elif i == 3:
			#	out.write('Thursday;')
			#elif i == 4:
			#	out.write('Friday;')
			#elif i == 5:
			#	out.write('Saturday;')
			#elif i == 6:
			#	out.write('Sunday;')
			out.write('%d;' % i)
			out.write('%d;' % weekdays_count[i])
			out.write('%d;' % votes_count[i])
			out.write('%d;' % comments_count[i])
			out.write('\n')

	out.close()


##########
##########


#close database
finally:
	db.close()