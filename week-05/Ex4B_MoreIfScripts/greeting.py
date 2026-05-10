import datetime

hour = datetime.datetime.now().hour

if hour < 10:
    print("Good morning!")
elif hour > 10 and hour <17:
    print ("Good Day!")
elif hour > 23 and hour < 4:
    print("What are you doing up so late??")
else:
    print ("Good evening!")