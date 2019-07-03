from datetime import datetime
now = datetime.now()
print(now)
dt = datetime(2015, 4, 19, 12, 20)
print(dt)

#转timestamp
print(dt.timestamp())

t = 1429417200.0
print(datetime.fromtimestamp(t))