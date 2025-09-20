"""Lista de compras com opçoes de: inserir/ apagar itens e listar a nova lista"""
from os import system
lista_compras= []
while True:
    try:
        op = input("[I]nseri / [A]pagar / [Listar]").upper()
        if op == "I":
            lista_compras.append(input("Digite o item para adicionar: "))
            continue
        elif op == "A":
            if len(lista_compras)== 0:
                print("A lista esta vazia, não sera possivel apagar um item")
                continue
            else:
                for index,item in enumerate(lista_compras) :
                    print (index+1, item)
            deletar = int(input("Digite o numero do item que deseja apagar: "))
            if deletar-1 in range(len(lista_compras)):
                del lista_compras[deletar-1]
                print(f"O item: {item} foi removido da lista")
            else:
                print(f"Não existe um item {item} para deleta, tente novamente")
        elif op == 'L':
            
            for index,item in enumerate(lista_compras) :
                print (index+1, item)
        else: 
            print("A opção inserida nao foi encontrada, tente novamente.")
            continue
    except:
        print("Algo deu errado, informe a opção desejada novamente")
