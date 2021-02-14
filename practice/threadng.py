import time
import threading

start = time.perf_counter()

def do_something(seconds):
    print(f"sleeping for {seconds} second(s)..")
    time.sleep(seconds)
    print("done sleeping")

# do_something()
# do_something()
# do_something()
# entire code will run for 3 seconds if done like this

# t1=threading.Thread(target=do_something)
# t2=threading.Thread(target=do_something)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# end = time.perf_counter()
#-----------------------------------------------------------
# sleeping for 1 second..
# sleeping for 1 second..
# done sleeping
# done sleeping
#  time taken for entire program to run : 1.002

threads = []

for _ in range(10):
    t1=threading.Thread(target=do_something,args=[1.5])
    t1.start()
    threads.append(t1)

for m in threads:
    m.join()

end = time.perf_counter()

print(f" time taken for entire program to run : {round(end-start,3)}")
