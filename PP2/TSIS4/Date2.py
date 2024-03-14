import datetime
#ex1
current_date= datetime.datetime.now()
print(current_date.day-5)

#ex2
from datetime import datetime, timedelta
today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)
#ex3 
current_datetime = datetime.now()
current_datetime_without_microseconds = current_datetime.replace(microsecond=0)
print(current_datetime_without_microseconds)
#ex4 
from datetime import datetime, time
def date_diff_in_Seconds(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds

date1 = datetime.strptime('2015-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')

date2 = datetime.now()
print("\n%d seconds" %(date_diff_in_Seconds(date2, date1)))
print()