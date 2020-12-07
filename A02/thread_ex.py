import time

# une procedure qui perd du temps!
def fonct(nom):
  print(nom)
  time.sleep(10)
  print("fin", nom)

def appel_fonc():
  debut = time.time()
  fonct("nfp103")
  fin = time.time()
  print(f'durée = {fin-debut}')

def pgm(lafonc):
  print("Avant appel")
  lafonc()
  print("Apres appel")

import threading
def th_appel_fonc():
  debut = time.time()
  # fonct("nfp103") Nous allons remplcer ceci par
  t = threading.Thread(target=fonct, args=['utc503 avec th'])
  t.start()
  fin = time.time()
  print(f'durée = {fin-debut}')

# print("Sans thread .... ")
# pgm(appel_fonc)

print("avec Thread")
pgm(th_appel_fonc)