'''Explicação do Código
O código apresentado simula uma transferência de dinheiro entre duas contas bancárias (conta1 e conta2) utilizando threads. Cada thread representa uma transferência de 1 unidade de dinheiro da conta1 para a conta2. O objetivo é garantir que, após todas as transferências, a conta1 tenha um saldo de 0 e a conta2 tenha um saldo de 100.

Resultado após Execução do Código
Após a execução do código, o saldo da conta1 será 0 e o saldo da conta2 será 100, como esperado. Isso ocorre porque cada thread deduz 1 do saldo da conta1 e adiciona 1 ao saldo da conta2. Como 100 transferências são realizadas, o saldo final da conta1 será 0 e o saldo final da conta2 será 100.

Execução do Código 10 Vezes
Executar o código 10 vezes resultará em saldo final da conta1 como 0 e saldo final da conta2 como 1000. Isso ocorre porque cada execução do código realiza 100 transferências, resultando em um aumento de 100 unidades no saldo da conta2 e uma diminuição de 100 unidades no saldo da conta1. Portanto, após 10 execuções, o saldo da conta1 será 0 e o saldo da conta2 será 1000.

Utilizando Mecanismos de Sincronização
Para garantir que ao final da execução do código conta2 possua saldo 100 e conta1 possua saldo 0, é necessário utilizar mecanismos de sincronização, como um Lock, para evitar condições de corrida. A condição de corrida ocorre quando duas ou mais threads acessam e modificam uma variável compartilhada simultaneamente, levando a resultados inesperados.

Aqui está o código modificado utilizando um Lock para sincronizar as transferências entre as contas:
'''
import threading
import time

class ContaBancaria():
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
        self.lock = threading.Lock()

    def __str__(self):
        return self.nome

conta1 = ContaBancaria("conta1", 100)
conta2 = ContaBancaria("conta2", 0)

class ThreadTransferenciaEntreContas(threading.Thread):
    def __init__(self, origem, destino, valor):
        threading.Thread.__init__(self)
        self.origem = origem
        self.destino = destino
        self.valor = valor

    def run(self):
        with self.origem.lock:
            origem_saldo_inicial = self.origem.saldo
            origem_saldo_inicial -= self.valor
            time.sleep(0.001)
            self.origem.saldo = origem_saldo_inicial

        with self.destino.lock:
            destino_saldo_inicial = self.destino.saldo
            destino_saldo_inicial += self.valor
            time.sleep(0.001)
            self.destino.saldo = destino_saldo_inicial

if __name__ == "__main__":
    threads = []
    for i in range(100):
        threads.append(ThreadTransferenciaEntreContas(conta1, conta2, 1))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print('Saldo da', conta1, ':', conta1.saldo)
    print('Saldo da', conta2, ':', conta2.saldo)