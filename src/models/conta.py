from datetime import datetime

class Conta:
    def __init__(self):
        self.saldo = 0.0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    def sacar(self, valor):
        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
            return

        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= self.LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        else:
            self.saldo -= valor
            self.extrato += f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Saque: R$ {valor:.2f}\n"
            self.numero_saques += 1
            print("Saque realizado com sucesso!")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print(f"Você ainda pode realizar {self.LIMITE_SAQUES - self.numero_saques} saque(s) hoje.")
        print("==========================================")    
