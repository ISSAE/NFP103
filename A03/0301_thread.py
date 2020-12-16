import random
import sys
import threading
from threading import Thread, RLock
import time

verrou = RLock()

class Afficheur2(Thread):

    """Thread chargé simplement d'afficher un mot dans la console."""


    def __init__(self, mot):
        Thread.__init__(self)
        self.mot = mot

    def run(self):
        dlocal = threading.local()
        dlocal.x = self.mot
        """Code à exécuter pendant l'exécution du thread."""
        i = 0
        print("dans le run",threading.current_thread(), dlocal.x)
        while i < 5:
            with verrou:
                for lettre in self.mot:
                    sys.stdout.write(lettre)
                    sys.stdout.flush()
                    attente = 0.1
                    # attente += random.randint(1, 60) / 100
                    time.sleep(attente)
            i += 1


# Création des threads
thread_1 = Afficheur2("canard")
thread_2 = Afficheur2("TORTUE")

# Lancement des threads
thread_1.start()
thread_2.start()

# Attend que les threads se terminent
thread_1.join()
thread_2.join()
