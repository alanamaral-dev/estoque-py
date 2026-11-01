from dados import estoque, salvar, caixa, registroDeVendas, salvar_caixa, ARQUIVO_ESTOQUE, ARQUIVO_VENDAS

'''==============================================================================
=============================FUNÇÕES DO MENU=====================================
=============================================================================='''

#FUNÇÃO DE CADASTRO E ATUALIZAÇÃO
def cadastro():
    #ADICIONA UM ID AO PRODUTO
    id = 1
    for i in range (len(estoque)):
        id += 1

    #PEDE AS INFORMAÇÕES SOBRE O PRODUTO
    produto = input('Digite o nome do produto a ser cadastrado: ')
    print(f'{'='*39}')
    preco = float(input('Digite o preço do produto: '))
    print(f'{'='*39}')
    quantidade = int(input('Digite a quantidade: '))
    print(f'{'='*39}')

    #CONFERE SE JÁ NÃO HÁ O PRODUTO EM ESTOQUE
    for itens in estoque:
        if itens['Id'] == id:
            itens['Produto'] = produto
            itens['Quantidade'] = quantidade
            itens['Preço'] = preco
            print('Produto Atualizado.')
            break

    #ADICIONA O PRODUTO AO ESTOQUE
    else:
        estoque.append({
                        'Id' : id,
                        'Produto': produto,
                        'Preço': preco, 
                        'Quantidade': quantidade
                        })

        print('[Produto Cadastrado.]')

    salvar(estoque, ARQUIVO_ESTOQUE)


#FUNÇÃO DE REMOÇÃO
def remover():
    #PEDE O PRODUTO QUE SERA REMOVIDO
    removeId = int(input('Digite o [ID] do produto que deseja remover: '))

    #CONFERE SE O PRODUTO REALMENTE ESTÁ EM ESTOQUE E REMOVE
    for i in range (len(estoque)):
        if estoque[i]['Id'] == removeId:
            del estoque[i]
            print('Produto Removido.')
            salvar(estoque, ARQUIVO_ESTOQUE)
            break
    else:
        print('Produto Não Encontrado.')


#FUNÇÃO DE TABELAR OS PRODUTOS
#CRIA UMA TABELA ORGANIZANDO OS PRODUTOS DO ESTOQUE
def lista():
    print('='*44)
    print(f'|{'Id':.<6.6}{'|Produto':.<19.19}|{'Qtd':.>8.8}|{'Preço|':.>8.8}')
    print('='*44)
    for item in estoque:
        print(f"|{str(item['Id']):.>6.6}|{item['Produto']:.<18.18}|{item['Quantidade']:.>8}|{item['Preço']:.>7.2f}|")
    print('='*44)


'''==============================================================================
=========================FUNÇÕES DO MENU DE TABELA===============================
=============================================================================='''

#FUNÇÃO DE SOMAR O VALOR DO ESTOQUE
def somaEstoque():

    soma = 0

    #RECEBE A QUANTIDADE E PREÇO DE UM PRODUTO E OS ATRIBUI A UM ACUMULADOR DE SALDO
    for i in range(len(estoque)):
        preço = estoque[i]['Preço']
        quantidade = estoque[i]['Quantidade']

        acumulador = preço * quantidade
        soma += acumulador

    print(f'O valor do estoque é de: [{soma:.2f}]')


#FUNÇÃO DE SEPARAR POR FAIXA DE PREÇO
def separarPreco():

    #PEDE OS PARAMETROS PARA A SEPARAÇÃO
    valorMinimo = float(input('Digite o valor minimo: '))
    valorMaximo = float(input('Digite o valor maximo: '))

    #GUARDA OS PRODUTOS SEPARADOS PELOS PARAMETROS
    separados = []

    #CONFERE OS PRODUTOS QUE SE ENCAIXAM NOS PARAMETROS E OS GUARDA
    for i in range(len(estoque)):
        itens = estoque[i]['Preço']

        if itens >= valorMinimo and itens <= valorMaximo:
            separados.append({
                            'Id': estoque[i]['Id'],
                            'Produto': estoque[i]['Produto'],
                            'Quantidade': estoque[i]['Quantidade'],
                            'Preço': estoque[i]['Preço']
            })

    #SEPARA OS PRODUTOS SELECIONADOS POR ORDEM DE PREÇO
    listaSeparada = sorted(separados, key=lambda item: item['Preço'])

    print('='*44)
    print(f'|{'Id':.<6.6}{'|Produto':.<19.19}|{'Qtd':.>8.8}|{'Preço|':.>8.8}')
    print('='*44)
    for item in listaSeparada:
        print(f"|{str(item['Id']):.>6.6}|{item['Produto']:.<18.18}|{item['Quantidade']:.>8}|{item['Preço']:.>7.2f}|")
    print('='*44)

    listaSeparada.clear()
    separados.clear()


