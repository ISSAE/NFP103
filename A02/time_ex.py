# vérifions leur effet et leur utilisation
import time
# pour utiliser un module en Python faut utiliser import (cf cours UTC503)
debut = time.time()
s = 0
i = 1000000
while (i):
  s += i
  i -= 1
fin = time.time()
print(f"temps écoulé en secondes= {fin-debut}")