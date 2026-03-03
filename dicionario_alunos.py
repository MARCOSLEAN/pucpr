# Cria um dicionário para armazenar os alunos e suas notas.
alunos = {}

# Usa um loop que solicita o nome e a nota de 3 alunos e armazena no dicionário.
for i in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota: "))
    alunos[nome] = nota

# Imprime o nome do aluno, a nota e se ele foi aprovado ou reprovado (nota >= 7 é aprovado).
print("\nRelatório de Notas:")

# Utiliza um loop para iterar sobre o dicionario e imprimir as informações de cada aluno.
for nome, nota in alunos.items():
    status = "Aprovado" if nota >= 7 else "Reprovado"
    print(f"{nome} - Nota: {nota} - {status}")