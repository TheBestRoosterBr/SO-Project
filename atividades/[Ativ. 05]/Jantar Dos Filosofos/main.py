import threading

class Filosofo:
    def __init__(self, id, garfos):
        self.id = id
        self.garfos = garfos
        self.lock_esquerdo = threading.Lock()
        self.lock_direito = threading.Lock()

    def comer(self):
        with self.lock_esquerdo:
            with self.lock_direito:
                print(f"Filósofo {self.id} está comendo")

    def pensar(self):
        print(f"Filósofo {self.id} está pensando")

if __name__ == "__main__":
    garfos = [threading.Lock() for _ in range(5)]
    filosofos = [Filosofo(i, garfos) for i in range(5)]

    for i, filosofo in enumerate(filosofos):
        filosofo.lock_esquerdo = garfos[i]
        filosofo.lock_direito = garfos[(i + 1) % 5]

    threads = []
    for filosofo in filosofos:
        threads.append(threading.Thread(target=filosofo.comer))
        threads.append(threading.Thread(target=filosofo.pensar))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
