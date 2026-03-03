# Criar arquivo
with open("infos.txt", "w") as arquivo:
    arquivo.write("Estudando DevOps!\n")
    arquivo.write("Entender Git é essencial.\n")

# Ler arquivo
with open("infos.txt", "r") as arquivo:
    conteudo = arquivo.read()

print("Conteúdo do arquivo:")
print(conteudo)