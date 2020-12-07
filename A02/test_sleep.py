from time import *
import os

if (os.name == 'nt'):
    from ctypes import windll #new
    print('nt!')
    timeBeginPeriod = windll.winmm.timeBeginPeriod #new
    timeBeginPeriod(1) #new

debut = time_ns()
sleep(0.000000001)
fin = time_ns()
print(f"temps écoulé en nanosecondes= {fin-debut} en seconde {(fin-debut)*1e-9}")