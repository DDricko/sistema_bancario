# Sistema Bancário

Bem-vindo ao Sistema Bancário! Este documento contém perguntas-chave para ajudá-lo a entender este projeto.

## 📋 Visão Geral do Projeto

### O que é este projeto?
Este é um sistema bancário simples desenvolvido em Python que simula operações básicas de uma conta bancária, incluindo depósitos, saques e consulta de extrato.

### Qual é o propósito principal?
Fornecer uma aplicação de linha de comando para gerenciar operações bancárias básicas com autenticação de usuário e controle de transações.

## 🏗️ Perguntas sobre Arquitetura

### Como o código está organizado?
O projeto possui duas implementações:
1. **Sistema_bancario.py** - Versão monolítica com todas as funcionalidades em um único arquivo (usa autenticação com usuário/senha simples: teste01/123asd)
2. **src/** - Versão modular organizada em:
   - `models/` - Classes de domínio (Conta, Usuario - onde a autenticação está implementada)
   - `services/` - Serviços auxiliares (contém autenticacao.py vazio, reservado para expansões futuras)
   - `main.py` - Ponto de entrada da aplicação modular

### Qual versão devo usar?
A versão modular em `src/` é a mais atual e recomendada, pois segue melhores práticas de organização de código.

### Quais são as principais classes e suas responsabilidades?
- **Conta** (`src/models/conta.py`): Gerencia o saldo, limites, extrato e operações financeiras
- **Usuario** (`src/models/usuario.py`): Representa um usuário e implementa autenticação

## 💡 Perguntas sobre Funcionalidades

### Quais operações estão disponíveis?
- **Depositar [d]**: Adicionar dinheiro à conta
- **Sacar [s]**: Retirar dinheiro da conta (com limites)
- **Extrato [e]**: Visualizar histórico de transações e saldo atual
- **Sair [q]**: Encerrar o programa

### Quais são os limites e regras de negócio?
- **Saldo inicial**: R$ 0,00
- **Limite por saque**: R$ 500,00
- **Número máximo de saques diários**: 3
- **Limite de tentativas de autenticação**: 3

### Como funciona a autenticação?
**Versão modular (src/)**: Utiliza CPF e senha para autenticação. Os usuários predefinidos são:
- CPF: 12345678900, Nome: Rodrigo, Senha: 123asd
- CPF: 11122233344, Nome: Maria, Senha: senha123

**Versão monolítica (Sistema_bancario.py)**: Utiliza usuário e senha simples:
- Usuario: teste01, Senha: 123asd

## 🚀 Perguntas sobre Uso

### Como executar o programa?
```bash
# Versão modular (recomendada)
cd src
python main.py

# Versão monolítica
python Sistema_bancario.py
```

### Qual é o fluxo de uso típico?
1. O usuário é solicitado a fazer login com CPF e senha
2. Após autenticação bem-sucedida, o menu principal é exibido
3. O usuário escolhe uma operação (depositar, sacar, extrato)
4. A operação é processada e o resultado é exibido
5. O menu é exibido novamente até que o usuário escolha sair

### O que acontece se eu errar a senha?
O sistema permite até 3 tentativas. Após esgotar as tentativas, o programa é encerrado.

## 🔧 Perguntas sobre Desenvolvimento

### Quais são as dependências do projeto?
O projeto utiliza apenas bibliotecas padrão do Python:
- `datetime` - Para registro de data/hora das transações

### Como posso adicionar novos usuários?
**Versão modular**: Os usuários são codificados diretamente no método estático `autenticar_usuario()` da classe `Usuario`. Para adicionar um novo usuário, adicione uma nova instância de `Usuario` na lista `usuarios` (linhas 9-11 em `src/models/usuario.py`).

Exemplo:
```python
usuarios = [
    Usuario("12345678900", "Rodrigo", "123asd"),
    Usuario("11122233344", "Maria", "senha123"),
    Usuario("99988877766", "João", "minhasenha"),  # Novo usuário
]
```

### Como posso adicionar novas funcionalidades?
1. **Novas operações bancárias**: Adicione métodos na classe `Conta`
2. **Novos serviços**: Crie novos módulos em `src/services/`
3. **Menu**: Atualize a função `exibir_menu()` e adicione o tratamento na função `main()`

### Existe algum banco de dados?
Não. Atualmente, todos os dados são armazenados em memória e são perdidos quando o programa é encerrado.

### Como posso melhorar a segurança?
Sugestões:
- Implementar hash de senhas (bcrypt, hashlib)
- Armazenar credenciais em um banco de dados
- Adicionar validação de CPF
- Implementar logs de auditoria

## 📝 Perguntas sobre Manutenção

### Onde estão registradas as transações?
As transações são armazenadas como strings no atributo `extrato` da classe `Conta`, formatadas com data/hora e valor.

### Como funciona o controle de saques diários?
O atributo `numero_saques` na classe `Conta` conta quantos saques foram realizados. Este contador é zerado apenas quando uma nova instância da conta é criada (ao reiniciar o programa).

### O que são os arquivos commit.sh e commit_msg_helper.py?
São utilitários para auxiliar no processo de commits do Git, provavelmente para padronizar mensagens de commit.

## 🎯 Próximos Passos Sugeridos

1. Explorar o código em `src/main.py` para entender o fluxo principal
2. Examinar as classes `Conta` e `Usuario` para entender o modelo de domínio
3. Executar o programa e testar todas as operações
4. Considerar melhorias como persistência de dados e testes automatizados

---

**Dúvidas?** Sinta-se à vontade para explorar o código-fonte e fazer perguntas à equipe!
