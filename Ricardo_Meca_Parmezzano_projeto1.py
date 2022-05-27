import json
import os.path
import sys

def obter_dados():
    with open(os.path.join(sys.path[0], 'dados.json'),'r') as arq:
        dados = json.loads(arq.read())
    return dados

def listar_categorias(dados:list) -> list:
    """
    parâmetro dados: Esta função recebe uma lista de dicionários.
    return: Esta função retorna uma lista de categorias em ordem alfabética.
    """
    k = 0
    lista_categorias = []
    while k < len(dados):
        while not dados[k]["categoria"] in lista_categorias:
             lista_categorias.append(dados[k]["categoria"])
        k +=1
        
    return sorted(lista_categorias)


def listar_por_categoria(dados:list, categoria:str) -> list:
    """
    parâmetro dados: Este parâmetro recebe uma lista de dicionários.
    parâmetro categoria: Este parâmetro recebe via input digitado pelo usuário uma categoria (str).
    return: Esta função retorna uma lista por categoria.
    """
    k = 0
    lista_por_categoria = []
    while k < len(dados):
        if dados[k]["categoria"] == categoria:
            lista_por_categoria.append(dados[k])
        k +=1
    return lista_por_categoria

def produto_mais_caro(dados:list, categoria:str) -> dict:
    """
    parâmetro dados: Este parâmetro recebe uma lista de dicionários.
    parâmetro categoria: Este parâmetro recebe via input digitado pelo usuário uma categoria (str).
    return: Esta função retorna o produto mais caro de uma categoria da lista. Caso haja mais de um,
    retorna uma lista com os produtos de mesmo valor.
    """
    i = 0
    k = 0
    while not dados[i]["categoria"] == categoria:
        i +=1
    item_mais_caro = float(dados[i]["preco"])
    dic_produto = dict(dados[i])
    lista_mesmo_valor = [dados[i]]
    while k < len(dados):
        if dados[k]["categoria"] == categoria:
            if float(dados[k]["preco"]) == item_mais_caro and k != i:
                lista_mesmo_valor.append(dados[k])
            elif float(dados[k]["preco"]) > item_mais_caro:
                item_mais_caro = float(dados[k]["preco"])
                dic_produto = dados[k]
                lista_mesmo_valor = []
                lista_mesmo_valor.append(dados[k])
        k +=1
    return dic_produto, lista_mesmo_valor

def produto_mais_barato(dados:list, categoria:str) -> dict:
    """
    parâmetro dados: Este parâmetro recebe uma lista de dicionários.
    parâmetro categoria: Este parâmetro recebe via input digitado pelo usuário uma categoria (str).
    return: Esta função retorna o produto mais barato de uma categoria da lista. Caso haja mais de um,
    retorna uma lista com os produtos de mesmo valor.
    """
    i = 0
    k = 0
    while not dados[i]["categoria"] == categoria:
        i +=1
    item_mais_barato = float(dados[i]["preco"])
    dic_produto = dict(dados[i])
    lista_mesmo_valor = [dados[i]]
    while k < len(dados):
        if dados[k]["categoria"] == categoria:
            if float(dados[k]["preco"]) == item_mais_barato and k != i:
                lista_mesmo_valor.append(dados[k])
            elif float(dados[k]["preco"]) < item_mais_barato:
                item_mais_barato = float(dados[k]["preco"])
                dic_produto = dados[k]
                lista_mesmo_valor = []
                lista_mesmo_valor.append(dados[k])
        k +=1
    return dic_produto, lista_mesmo_valor

def top_10_caros(dados:list) -> list:
    """
    parâmetro dados: Este parâmetro recebe uma lista de dicionários.
    return: Esta função retorna uma lista de dicionários com os 10 produtos mais caros de uma categoria da lista.
    Caso haja empate no décimo, a função lhe dá a opção de escolha pelo truncamento ou exibição de todos os produtos
    com mesmo valor que o décimo.
    """
    
    dados_organizados = sorted(dados, key=lambda x:float(x["preco"]), reverse = True)
    final = 10
    while float(dados_organizados[9]['preco']) == float(dados_organizados[final]['preco']):
        final +=1
    return dados_organizados, final

