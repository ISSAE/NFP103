#Thread Based Parallelism
import threading
import os

def my_Func(i):
    print (f'---> Appel avec {i} pid={os.getpid()}')
    for j in range (0,i):
        print(f'> Dans myFunc({i}) :{j}')
    print (f'<--- Fin {i}')
    return

def main():
    threads = []
    for i in range(10):
        t = threading.Thread( \
            target=my_Func, args=(i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

if __name__ == '__main__':
    main()