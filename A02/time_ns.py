# vérifions leur effet et leur utilisation
import time
# pour utiliser un module en Python faut utiliser import (cf cours UTC503)
debut = time.time_ns()
s = 0
i = 10000
while (i):
  s += i
  i -= 1
fin = time.time_ns()
print(f"temps écoulé en nanosecondes= {fin-debut} en seconde {(fin-debut)*1e-9}")