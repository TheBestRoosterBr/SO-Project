import threading
import queue

class ProdutorConsumidor:
    def __init__(self, buffer_size):
        self.buffer = queue.Queue(buffer_size)
        self.lock = threading.Lock()

    def produtor(self):
        for i in range(10):
            with self.lock:
                if not self.buffer.full():
                    self.buffer.put(i)
                    print(f"Produtor produziu {i}")

    def consumidor(self):
        while True:
            with self.lock:
                if not self.buffer.empty():
                    item = self.buffer.get()
                    print(f"Consumidor consumiu {item}")

if __name__ == "__main__":
    pc = ProdutorConsumidor(5)
    produtor_thread = threading.Thread(target=pc.produtor)
    consumidor_thread = threading.Thread(target=pc.consumidor)
    produtor_thread.start()
    consumidor_thread.start()
    produtor_thread.join()
    consumidor_thread.join()
