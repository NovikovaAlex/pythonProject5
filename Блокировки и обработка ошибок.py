import threading
import time
import random



class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def  deposit(self):
            for i in range(100):
                rand_numb = random.randint(50, 500)
                self.balance += rand_numb
                print(f'Пополнение: {rand_numb}. Баланс: {self.balance}')
                if self.balance >= 500 and self.lock.locked() :
                    self.lock.release()
                time.sleep(0.001)

    def take(self):
        for i in range(100):
            rand_numb = random.randint(50, 500)
            print(f'Запрос на {rand_numb}' )
            if self.balance <= rand_numb:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
                time.sleep(0.001)
            else:
                self.balance -= rand_numb
                print(f'Снятие: {rand_numb}. Баланс: {self.balance}')
                time.sleep(0.001)





bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')
