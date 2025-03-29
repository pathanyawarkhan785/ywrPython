import time
import threading


def func(second):
    time.sleep(second)
    return second


# normal method

print(func(2))
print(func(4))
print(func(1))

# threading method

# record the start time using time.perf_counter().
# t1 = time.perf_counter()

# # create three threads, each targeting the func function with different sleep times.
# thread1 = threading.Thread(target=func, args=[2])
# thread2 = threading.Thread(target=func, args=[4])
# thread3 = threading.Thread(target=func, args=[1])

# # start the threads with thread1.start(), thread2.start(), and thread3.start().
# thread1.start()
# thread2.start()
# thread3.start()

# # wait for all threads to complete with thread1.join(), thread2.join(), and thread3.join().
# # if you don't write join output is very close to zero because it don't wait for process to copmplete instead they ran below line t2 = time.perf_counter() - t1
# thread1.join()
# thread2.join()
# thread3.join()

# # calculate the elapsed time and print it
# t2 = time.perf_counter() - t1
# print(t2)


# using concurrent.futures

from concurrent.futures import ThreadPoolExecutor

t1 = time.perf_counter()

with ThreadPoolExecutor() as executor:
    res = executor.map(func, [3, 2, 4])
    for i in res:
        print(i)

t2 = time.perf_counter() - t1
print(t2)
