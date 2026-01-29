# wihout walrus operstor

n = len("Narendra")
if n>5:
  print(n)

# with walrus operstor

if (n := len("Narendra")) > 5:
  print(n)


a = True
print(a := False)