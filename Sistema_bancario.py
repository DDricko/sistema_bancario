from datetime import datetime




def exibir_menu():
    menu = """
    [d] - Depositar
    [s] - Sacar
    [e] - Extrato
    [q] - Sair

    => """

    opcao = input(menu)
    return opcao

def depositar(saldo, extrato, valor):
    if valor > 0:
        saldo += valor
        extrato += f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Depósito: R$ {valor:.2f}\n"
        return saldo, extrato
    else:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato
    
def sacar(valor, saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato, numero_saques

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        saldo -= valor
        extrato += f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato, LIMITE_SAQUES, numero_saques): 
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print(f"Você ainda pode realizar {LIMITE_SAQUES - numero_saques} saque(s) hoje.")
    print("==========================================")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = exibir_menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, extrato, valor)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(valor, saldo, extrato, numero_saques, limite, LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo, extrato, LIMITE_SAQUES, numero_saques)

        elif opcao == "q":
            print("Programa encerrado. Até mais!")
            break
main()