#FUNÇÃO DE SEPARAR POR QUANTIDADE
def separarQuantidade():

    #ORDENA A TABELA POR ORDEM DE QUANTIDADE
    listaOrdenada = sorted(estoque, key=lambda item: item['Quantidade'])

    print('='*44)
    print(f'|{'Id':.<6.6}{'|Produto':.<19.19}|{'Qtd':.>8.8}|{'Preço|':.>8.8}')
    print('='*44)
    for item in listaOrdenada:
        print(f"|{str(item['Id']):.>6.6}|{item['Produto']:.<18.18}|{item['Quantidade']:.>8}|{item['Preço']:.>7.2f}|")
    print('='*44)

    listaOrdenada.clear()


#FUNÇÃO PARA REALIZAR BUSCAS DE PRODUTOS
def pesquisar():
    #PEDE O PRODUTO A SER PESQUISADO
    pesquisa = (input('Digite o nome do produto que deseja buscar: ')).strip()
    #GUARDA AS INFORMAÇÕES DO PRODUTO PESQUISADO
    pesquisado = []
    teste = 0

    #CONFERE SE O ID DO PRODUTO ESTÁ PRESENTE NO ESTOQUE
    for i in range (len(estoque)):
        if pesquisa == estoque[i]['Produto']:
            #ADICIONA O PRODUTO A LISTA DE PESQUISADO
            pesquisado.append({
                'Id': estoque[i]['Id'],
                'Produto': estoque[i]['Produto'],
                'Quantidade': estoque[i]['Quantidade'],
                'Preço': estoque[i]['Preço']
            })
            print('='*44)
            print(f'|{'Id':.<6.6}{'|Produto':.<19.19}|{'Qtd':.>8.8}|{'Preço|':.>8.8}')
            print('='*44)
            for item in pesquisado:
                print(f"|{str(item['Id']):.>6.6}|{item['Produto']:.<18.18}|{item['Quantidade']:.>8}|{item['Preço']:.>7.2f}|")
                print('='*44)

            teste = 1

    if teste == 0:
        print('Produto não encontrado: Verifique se o [ID] está correto.')


'''==============================================================================
=========================FUNÇÕES DA ÁREA DE VENDAS===============================
=============================================================================='''

#FUNÇÃO PARA REGISTRAR UMA VENDA
def vender():

    global caixa
    registro = 1
    vendas = []
    preço = []

    while registro != 0:
        #REGISTRA UMA VENDA PELO ID
        print(f'{'='*39}')
        venda = int(input('Digite o ID do produto a ser vendido: '))
        quantidade = int(input('Digite a quantidade desse produto a ser vendido: '))
        print(f'{'='*39}')

        vendas.append(venda)

        #ATUALIZA O ESTOQUE COM BASE NA VENDA
        for i in range (len(estoque)):
            if estoque[i]['Id'] == venda:
                estoque[i]['Quantidade'] -= quantidade
                #CALCULA O PREÇO TOTAL DA VENDA
                preço.append(estoque[i]['Preço'] * quantidade)

                print(f'Venda realizada, |Produto: [{estoque[i]['Produto']}]| Qtd: [{quantidade}]| Valor Total: [{sum(preço):.2f}]')
                print(f'{'='*39}')
                #ADICIONA O TOTAL DA VENDA AO CAIXA
                caixa += sum(preço)
                #REGISTRA A VENDA EM UMA LISTA
                registroDeVendas.append({
                    'Produto': estoque[i]['Produto'],
                    'Quantidade': quantidade,
                    'Preço': sum(preço)
                })


        cont = input('Deseja realizar outra venda? [s/n]: ').upper()
        if cont == 'N':
            registro = 0

    salvar(estoque, ARQUIVO_ESTOQUE)
    salvar(registroDeVendas, ARQUIVO_VENDAS)
    salvar_caixa(caixa)

#FUNÇÃO PARA CONFERIR O REGISTRO DAS VENDAS
def registroDeVenda():
    print('='*37)
    print(f'{' REGISTROS DE VENDAS ':=^37}')
    print('='*37)
    print(f'{'|Produto':.<19.19}|{'Qtd':.>8.8}|{'Preço|':.>8.8}')
    print('='*37)
    for i in range (len(registroDeVendas)):
        print(f'|{registroDeVendas[i]['Produto']:.<18.18}|{registroDeVendas[i]['Quantidade']:.>8}|{registroDeVendas[i]['Preço']:.>7.2f}|')
    print('='*37)

    limpar = input('Deseja limpar o registro de vendas? [s/n]: ').strip().upper()

    if limpar == 'S':
        registroDeVendas.clear()
        salvar(registroDeVendas, ARQUIVO_VENDAS)
        print('[Registros de vendas limpo.]')


#FUNÇÃO PARA CONFERIR O VALOR TOTAL EM CAIXA
def conferirCaixa():

    global caixa

    print(f'Valor total em caixa: [R${caixa:.2f}]')
    print('='*37)
    limpar = input('Deseja limpar o saldo do caixa? [s/n]: ').strip().upper()

    if limpar == 'S':
        caixa = 0

        salvar_caixa(caixa)

        print('[Caixa limpo.]')
