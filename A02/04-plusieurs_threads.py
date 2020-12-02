import time
import threading 

def mafonc1(name):
    print(f'mafonc1 démarre {name}')
    time.sleep(10)
    print('mafonc1 terminée')

def mafonc2(name):
    print(f'mafonc2 démarre {name}')
    time.sleep(10)
    print('mafonc2 terminée')

def mafonc3(name):
    print(f'mafonc3 démarre {name}')
    time.sleep(10)
    print('mafonc3 terminée')

if __name__ == '__main__':
    print('main started')
    t1 = threading.Thread(target=mafonc1, args=['nfp103'])
    t1.start()
    t2 = threading.Thread(target=mafonc2, args=['titi'])
    t2.start()
    t3 = threading.Thread(target=mafonc3, args=['toto'])
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print('main terminée')