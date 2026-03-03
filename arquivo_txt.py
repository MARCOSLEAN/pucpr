# Criar arquivo
with open("dados.txt", "w") as arquivo:
    arquivo.write("Estudando DevOps!\n")
    arquivo.write("Entender Git é essencial.\n")

# Ler arquivo
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()

print("Conteúdo do arquivo dados.txt:")
print(conteudo)