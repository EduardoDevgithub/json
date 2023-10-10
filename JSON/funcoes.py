import json
import os
import main
from os import system

transacao = 'transacao.json'

def listar(transacao):
    with open('transacao.json', 'r') as f:
        return json.load(f)
        
    

def verific():
    nome_arquivo = 'transacao.json'
    if os.path.exists(nome_arquivo):
        with open('transacao.json', 'r') as f:
            transacao = json.load(f)
    else:
        transacao = []
         

def insert_work():
    data, mes, ano = input('\nInsira a data (8 caracteres): ').split(' ')
    with open('transacao.json', 'w') as f:
        json.dump(transacao, f)
        transacao.append(data)
        transacao.append(mes)
        transacao.append(ano)
        system('cls')

    descricao = input('\nInsira a descrição: ')
    with open('transacao.json', 'w') as f:
        json.dump(transacao, f)
        transacao.append(descricao)
        system('cls')

    valor = float(input('\nInsira o valor: '))
    with open('transacao.json', 'w') as f:
        json.dump(transacao, f)
        transacao.append(valor)
        system('cls')

    categoria = input('\nInsira a categoria: ')
    with open('transacao.json', 'w') as f:
        json.dump(transacao, f)
        transacao.append(categoria)
        system('cls')