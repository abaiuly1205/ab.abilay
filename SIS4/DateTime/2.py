from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days = 1)
tomorrow = today + timedelta(days = 1)
print("Yesterday:", yesterday.strftime("%x"))
print("Today:", today.strftime("%x"))
print("Tomorrow:", tomorrow.strftime("%x"))