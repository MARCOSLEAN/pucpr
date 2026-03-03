numeros = []

for i in range(5):
    numero = int(input(f"Digite o número {i+1}: "))
    numeros.append(numero)

print("Lista completa:", numeros)
print("Maior número:", max(numeros))
print("Menor número:", min(numeros))
print("Soma total:", sum(numeros))