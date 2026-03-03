def calcular(a, b, operacao):
    if operacao == "+":
        return a + b
    elif operacao == "-":
        return a - b
    elif operacao == "*":
        return a * b
    elif operacao == "/":
        return a / b
    else:
        return "Operação inválida"


if __name__ == "__main__":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    op = input("Digite a operação (+, -, *, /): ")

    resultado = calcular(num1, num2, op)
    print("Resultado:", resultado)