def top_10_baratos(dados:list) -> list:
    """
    parâmetro dados: Este parâmetro recebe uma lista de dicionários.
    return:Esta função retorna uma lista de dicionários com os 10 produtos mais baratos de uma categoria da lista.
    Caso haja empate no décimo, a função lhe dá a opção de escolha pelo truncamento ou exibição de todos os produtos
    com mesmo valor que o décimo.
    """
    dados_organizados = sorted(dados, key=lambda x:float(x["preco"]))
    final = 10
    while float(dados_organizados[9]['preco']) == float(dados_organizados[final]['preco']):
        final +=1
    return dados_organizados, final

def menu(dados:list):
    """
    parâmetro dados: Este parâmetro recebe uma lista de dicionários.
    return: De acordo com a escolha do usuário: 
    1. Listar categorias
    2. Listar produtos de uma categoria
    3. Produto mais caro por categoria
    4. Produto mais barato por categoria
    5. Top 10 produtos mais caros
    6. Top 10 produtos mais baratos
    Há ainda a opção do 0 para sair do menu.
    """

    print('-'*50)
    print(f'{"LOJAS MECA TOP CODERS. SEJA BEM VINDO/A":^50}')
    print('-' * 50)
    opcao = -1
    while opcao != "0":
        opcao = input("""    Por favor, escolha uma das opções abaixo:
--------------------------------------------------                                        
1. Listar categorias
2. Listar produtos de uma categoria
3. Produto mais caro por categoria
4. Produto mais barato por categoria
5. Top 10 produtos mais caros
6. Top 10 produtos mais baratos
0. Sair
--------------------------------------------------
\n""")
        while (opcao != "0") and (opcao != "1") and (opcao != "2") and (opcao != "3") and (opcao != "4")\
                and (opcao != "5") and (opcao != "6"):
            print('Opção Inválida. Tente novamente!!!\n')
            opcao = input("""Escolha uma das opções abaixo:
--------------------------------------------------
1. Listar categorias
2. Listar produtos de uma categoria
3. Produto mais caro por categoria
4. Produto mais barato por categoria
5. Top 10 produtos mais caros
6. Top 10 produtos mais baratos
0. Sair
--------------------------------------------------
\n""")
        if opcao == "0":
            print('Você saiu do programa! Volte sempre!!!')
        
        if opcao == "1":
            lista_categoria = listar_categorias(dados)
            print('-' * 50)
            print(f'{"CATEGORIAS EM ORDEM ALFABÉTICA":^50}')
            print('-' * 50)

            for i in range(len(lista_categoria)):
                print(lista_categoria[i].upper())
            print('-' * 50)

        if opcao == "2":
            sub_menu = listar_categorias(dados)
            print('-' * 50)
            print(f'{"CATEGORIAS EM ORDEM ALFABÉTICA":^50}')
            print('-' * 50)
            for i in range(len(sub_menu)):
                print(sub_menu[i].upper())
            print('-' * 50)
            categoria = input('Por favor, digite uma das categorias acima: ').lower()
            while not categoria in sub_menu:
                print('-' * 50)
                print("A CATEGORIA DIGITADA NÃO EXISTE. TENTE NOVAMENTE!!")
                print('-' * 50)
                print(f'{"CATEGORIAS EM ORDEM ALFABÉTICA":^50}')
                print('-' * 50)
                for i in range(len(sub_menu)):
                    print(sub_menu[i].upper())
                print('-' * 50)
                categoria = input('Por favor, verifique as categorias acima e digite uma delas: ').lower()
                for i in range(len(sub_menu)):
                    print(sub_menu[i].upper())
                print('-' * 50)
            lista_por_categoria = listar_por_categoria(dados, categoria)
            print('-' * 135)
            print(f'{categoria.upper():^135}')
            print('-' * 135)
            for i in range(len(lista_por_categoria)):
                print(lista_por_categoria[i])
            print('-' * 135)

        if opcao == "3":
            sub_menu = listar_categorias(dados)
            print('-' * 50)
            print(f'{"CATEGORIAS EM ORDEM ALFABÉTICA":^50}')
            print('-' * 50)
            for i in range(len(sub_menu)):
                print(sub_menu[i].upper())
            print('-' * 50)
            categoria = input('Por favor, verifique as categorias acima e digite uma delas:  ').lower()
            while not categoria in sub_menu:
                print('-' * 50)
                print("A CATEGORIA DIGITADA NÃO EXISTE. TENTE NOVAMENTE!!")
                print('-' * 50)
                print(f'{"CATEGORIAS EM ORDEM ALFABÉTICA":^50}')
                print('-' * 50)
                for i in range(len(sub_menu)):
                    print(sub_menu[i].upper())
                print('-' * 50)
                categoria = input('Por favor, verifique as categorias acima e digite uma delas:  ').lower()
                for i in range(len(sub_menu)):
                    print(sub_menu[i].upper())
                print('-' * 50)
            dic_produto, lista_mesmo_valor = produto_mais_caro(dados, categoria)

            if len(lista_mesmo_valor) == 1:
                print('-' * 135)
                print(f'EXISTE APENAS UM PRODUTO MAIS CARO NA CATEGORIA {categoria.upper()}')
                print('-' * 135)
                print(dic_produto)
                print('-' * 135)
            else:
                print('-' * 135)
                print(
                    f'EXISTEM {len(lista_mesmo_valor)} PRODUTOS MAIS CAROS (COM MESMO VALOR) NA CATEGORIA {categoria.upper()}')
                print('-' * 135)
                for i in range(len(lista_mesmo_valor)):
                    print(lista_mesmo_valor[i])
                print('-' * 135)

        if opcao == "4":
            sub_menu = listar_categorias(dados)
            print('-' * 50)
            print(f'{"CATEGORIAS EM ORDEM ALFABÉTICA":^50}')
            print('-' * 50)
            for i in range(len(sub_menu)):
                print(sub_menu[i].upper())
            print('-' * 50)
            categoria = input('Por favor, verifique as categorias acima e digite uma delas:  ').lower()
            while not categoria in sub_menu:
                print('-' * 50)
                print("A CATEGORIA DIGITADA NÃO EXISTE. TENTE NOVAMENTE!!")
                print('-' * 50)
                print(f'{"CATEGORIAS EM ORDEM ALFABÉTICA":^50}')
                print('-' * 50)
                for i in range(len(sub_menu)):
                    print(sub_menu[i].upper())
                print('-' * 50)
                categoria = input('Por favor, verifique as categorias acima e digite uma delas:  ').lower()
                for i in range(len(sub_menu)):
                    print(sub_menu[i].upper())
                print('-' * 50)
            dic_produto, lista_mesmo_valor = produto_mais_barato(dados, categoria)

            if len(lista_mesmo_valor) == 1:
                print('-' * 135)
                print(f'EXISTE APENAS UM PRODUTO MAIS BARATO NA CATEGORIA {categoria.upper()}')
                print('-' * 135)
                print(dic_produto)
                print('-' * 135)
            else:
                print('-' * 135)
                print(
                    f'EXISTEM {len(lista_mesmo_valor)} PRODUTOS MAIS BARATOS (COM MESMO VALOR) NA CATEGORIA {categoria.upper()}')
                print('-' * 135)
                for i in range(len(lista_mesmo_valor)):
                    print(lista_mesmo_valor[i])
                print('-' * 135)
        if opcao == "5":
            dados_organizados, final = top_10_caros(dados)
            print('-' * 135)
            print(f'A LISTA POSSUI {final} PRODUTOS MAIS CAROS.')
            if final > 10:
                print(f'A LISTA FINAL POSSUIRÁ {final - 10} ELEMENTO/S A MAIS POIS HÁ PRODUTOS COM MESMO PREÇO DO DÉCIMO.')
                resposta = input('Deseja truncar a lista para 10 elementos? S/N').upper()
                while resposta != 'S' and resposta != 'N':
                    print("RESPOSTA INVÁLIDA")
                    print('-' * 135)
                    resposta = input('Deseja truncar a lista para 10 elementos? S/N: ').upper()
                if resposta == 'S':
                    final = 10
            print('-' * 135)
            for cont in range(final):
               print(dados_organizados[cont])
        if opcao == "6":
            dados_organizados, final = top_10_baratos(dados)
            print('-' * 135)
            print(f'A LISTA POSSUI {final} PRODUTOS MAIS BARATOS.')
            if final > 10:
                print(f'A LISTA FINAL POSSUIRÁ {final - 10} ELEMENTO/S A MAIS POIS HÁ PRODUTOS COM MESMO PREÇO DO DÉCIMO.')
                resposta = input('Deseja truncar a lista para 10 elementos? S/N').upper()
                while resposta != 'S' and resposta != 'N':
                    print("RESPOSTA INVÁLIDA")
                    print('-' * 135)
                    resposta = input('Deseja truncar a lista para 10 elementos? S/N: ').upper()
                if resposta == 'S':
                    final = 10
            print('-' * 135)
            for cont in range(final):
               print(dados_organizados[cont])
dados = obter_dados()
menu(dados)