alunos = {}

for i in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota: "))
    alunos[nome] = nota

print("\nRelatório de Notas:")

for nome, nota in alunos.items():
    status = "Aprovado" if nota >= 7 else "Reprovado"
    print(f"{nome} - Nota: {nota} - {status}")