"""Python program to get Current Time
Get Current Date and Time using Python
Python | Find yesterday’s, today’s and tomorrow’s date
Python program to convert time from 12 hour to 24 hour format
Python program to find difference between current time and given time
Python Program to Create a Lap Timer
Convert date string to timestamp in Python
How to convert timestamp string to datetime object in Python?
Find number of times every day occurs in a Year"""

#Python program to get Current Time
from datetime import datetime
now = datetime.now()
print(now)
time = now.strftime('%H:%M:%S')
print(time)
time = datetime.now().time()
print(time)
date=datetime.now().date()
date = now.strftime('%D')
print(date)
date = now.strftime('%d-%m-%y')
print(date)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)




import time
now = time.localtime()
curr_time = time.strftime("%H:%M:%S", now)
print(curr_time)

import time
print("epoch time is", time.time())


# Find today a tomorrows time
from datetime import datetime, timedelta
now = datetime.now()
tomorrow = now+timedelta(1)
yesterday = now-timedelta(1)
print("yesterday", yesterday, "tomorrow", tomorrow)


from datetime import date, timedelta
import calendar
today = date.today()
yesterday=today-timedelta(1)
print(today)
print(yesterday)
print(yesterday.day)
print(calendar.day_name[yesterday.weekday()], yesterday.strftime('%d-%m-%y'))


#Python program to convert time from 12 hour to 24 hour format

from datetime import datetime
now = datetime.now()
time_24_format = time.strftime("%H:%M:%S")
time_24_format = str(time_24_format)
print(time_24_format)
time_obj = datetime.strptime(time_24_format, "%H:%M:%S")
print(time_obj.strftime("%I:%M:%S %p"))

#Difference between the times
from datetime import datetime
day, month, year, hours, minutes, seconds= '23','10','2022','10','30','45'

time1 = datetime.strptime(day+' '+month + ' '+year + ' '+hours + ' '+minutes + ' '+seconds, '%d %m %Y %H %M %S')
print(time1.strftime('%d %m %Y'))
print(time1.strftime('%d %m %y'))
print(time1.strftime('%d %m %y %I:%M:%S %p'))
day, month, year, hours, minutes, seconds= '24','10','2022','10','35','50'
time2 = datetime.strptime(day+' '+month + ' '+year + ' '+hours + ' '+minutes + ' '+seconds, '%d %m %Y %H %M %S')
print(time1.strftime('%d %m %Y'))
print(time1.strftime('%d %m %y'))
print(time1.strftime('%d %m %y %I:%M:%S %p'))
delta_t=time2-time1
print(delta_t.days)
print(delta_t.min)
print(delta_t.seconds)

# Convert date string to timestamp in Python
import time
import datetime
string = "20/01/2020"
time1 = datetime.datetime.strptime(string, '%d/%m/%Y')
print(time1.timetuple())
timestamp = time.mktime(time1.timetuple())
print(timestamp)
timestamp = datetime.datetime.timestamp(time1)
print(timestamp)



# python program Find number of
# times every day occurs in a Year 

from datetime import datetime
import calendar


days = ["Monday", "Tuesday", "Wednesday", "Thursday",  "Friday", "Saturday", "Sunday"  ]
L = [52 for i in range(7)]
Y = 2020

time_obj = datetime(year = Y, month = 1, day =1)
day = time_obj.strftime('%A')
for i in range(7):
    if day == days[i]:
        pos = i

if calendar.isleap(Y):
    L[pos]+=1
    L[(pos+1)%7]+=1
else:
    L[pos]+=1
    
print(L)

#Python Program to Create a Lap Timer

import time 
starttime = time.time()
lasttime = starttime
lapnum = 1

try: 
    while True: 
        input() 
        laptime = round((time.time() - lasttime), 2)
        totaltime = round((time.time() - starttime),2)
    
        print("laptime", laptime)
        print("lapnum", lapnum)
        print("totaltime", totaltime)
    
        lapnum+=1
        lasttime=time.time()
except KeyboardInterrupt:
	print("Done")
















