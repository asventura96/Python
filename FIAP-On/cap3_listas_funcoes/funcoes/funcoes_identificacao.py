def preencherInventario(lista):
    resp = "S"
    while resp == "S":
        equipamento = [input("Equipamento: "),
                        float(input("Valor: ")),
                        int(input("Número de Série: ")),
                        input("Departamento: ")]
    lista.append(equipamento)
    resp = input("Digite \"S\" para continuar a inserção de equipamentos: ").upper()

def exibirInventario(lista):
    for elemento in lista:
        print("Nome...................: ", elemento[0])
        print("Valor..................: ", elemento[1])
        print("Número de Série........: ", elemento[2])
        print("Departamento...........: ", elemento[3])

def localizarPorNome(lista):
    busca = input("\nDigite o nome do equipamento que deseja visualizar: ")
    for elemento in lista:
        if busca == elemento[0]:
            print("Valor..................: ", elemento[1])
            print("Número de Série........: ", elemento[2])

def depreciarPorNome(lista, porc):
    depreciacao = input("\nDigite o nome do equipamento que será depreciado: ")
    for elemento in lista:
        if depreciacao == elemento[0]:
            print("Valor antigo: ", elemento[1])
            elemento[1] = elemento[1] * (1 - porc / 100)
            print("Novo valor: ", elemento[1])

def excluirPorSerial(lista):
    serial = int(input("\nDigite o número de série do equipamento que será excluído: "))
    for elemento in lista:
        if elemento[2] == serial:
            lista.remove(elemento)
        return "Item Excluído com Sucesso!"

def resumirValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    if len (valores) > 0:
        print("O equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O total de equipamentos é de: ", sum(valores))