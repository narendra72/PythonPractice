import threading
import time

# without multithreading
'''
def square(n):
  time.sleep(4)
  print(f"square of {n} is" ,n * n)

start = time.time()
print(square(4))
print(square(5))
end = time.time()
print(end-start)
'''

# using threading

def square(n):
  time.sleep(4)
  print(f"square of {n} is" ,n * n)
  
start = time.time()

t1 = threading.Thread(target=square , args=(4,))
t2 = threading.Thread(target=square,  args=(5,))

t1.start()    # start a new theard and run code concurently not wait for to complete the task 
t2.start()

t1.join()    # wait til the t1 is not completed 
t2.join()

end = time.time()
print(end - start)


