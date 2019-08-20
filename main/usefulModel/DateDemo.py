from datetime import datetime, timedelta
import time
now = datetime.now()
print(now)

yesterday = now - timedelta(days=3)
DT = datetime.strftime(yesterday,'%Y%m%d')
print('DT',DT)
JOB_DATE = datetime.strptime(DT,'%Y%m%d').date()
print('jobDate',JOB_DATE)
dt = datetime(2015, 4, 19, 12, 20)
print(dt)

#转timestamp
print(dt.timestamp())

t = 1429417200.0
print(datetime.fromtimestamp(t))

#判断今天周几
anyday=yesterday.strftime("%w")
print(anyday)