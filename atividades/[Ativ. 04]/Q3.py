'''
I. O código apresentado é um exemplo de uma simulação de transferência de dinheiro entre duas contas bancárias usando threads em Python. A ideia é que, ao final da execução, a conta conta1 tenha um saldo de 0 e a conta conta2 tenha um saldo de 100. Isso é feito através de 100 transferências de 1 unidade de dinheiro de conta1 para conta2.

II. O resultado após a execução do código pode variar devido à natureza concorrente das threads. Sem mecanismos de sincronização adequados, é possível que as operações de atualização do saldo das contas não sejam atômicas, levando a condições de corrida. Isso significa que o saldo final das contas pode não ser exatamente o esperado (100 para conta2 e 0 para conta1), devido a atualizações de saldo que são interrompidas por outras threads.

III. Os resultados podem não ser iguais ao executar o código várias vezes, principalmente devido à condição de corrida mencionada. Sem mecanismos de sincronização, o resultado pode variar a cada execução, dependendo da ordem em que as threads acessam e modificam os saldos das contas. Isso ocorre porque as operações de atualização do saldo não são atômicas e podem ser interrompidas por outras threads, levando a um estado inconsistente dos saldos.

IV. Para garantir que o saldo final das contas seja exatamente o esperado, podemos usar um objeto Lock para sincronizar o acesso às operações de atualização do saldo. Isso garante que apenas uma thread possa modificar o saldo de uma conta de cada vez, evitando condições de corrida.

V.
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

    def transferir(self, destino, valor):
        with self.lock:
            self.saldo -= valor
        with destino.lock:
            destino.saldo += valor

conta1 = ContaBancaria("conta1", 100)
conta2 = ContaBancaria("conta2", 0)

class ThreadTransferenciaEntreContas(threading.Thread):
    def __init__(self, origem, destino, valor):
        threading.Thread.__init__(self)
        self.origem = origem
        self.destino = destino
        self.valor = valor

    def run(self):
        self.origem.transferir(self.destino, self.valor)

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