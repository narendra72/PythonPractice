print("ElseInLoop")

for i in range(5):
  print(i)

else:
  print("Loop completelly run")

for i in range(5):
  print(i)
  if(i==3):
    break

else:
  print("Loop completelly run")