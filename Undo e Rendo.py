# Criando minhas Funções

def cria_tarefa(task):
    task.append(input('Nome da Tarefa: '))
    print(task)
    return task


def lista_tarefa(lista):
    print(lista)

def desfaz_tarefa(tirado, desfez):
    desfez.append(lista[tirado])
    lista.pop(tirado)
    return lista, desfez


def refaz_tarefa(lista, desfeito):
    if len(desfeito) == 0:
        print('\t\033[1;31mVOCÊ NÃO TEM NADA PARA REFAZER\033[m')
        return lista, desfeito
    else:
        print('Qual Tarefa Você quer refazer: ')
        for k, v in enumerate(desfeito):
            print(f'[{k}] para refazer {v}')
        resp = int(input('Opção: '))
        lista.append(desfeito[resp])
        desfeito.pop(resp)
        return lista, desfeito


# Criando o Menu

import time

lista = []
desfeito = []
cont = 0
while True:
    title = 'UNDO REDO'
    print('-='*20)
    print(f'{title:^40}')
    print('-='*20)

    print('Escolha: ')
    print("""\t[1]. Criar uma Tarefa
\t[2]. Mostrar minhas Tarefas
\t[3]. Desfazer Uma Tarefa
\t[4]. Refazer Uma Tarefa
\t[5]. Encerrar
----------------------------------------""")
    op = int(input('Opção: '))
 # Criado para ter a certeza de que o user criou ao menos uma tarefa

# Fazendo as Interações com as funções criadas

    if cont == 0:

        if op == 1:
            lista = cria_tarefa(lista)
            cont += 1

        elif op == 5:
            print('\t\033[1;31mATÉ A PRÓXIMA...\033[m')
            break

        else:
            print('\t\033[1;31mCRIE UMA TAREFA ANTES\033[m')
            time.sleep(0.3)
            continue

    else:

        if op == 1:
            lista = cria_tarefa(lista)

        elif op == 2:
            lista_tarefa(lista)
            time.sleep(0.3)

        elif op == 3:
            for k, v in enumerate(lista):
                print(f'[{k}] para tirar {v}')
            tira_da_lista = int(input('Opção: '))
            lista, desfeito = desfaz_tarefa(tira_da_lista, desfeito)
            time.sleep(0.3)

        elif op == 4:
            lista, desfeito = refaz_tarefa(lista, desfeito)
            time.sleep(0.3)

        elif op == 5:
            print('\t\033[1;31mATÉ A PRÓXIMA...\033[m')
            break
        else:
            pass


# Considerações:

# 1- O programa atende a funcionalidade de não deixar vc fazer qualquer operação
# sem antes criar uma tarefa.

# 2- Tive algun problemas com as passagens de parâmetros no começo, mas após testar
# separadamente consegui atingir o resultado desejado.

