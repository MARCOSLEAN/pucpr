def saudacao(nome):
    return f"Olá, {nome}! Bem-vindo ao DevOps."


if __name__ == "__main__":
    nome_usuario = input("Digite seu nome: ")
    print(saudacao(nome_usuario))