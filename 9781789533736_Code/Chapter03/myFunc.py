import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def myFunc(i):
    print (f'calling myFunc from process n°: {i}')
    info(f'p{i}')
    for j in range (0,i):
        print(f'output from myFunc_{i} is :{j}')
    return
