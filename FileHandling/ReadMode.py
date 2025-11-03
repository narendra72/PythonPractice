#  Read Mode 
file = open('myfile.txt','r')
text = file.read()
print(text)
file.close()

#  Read Line
f = open("myfile.txt", "r")
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
f.close()

print("Line 1: ", line1)
# print("Line 2: ", line2)
print("Line 3: ", line3)

#  Read Lines
f = open("myfile.txt", "r")
lines = f.readlines()
f.close()
print(lines)


#  Read Mode use with — it closes automatically file:

with open('myfile.txt','r') as file:
  text = file.read()
  print(text)

