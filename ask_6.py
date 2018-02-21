import datetime
from datetime import date

date_input=raw_input('\n\n\nType month and year (mm/yyyy):\n\n\t')
while ('/' not in date_input) and ('-' not in date_input) and ('.' not in date_input) and (len(date_input) > 2):
	print '\nWrong input, try again'
	date_input=raw_input('\n\nType month and year (mm/yyyy):\n\n\t')
if '-' in date_input:
	month, year=date_input.split('-')
elif '/' in date_input:
	month, year=date_input.split('/')
elif '.' in date_input:
	month, year=date_input.split('.')
elif len(date_input) < 3:
	month=date_input
	date_input=raw_input('Month accepted. Type in year:\n\n\t')
	year=date_input
month=int(month)
year=int(year)
mia_kyriakh=date(2018, 1, 7)
first_day=date(year, int(month), 1)
day_span=first_day - mia_kyriakh
day_span=day_span.days%7
max_date=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if year%400==0 or (year%4==0 and year%100!=0):
	max_date[2]=29 #disekto etos
week=[' ',' ',' ',' ',' ',' ',' ']
break1=0
for x in xrange(day_span, 7):
	week[x]=x-day_span+1
print '\n\n\n\n\n\n\t\tS\tM\tT\tW\tT\tF\tS\n\n'
for x in xrange(6):
	print '\n\t\t'+str(week[0])+'\t'+str(week[1])+'\t'+str(week[2])+'\t'+str(week[3])+'\t'+str(week[4])+'\t'+str(week[5])+'\t'+str(week[6])
	if break1==1:
		break
	for i in xrange(7):
		if i==0:
			week[0]=int(week[6])+1
		else:
			week[i]=week[i-1]+1
		if int(week[i])>max_date[month-1]:
			week[i]=' '
			for j in xrange(i,7):
				week[j]=' '
			break1=1
			break
print '\n\n\n'