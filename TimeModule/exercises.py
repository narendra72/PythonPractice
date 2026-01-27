# 1. Simple Countdown Program

import time

for i in range(5,0,-1):
  print(i)
  # time.sleep(1)

print("Done💡")


# 2. Execution Time

start = time.time()

for i in range(5000):
  print(i)

end = time.time()

print("Execution time: ", end - start)
