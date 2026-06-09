import random

senhas = []

while True:
    print("Seja muito bem-vindo ao gerador de senhas pt! Aqui você poderá criar senhas fortes e não terá problema na hora de acessar seus serviços.")
    print("Orientação: Procure sempre utilizar senhas fortes para seus acessos. Uma senha forte geralmente contém mais de 8 caracteres, que incluem letras maiúsculas e minúsculas, números e símbolos. Evite senhas contendo nomes de parentes, datas de aniversário sua ou deles e informações biográficas, pois hoje em dia são dados de fácil descoberta, por mais que não pareça tanto")

    print("Agora, escolha a sua opção: ")
    print("1: Cadastrar uma nova senha.")
    print("2: Ver sua senhas.")
    print("3: sair")
    escolhaOpcao = int(input("Escolha uma opção"))

    if(escolhaOpcao == 1):
        letramaiuscula = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        letraminuscula = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        simbolos = [".", "-", "!", "?", "_"]
        caracteres = letramaiuscula + letraminuscula + numeros + simbolos
        senha = ""


        user     = input("Indique a qual serviço ou nome de usuário pertence essa senha")
        comprimento = int(input("Indique quantos caracteres a sua senha terá"))

        for _ in range(comprimento):
            letra = random.choice(caracteres)
            senha += letra
        
        dict_dados_senha = {
            "service": user,
            "password": senha
        }

        senhas.append(dict_dados_senha)
        print(f"A sua senha é do user {user}, e ela possuirá {comprimento} caracteres. A senha é: {senha}")
    elif escolhaOpcao == 2:
        if len(senhas) == 0:
            print("Nenhuma senha cadastrada ainda")
        else:
            for item in senhas:
                print(f"Serviço: {item["service"]}. Senha: {item["password"]}")
    elif escolhaOpcao == 3:
        print("Fim do programa, até a próxima")
        break
    else:
        print("A sua escolha deve ser um número de 1 a 3, e não pode ser um texto. Tente de novo por favor")
