import threading
import time


class Compte:

    def __init__(self):
        self.balance = 100  # DonnÃ©e partagÃ©e
    
    def maj(self, transaction, montant):
        print(f'{transaction} thread maj...{montant}')
        local_copy = self.balance
        local_copy += montant
        time.sleep(1)
        self.balance = local_copy
        print(f'{transaction} thread fin...')


if __name__ == '__main__':
    compte = Compte()
    th = []
    print(f'balance début {compte.balance}')
    for transaction, montant in [('depot', 50), ('retrait', -150)]:
        # t = threading.Thread(target=compte.maj,args=[transaction, montant])
        # t.start()
        # th.append(t)
        compte.maj(transaction, montant)
    # for t in th:
        # t.join()
    print(f'balance de fin {compte.balance}')
