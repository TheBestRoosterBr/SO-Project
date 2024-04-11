import threading

class BarbeiroDorminhoco:
    def __init__(self):
        self.lock = threading.Lock()
        self.cliente_esperando = False

    def barbeiro(self):
        while True:
            with self.lock:
                if not self.cliente_esperando:
                    print("Barbeiro está dormindo")
                else:
                    print("Barbeiro está cortando o cabelo")
                    self.cliente_esperando = False

    def cliente(self):
        with self.lock:
            self.cliente_esperando = True
            print("Cliente está esperando pelo barbeiro")

if __name__ == "__main__":
    bd = BarbeiroDorminhoco()
    barbeiro_thread = threading.Thread(target=bd.barbeiro)
    cliente_thread = threading.Thread(target=bd.cliente)

    barbeiro_thread.start()
    cliente_thread.start()

    barbeiro_thread.join()
    cliente_thread.join()
