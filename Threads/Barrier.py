#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num_coureurs = 3
finish_line = Barrier(num_coureurs)
coureurs = ['Pascal', 'Emile', 'Fares']

def coureur():
    name = coureurs.pop()
    sleep(randrange(2, 5))
    print(f'{name} a atteint la barière à: {ctime()}')
    finish_line.wait()

def main():
    threads = []
    print(f'Début de course!!!! à {ctime()}')
    for i in range(num_coureurs):
        threads.append(Thread(target=coureur))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Course términée!')

if __name__ == "__main__":
    main()
