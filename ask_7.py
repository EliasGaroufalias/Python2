import datetime
from datetime import date

mia_kyriakh=date(2018, 1, 7)
today=datetime.date.today()
today2=str(today)
year, month, day_no=today2.split('-')
year=int(year)

day_span=today - mia_kyriakh
day_span=day_span.days%7

day_names = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
max_date = {1: '31', 2: '28', 3: '31', 4: '30', 5: '31', 6: '30', 7: '31', 8: '31', 9: '30', 10: '31', 11: '30', 12: '31'}
#todo: make this ^ thing a goddamn list, please. What were you thinking, me?
if year%4==0:
	max_date['02']='29'

print "\n\n\n\n\n\n\n\n\n\tToday the date is " + day_no + '/' + month + '/' + str(year) + ", it's a " + day_names[day_span]
c=0
for j in xrange(int(month), 13):
	if day_no<=max_date[j]:
		date1=date(year, j, int(day_no))
		date_span=date1 - mia_kyriakh
		date_span=date_span.days%7
		if date_span==day_span:
			c+=1
for i in xrange(year+1,year+10):
	for j in xrange(1,13):
		if day_no<=max_date[j]:
			date1=date(i, j, int(day_no))
			date_span=date1 - mia_kyriakh
			date_span=date_span.days%7
			if date_span==day_span:
				c+=1
for j in xrange(1, int(month)+1):
	if day_no<=max_date[j]:
		date1=date(year+10, j, int(day_no))
		date_span=date1 - mia_kyriakh
		date_span=date_span.days%7
		if date_span==day_span:
			c+=1
print '\tand there will be ' + str(c) + ' more ' + day_names[day_span] + 's on the ' + day_no + 'th\n\tof any month in the next 10 years.\n\n\n\n\n\n\n\n'