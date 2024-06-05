## Pequeno Crud em python

usuarios = []
menu = """
===================================
Bem-vindo ao Cadastro de Usuários

[1] - Cadastrar Usuário
[2] - Atualizar Usuário
[3] - Listar Usuários
[4] - Procurar Usuário
[5] - Apagar Usuário
[6] - Sair
===================================
"""
usuario_encontrado = False

while True:
    print(menu)
    opcao = int(input("Escolha uma opção: "))

    ## Cadastrar Usuário

    if opcao == 1:
        nome = input("Digite o nome do usuário: ")
        email = input("Digite o email do usuário: ")
        cpf = int(input("Digite o cpf do usuário(Atenção: Não pode ser alterado!): "))
        idade = int(input("Digite a idade do usuário: "))
        usuarios.append({
            "nome": nome,
            "email": email,
            "cpf": cpf,
            "idade": idade
        })

    ## Atualizar Usuário

    elif opcao == 2:
        nome = input("Digite o CPF do usuário: ")
        for usuario in usuarios:
            if usuario["cpf"] == cpf:
                usuario["nome"] = input("Digite o novo nome do usuário: ")
                usuario["email"] = input("Digite o novo email do usuário: ")
                usuario["idade"] = int(input("Digite a nova idade do usuário: "))
                usuario_encontrado = True
                print("Usuário atualizado com sucesso!")
                break
        if not usuario_encontrado:
            print("Usuário não encontrado!")
        

    ## Listar Usuários

    elif opcao == 3:
        print("======Usuários cadastrados======\n")
        for usuario in usuarios:
            print("------------------------------")
            print(f"Nome: {usuario['nome']}")
            print(f"Email: {usuario['email']}")
            print(f"CPF: {usuario['cpf']}")
            print(f"Idade: {usuario['idade']}")
            print("------------------------------")

    ## Pesquisar usuário

    elif opcao == 4:
        cpf = int(input("Digite o cpf do usuário: "))
        for usuario in usuarios:
            if usuario["cpf"] == cpf:
                print("------------------------------")
                print(f"Nome: {usuario['nome']}")
                print(f"Email: {usuario['email']}")
                print(f"CPF: {usuario['cpf']}")
                print(f"Idade: {usuario['idade']}")
                print("------------------------------")
                usuario_encontrado = True
                break
        if not usuario_encontrado:
            print("Usuário não encontrado!")

    ## Apagar o usuário

    elif opcao == 5:
        nome = input("Digite o cpf do usuário: ")
        for usuario in usuarios:
            if usuario["cpf"] == cpf:
                usuario_encontrado = True
                usuarios.remove(usuario)
                break
        if not usuario_encontrado:
            print("Usuário não encontrado!")

    ## Encerrar
    
    elif opcao == 6:
        print("Obrigado por utilizar nossos serviços!")
        break
    else:
        print("Opção inválida!")
        break