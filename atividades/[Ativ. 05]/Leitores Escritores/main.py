import threading

class LeitorEscritor:
    def __init__(self):
        self.lock_leitura = threading.Lock()
        self.lock_escrita = threading.Lock()
        self.leitores = 0

    def leitor(self):
        with self.lock_leitura:
            self.leitores += 1
            if self.leitores == 1:
                self.lock_escrita.acquire()

        print("Leitor está lendo")

        with self.lock_leitura:
            self.leitores -= 1
            if self.leitores == 0:
                self.lock_escrita.release()

    def escritor(self):
        with self.lock_escrita:
            print("Escritor está escrevendo")

if __name__ == "__main__":
    le_es = LeitorEscritor()
    leitores_threads = [threading.Thread(target=le_es.leitor) for _ in range(5)]
    escritor_thread = threading.Thread(target=le_es.escritor)

    for leitor_thread in leitores_threads:
        leitor_thread.start()

    escritor_thread.start()

    for leitor_thread in leitores_threads:
        leitor_thread.join()

    escritor_thread.join()
