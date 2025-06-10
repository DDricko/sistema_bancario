class Usuario:
    def __init__(self, cpf, nome, senha):
        self.cpf = cpf
        self.nome = nome
        self.senha = senha

    def autenticar_usuario(self):
        LIMITE_TENTATIVAS = 3
        tentativas = 0

        while tentativas < LIMITE_TENTATIVAS:
            print(f"\nTentativa {tentativas + 1} de {LIMITE_TENTATIVAS}")
            input_cpf = input("Informe o seu cpf: ")
            input_senha = input("Informe a sua senha: ")

            if input_cpf == self.cpf and input_senha == self.senha:
                print(f"\nBem-vindo, {self.nome}!")
                return True
            else:
                tentativas += 1
                print("Usuario ou senha inválidos")

        print("Você excedeu o limite maximo de tentativas")
        return False