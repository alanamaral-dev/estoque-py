from menus import menu
from menus import menu_estoque
from menus import menuVendas
import menu_funções

menu()

#GUARDA A FUNÇÃO QUE O USUARIO ESCOLHER ULTILIZAR3
func = int(input('Qual função deseja usar: '))

while func != 0:

    #MOSTRA O MENU PRINCIPAL DE FUNÇÕES
    if func == 9:
        menu()
        func = int(input('Qual função deseja usar: '))

    #REALIZA CADASTROS E ATUALIZAÇÕES DE PRODUTOS
    if func == 1:
        menu_funções.cadastro()
        enter = input('[Aperte enter para voltar ao menu:] ')

        if enter == '':
            func = 9

    #REMOVE PRODUTOS CADASTRADOS
    elif func == 2:
        menu_funções.remover()
        enter = input('[Aperte enter para voltar ao menu:] ')
        
        if enter == '':
            func = 9

    #MOSTRA UMA TABELA COM TODOS OS PRODUTOS CADASTRADOS
    elif func == 3:
        menu_funções.lista()
        menuEstoque = input('[Deseja acessar o menu de estoque? [s/n]: ').strip().upper()

        if menuEstoque == 'N':
            enter = input('[Aperte enter para voltar ao menu:] ')
            
            if enter == '':
                func = 9
                

        #MOSTRA O MENU DE TABELA PARA REALIZAR SELECTS MAIS PRECISOS DE PRODUTOS
        while menuEstoque == 'S':
            menu_estoque()
            funcEstoque = int(input('Qual função deseja usar: '))


            #SOMA O VALOR TOTAL DO ESTOQUE
            if funcEstoque == 1:
                print(f'{'='*39}')
                menu_funções.somaEstoque()
                enter = (input('[Aperte enter para voltar ao menu do estoque]'))
                if enter == '':
                    menuEstoque = 'S'

            #SEPARA OS PRODUTOS POR DETERMINADA FAIXA DE PREÇO
            elif funcEstoque == 2:
                print(f'{'='*39}')
                menu_funções.separarPreco()
                enter = (input('[Aperte enter para voltar ao menu do estoque]'))
                if enter == '':
                    menuEstoque = 'S'

            #SEPARA OS PRODUTOS POR QUANTIDADESA
            elif funcEstoque == 3:
                print(f'{'='*39}')
                menu_funções.separarQuantidade()
                enter = (input('[Aperte enter para voltar ao menu do estoque]'))
                if enter == '':
                    menuEstoque = 'S'


            #USADO PARA PESQUISAR UM PRODUTO DENTRO DOS JA CADASTRADOS
            elif funcEstoque == 4:
                print(f'{'='*39}')
                menu_funções.pesquisar()
                enter = (input('[Aperte enter para voltar ao menu do estoque]'))
                if enter == '':
                    menuEstoque = 'S'

            #FECHA O PROGRAMA
            elif funcEstoque == 0:
                func = 9
                menuEstoque = 'N'

    #ACESSA SESSÃO DE VENDAS
    elif func == 4:
        menuVendas()
        funcVendas = -1

        while funcVendas != 0:
            menuVendas()
            print(f'{'='*39}')
            funcVendas = int(input('Qual função deseja utilizar: '))

            #REALIZA VENDAS
            if funcVendas == 1:
                menu_funções.vender()
            
                enter = input('[Aperte enter para voltar ao menu] ')
                
                if enter == '':
                    func = 9

            #MOSTRA O REGISTRO DAS VENDAS
            elif funcVendas == 2:
                menu_funções.registroDeVenda()

                enter = input('[Aperte enter para voltar ao menu] ')
                
                if enter == '':
                    func = 9

            #MOSTRA O SALDO EM CAIXA
            elif funcVendas == 3:
                menu_funções.conferirCaixa()

                enter = input('[Aperte enter para voltar ao menu] ')
                
                if enter == '':
                    func = 9

            #VOLTA AO MENU PRINCIPAL
            if funcVendas == 0:
                func = 9

    elif func == 0:
        break