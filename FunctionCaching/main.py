from functools import lru_cache
import time

@lru_cache (maxsize = None)
def printfun(n):
  time.sleep(5)
  return 2*n

#  take 5 second to print
print(printfun(3))
print("Done for 3")

# print immediately
print(printfun(3))
print("Done for 3")

