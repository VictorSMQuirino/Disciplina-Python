import os
import platform

ToDoList = []
resposta = '1'
ids = 1
opcao = ''
def menu():
    limpaTerminal()
    print('1 - Registrar uma tarefa')
    print('2 - Editar uma tarefa')
    print('3 - Listar as tarefas')
    print('4 - Marcar uma tarefa como realizada')
    print('0 - Encerrar o programa')
    print('Digite uma opção:')
    op = input()

    return op

def limpaTerminal():
    so = platform.system()
    if so == "Windows":
        os.system('cls')
    else:
        os.system('clear')

while(opcao != '0'):
    opcao = menu()
    match opcao:
        case '1':
            limpaTerminal()
            print('Digite o nome da tarefa')
            nome = input()
            while(nome == ''):
                nome = input()
                if(nome == ''):
                    print('Digite um nome para a tarefa!')
            ToDoList.append([ids, ' ' + nome + ' ', '[ ]'])
            ids += 1
        case '2':
            limpaTerminal()
            if len(ToDoList) == 0:
                print('A lista de tarefas esta vazia!')
                print('Tecle enter para continuar...')
                input()
            else:
                print('Digite o id da tarefa:')
                id = input()
                encontrou = False

                for tarefa in ToDoList:
                    if str(tarefa[0]) == id:
                        print('Digite um novo nome para a tarefa')
                        nome = input()
                        tarefa[1] = ' ' + nome + ' '
                        encontrou = True
                        break

                if encontrou == False:
                    print('Nao existe uma tarefa com esse id!')
        case '3':
            limpaTerminal()
            if len(ToDoList) == 0:
                print('A lista de tarefas esta vazia!')
                print('Tecle enter para continuar...')
                input()
            else:
                print('Lista de tarefas:')
                for tarefa in ToDoList:
                    print(tarefa[0], tarefa[1], tarefa[2])
                print('Tecle enter para continuar...')
                input()
        case '4':
            limpaTerminal()
            if len(ToDoList) == 0:
                print('A lista de tarefas esta vazia!')
                print('Tecle enter para continuar...')
                input()
            else:
                print('Digite o id da tarefa:')
                id = input()
                encontrou = False

                for tarefa in ToDoList:
                    if str(tarefa[0]) == id:
                        tarefa[2] = '[X]'
                        encontrou = True
                        break

                if encontrou == False:
                    print('Nao existe uma tarefa com esse id!')
                    print('Tecle enter para continuar...')
                    input()
        case '0':
            limpaTerminal()
            print('Programa encerrado')
        case _:
            limpaTerminal()
            print('Entrada inválida')
            print('Tecle enter para continuar...')
            input()

