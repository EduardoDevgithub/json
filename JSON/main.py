import time
import os
import funcoes
from os import system

transacao = []

if __name__ == '__main__': 
    system('cls')

    funcoes.verific()

    while True:
        system('cls')
        print('○ Data da transação. ')
        print('○ Descrição (por exemplo,"Almoço" ou "Salário" ). ')
        print('○ Valor(positivo para receitas e negativo para despesas). ')
        print('○ Categoria(por exemplo,"Alimentação","Transporte","Lazer","Renda", etc.)')


        print('\n[1] - Inserir Transação')
        print('[2] - Listar transações')
        print('[3] - Exibir receitas')
        print('[4] - Sair')
        escolha = int(input('\nSelect: '))

        if escolha == 4:
            break
        elif escolha == 2:
            funcoes.listar(transacao)
            input('\n\nPressione qualquer tecla para continuar... ')
            system('cls')
        elif escolha == 1:
            system('cls')
            funcoes.insert_work()
            input('\n\nPressione qualquer tecla para continuar... ')
        elif escolha == 3:
            system('cls')
            receitas = []
            despesas = []
            for item in transacao:
                if item['valor'] >= 0:
                    receitas.append(item['valor'])
                elif item['valor'] < 0:
                    despesas.append(item['valor'])
            
            print(f'\nTotal de Receitas: R${receitas}')
            print(f'Total de Despesas: R${despesas}\n')
            print('-' * 45, '\n', 'RELATÓRIO FINALIZADO COM SUCESSO!', '-')

            input('\n\nPressione qualquer tecla para continuar... ')
        else:
            print('Número inválido!!!')
            time.sleep(1)
            system('cls')