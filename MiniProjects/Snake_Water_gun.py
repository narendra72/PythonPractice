import random
# User input:
# 0 -> Snake
# 1 -> Gun
# 2 -> Water
user = int(input("Enter 0 For Snake 1 for Gun 2 for Water:\n"))
computer = random.randint(0,2)
print("user ",user)
print("computer", computer)

def check(user, computer):
  if(user == computer):
    return 0

  if(user == 0 and computer == 1):
    return -1

  if(user == 1 and computer == 2):
    return -1

  if(user == 2 and computer == 0):
    return -1

  return 1
   
result = check(user, computer)

if(result ==0):
  print("Draw")
elif(result==-1):
  print("Computer won")
else:
  print("You Won")
    
   




