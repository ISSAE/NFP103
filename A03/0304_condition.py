import threading
import time
import logging


def consomateur(cv):
    print(f'consomateur thread started ...{threading.currentThread()}')
    with cv:
        print('consomateur waiting ...')
        cv.wait()
        print('consomateur consomme la resource')

def producteur(cv):
    print('producteur thread started ...{threading.currentThread()')
    with cv:
        print('Poduire la resource')
        print('Notifier à tous les consomateur')
        cv.notify()

if __name__ == '__main__':
    condition = threading.Condition()
    cs1 = threading.Thread(name='consomateur1', target=consomateur, args=(condition,))
    cs2 = threading.Thread(name='consomateur2', target=consomateur, args=(condition,))
    pd = threading.Thread(name='producteur', target=producteur, args=(condition,))

    cs1.start()
    time.sleep(2)
    cs2.start()
    time.sleep(2)
    pd.start()