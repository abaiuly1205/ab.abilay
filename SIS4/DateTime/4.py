from datetime import datetime

def difference_in_seconds(d1, d2):
    delta = d2 - d1
    return abs(delta.total_seconds())

date_format = "%Y-%m-%d %H:%M:%S"

date1 = input("Enter the first date(YYYY-MM-DD HH:MM:SS): ")
date2 = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")

d1 = datetime.strptime(date1, date_format)
d2 = datetime.strptime(date2, date_format)

s = difference_in_seconds(d1, d2)
print(s)