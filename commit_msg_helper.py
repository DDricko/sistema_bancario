# commit_msg_helper.py
print("=== Criador de commit semantico ===")
tipos = {
    "1": "feat",
    "2": "fix",
    "3": "docs",
    "4": "style",
    "5": "refactor",
    "6": "test",
    "7": "chore"
}

print("Escolha o tipo de alteracao:")
for key, value in tipos.items():
    print(f"{key}: {value}")

tipo_escolhido = input("Numero: ").strip()
tipo = tipos.get(tipo_escolhido)

if not tipo:
    print("❌ Tipo invalido")
    exit(1)

escopo = input("Escopo (ex: banco, login, api): ").strip()
descricao = input("Descricao breve: ").strip()

commit_message = f"{tipo}({escopo}): {descricao}"

# Salvar em .commitmsg
with open(".commitmsg", "w") as f:
    f.write(commit_message)

print(f"✅ Mensagem gerada: {commit_message}")
