import datetime
yester = datetime.datetime(2007, 8, 2, 8,0,0,0)
print(yester)
now=datetime.datetime.now()
print(now)
delta=now-yester
print(delta)
after=now+datetime.timedelta(days=2)
print(after)
print(delta.total_seconds())
import time
lst=[]
for i in range(5):
    lst.append(datetime.datetime.now())
    time.sleep(2)

for i in lst:
    print(i)


