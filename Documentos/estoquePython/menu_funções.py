from dados import estoque, salvar, caixa, registroDeVendas

'''==============================================================================
=============================FUNÇÕES DO MENU=====================================
=============================================================================='''

#FUNÇÃO DE CADASTRO E ATUALIZAÇÃO
def cadastro():
    id = 1
    for i in range (len(estoque)):
        id += 1

    produto = input('Digite o nome do produto a ser cadastrado: ')
    print(f'{'='*39}')
    preco = float(input('Digite o preço do produto: '))
    print(f'{'='*39}')
    quantidade = int(input('Digite a quantidade: '))
    print(f'{'='*39}')

    for itens in estoque:
        if itens['Id'] == id:
            itens['Produto'] = produto
            itens['Quantidade'] = quantidade
            itens['Preço'] = preco
            print('Produto Atualizado.')
            break

    else:
        estoque.append({
                        'Id' : id,
                        'Produto': produto,
                        'Preço': preco, 
                        'Quantidade': quantidade
                        })

        print('[Produto Cadastrado.]')

    salvar()


#FUNÇÃO DE REMOÇÃO
def remover():
    produto = input('Digite o [ID] do produto que deseja remover: ')

    for item in estoque:
        if item['Id'] == id:
            estoque.remove(item)
            print('Produto Removido.')
            salvar()
            break
    else:
        print('Produto Não Encontrado.')


#FUNÇÃO DE TABELAR OS PRODUTOS
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

    for i in range(len(estoque)):
        preço = estoque[i]['Preço']
        quantidade = estoque[i]['Quantidade']

        acumulador = preço * quantidade
        soma += acumulador

    print(f'O valor do estoque é de: [{soma:.2f}]')


#FUNÇÃO DE SEPARAR POR FAIXA DE PREÇO
def separarPreco():

    valorMinimo = float(input('Digite o valor minimo: '))
    valorMaximo = float(input('Digite o valor maximo: '))

    separados = []

    for i in range(len(estoque)):
        itens = estoque[i]['Preço']

        if itens >= valorMinimo and itens <= valorMaximo:
            separados.append({
                            'Id': estoque[i]['Id'],
                            'Produto': estoque[i]['Produto'],
                            'Quantidade': estoque[i]['Quantidade'],
                            'Preço': estoque[i]['Preço']
            })

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
    pesquisa = (input('Digite o nome do produto que deseja buscar: ')).strip()
    pesquisado = []
    teste = 0

    for i in range (len(estoque)):
        if pesquisa == estoque[i]['Produto']:
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

def vender():

    registro = -1
    vendas = []

    while registro != 0:

        venda = input('Digite o ID do produto a ser vendido [0 Para parar de registrar]: ').strip()
        quantidade = int(input('Digite a quantidade desse produto a ser vendido: '))
        preço = []
        vendas.append(venda)

        for id in vendas:
            for i in range (len(estoque)):
                if estoque[i]['Id'] == id:
                    estoque[i]['Quantidade'] -= quantidade
                    preço.append(estoque[i]['Preço'] * quantidade)

                    print(f'Venda realizada, preço total: {sum(preço)}')

                    caixa += sum(preço)
                    
                    registroDeVendas.append({
                        estoque[i]['Produto'], 
                        quantidade,
                        sum(preço)
                    })

                    salvar()


def registroDeVenda():

    for i in range (len(registroDeVendas)):
        print(f'{registroDeVendas[i]}')


def conferirCaixa():

    print(f'Valor total em caixa: {caixa}')
