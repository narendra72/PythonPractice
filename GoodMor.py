import time

t = time.strftime("%H:%M:%S")

currentTime = print(t)

h = int(time.strftime("%H"))

if h>=1 and h<12:
  print("Good Morning")
elif h>=12 and h<17:
  print("Good Afternood")
elif h>=17 and h<20:
  print("Good Evening")
else:
  print("Good Nigth")
