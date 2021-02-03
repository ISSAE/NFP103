#Spawn (fork) a Process – Process Based Parallelism
import multiprocessing
import os

def my_Func(i):
    print (f'---> Appel avec {i} pid={os.getpid()}')
    for j in range (0,i):
        print(f'> Dans myFunc({i}) :{j}')
    print (f'<--- Fin {i}')
    return

def main():
    process = []
    for i in range(10):
        t = multiprocessing.Process( \
            target=my_Func, args=(i,))
        process.append(t)
        t.start()
    for t in process:
        t.join()

if __name__ == '__main__':
    main()