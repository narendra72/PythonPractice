import multiprocessing
import time

'''
def square(n):
    time.sleep(2)
    print(f" square of {n} is {n*n}")

start = time.time()
square(4)
square(5)
end = time.time()
print("Time: ", end - start)

'''

def square(n):
  time.sleep(2)
  print(f" square of {n} is {n*n}")

if __name__ == "__main__":
  start = time.time()

  p1 = multiprocessing.Process(target=square, args=(4,))
  p2 = multiprocessing.Process(target=square, args=(5,))

  p1.start()
  p2.start()

  p1.join()
  p2.join()
  end = time.time()
  print("Time:", end - start)