import datetime
from datetime import date

mia_kyriakh=date(2018, 1, 7)
today=datetime.date.today()
today2=str(today)
year, month, day_no=today2.split('-')
year=int(year)
month=int(month)
day_no=int(day_no)

day_span=today - mia_kyriakh
day_span=day_span.days%7

day_names = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
max_date = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if year%4==0:
	max_date['02']='29'

print "\n\n\n\n\n\n\n\n\n\tToday the date is " + str(day_no) + '/' + str(month) + '/' + str(year) + ", it's a " + day_names[day_span]
c=0
for j in xrange(month, 13):
	if day_no<=max_date[j]:
		date1=date(year, j, day_no)
		date_span=date1 - mia_kyriakh
		date_span=date_span.days%7
		if date_span==day_span:
			c+=1
for i in xrange(year+1,year+10):
	for j in xrange(1,13):
		if day_no<=max_date[j]:
			date1=date(i, j, day_no)
			date_span=date1 - mia_kyriakh
			date_span=date_span.days%7
			if date_span==day_span:
				c+=1
for j in xrange(1, month+1):
	if day_no<=max_date[j]:
		date1=date(year+10, j, day_no)
		date_span=date1 - mia_kyriakh
		date_span=date_span.days%7
		if date_span==day_span:
			c+=1
print '\tand there will be ' + str(c) + ' more ' + day_names[day_span] + 's on the ' + str(day_no) + 'th\n\tof any month in the next 10 years.\n\n\n\n\n\n\n\n'