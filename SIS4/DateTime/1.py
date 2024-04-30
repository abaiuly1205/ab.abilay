from datetime import datetime, timedelta

d = datetime.now()
bes_kun_buryn = d - timedelta(days = 5)
print("Today:", d.strftime("%x"))
print("Five days ago:", bes_kun_buryn.strftime("%x"))