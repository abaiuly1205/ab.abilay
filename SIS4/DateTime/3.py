from datetime import datetime

d = datetime.now()
dwms = d.replace(microsecond=0)
print("Original Datetime:", d)
print("Datetime without microseconds:", dwms)