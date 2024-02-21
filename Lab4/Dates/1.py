import datetime

today = datetime.datetime.now()
fivedaysbefore = today - datetime.timedelta(days = 5)

print(fivedaysbefore)