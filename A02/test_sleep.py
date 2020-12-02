from time import *
debut = time_ns()
sleep(0.01)
fin = time_ns()
print(f"temps écoulé en nanosecondes= {fin-debut} en seconde {(fin-debut)*1e-9}")