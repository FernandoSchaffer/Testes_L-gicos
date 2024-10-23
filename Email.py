tentativas = 0
email_cadastrado = []
senha_cadastrada = []

while True:

    email = input("Insira o nome para usar no email: ")
    senha = input("Cadastre uma senha com 5 números: ")

    
    if len(senha) != 5:
        print("Senha precisa ter 5 números")
        continue

    senha_cadastrada.append(senha)
    email_cadastrado.append(email)
    print("Usuário cadastrado com sucesso")


    while True:

        login_email = input("Escreva seu email para login: ")
        login_senha = input("Digite a sua senha: ")
        tentativas += 1

        if tentativas > 3:
            print("Você tentou mais de 3 vezes. Espere 15 min")
            print(f"Usuário é {email_cadastrado} e a senha {senha_cadastrada}")
            break
        if login_email == email_cadastrado[-1] and login_senha == senha_cadastrada[-1]:
            print("Seja bem vindo")
            break
        else:
            print("Tente novamente")
            
    break