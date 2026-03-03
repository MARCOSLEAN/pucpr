numeros = []

for i in range(5):
    numero = int(input(f"Digite o número {i+1}: "))
    numeros.append(numero)

print("Lista dos Números:", numeros)
print("Este é o Maior número:", max(numeros))
print("Este é o Menor número:", min(numeros))
print("Soma total dos números:", sum(numeros))