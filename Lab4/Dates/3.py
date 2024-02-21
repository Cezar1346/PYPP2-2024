import datetime

today = datetime.datetime.now()
today1 = today.replace(microsecond = 0)

print(today1)