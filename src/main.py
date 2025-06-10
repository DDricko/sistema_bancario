from models.conta import Conta
from models.usuario import Usuario

def exibir_menu():
    menu = """
    [d] - Depositar
    [s] - Sacar
    [e] - Extrato
    [q] - Sair

    => """

    opcao = input(menu)
    return opcao

def main():

    usuario_autenticado = Usuario.autenticar_usuario()

    if not usuario_autenticado:
        print("Autenticação falhou. Encerrando o programa")
        return 
    
    conta = Conta()

    while True:
        opcao = exibir_menu() 

        if opcao == "d":
            try:
                valor = float(input("Informe o valor do depósito: "))
                conta.depositar(valor)
            except ValueError:
                print("O valor informado é inválido. Certifique-se de digitar um número válido.")

        elif opcao == "s":
            try:
                valor = float(input("Informe o valor do saque: "))
                conta.sacar(valor)
            except ValueError:
                print("O valor informado é inválido. Certifique-se de digitar um número válido.")

        elif opcao == "e":
            conta.exibir_extrato()

        elif opcao == "q":
            print("Programa encerrado. Até mais!")
            break
        
if __name__ == "__main__":
    main()