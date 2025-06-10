class Usuario:
    def __init__(self, cpf, nome, senha):
        self.cpf = cpf
        self.nome = nome
        self.senha = senha

    @staticmethod
    def autenticar_usuario():
        usuarios = [
            Usuario("12345678900", "Rodrigo", "123asd"),
            Usuario("11122233344", "Maria", "senha123"),
        ]

        LIMITE_TENTATIVAS = 3
        tentativas = 0

        while tentativas < LIMITE_TENTATIVAS:
            input_cpf = input("Informe o seu CPF: ")
            input_senha = input("Informe a sua senha: ")

            for usuario in usuarios:
                if usuario.cpf == input_cpf and usuario.senha == input_senha:
                    print(f"Autenticação realizada com sucesso. Bem-vindo(a), {usuario.nome}!")
                    return True

            tentativas += 1
            print("CPF ou senha inválidos.\n")

        print("Você excedeu o número máximo de tentativas.")
        return False
