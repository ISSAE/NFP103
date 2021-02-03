import multiprocessing
import time

def foo():
    name = multiprocessing.current_process().name
    print (f"Debut de  {name}")
    if name == 'background_process':
        for i in range(0,5):
            print(f'---> {i}')
        time.sleep(1)
    else:
        for i in range(5,10):
            print(f'---> {i}')
        time.sleep(1)
    print (f"Fin de {name}")
    

if __name__ == '__main__':
    background_process = multiprocessing.Process\
                         (name='background_process',\
                          target=foo)
    background_process.daemon = False

    NO_background_process = multiprocessing.Process\
                            (name='NO_background_process',\
                             target=foo)
    
    NO_background_process.daemon = True
    
    background_process.start()

    NO_background_process.start()
    

