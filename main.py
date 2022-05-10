# ETE PD
# Prof. Cloves
# Exemplo aula CRUD

# arquivo app.py

import db
import mensagens as msg

def main():
    NOVA_TAREFA     = 1
    CONCLUIR_TAREFA = 2
    REMOVER_TAREFA = 3
    
    while True:
        msg.exibir_cabecalho()
        msg.exibir_tarefas()
        try:
            # exibe as opções disponíveis
            opcao = int(input("O que deseja fazer? \n1 = Nova tarefa\n2 = Concluir tarefa  \n3 = Remover tarefa \n"))

            # verifica qual opção o usuário escolheu
            if opcao == NOVA_TAREFA:
                msg.mostrar_opcao_nova_tarefa()
            elif opcao == CONCLUIR_TAREFA:
                msg.mostrar_opcao_concluir_tarefa()
            elif opcao == REMOVER_TAREFA:
                msg.mostrar_opcao_remover_tarefa()
            else:
                print ("Opção não reconhecida, por favor informar um número")    
        except ValueError as e :
            print ("Opção não reconhecida, por favor informar um número")
        except Exception:
            exit(0)

if __name__ == "__main__":
    db.criar_tabela_todo()

    main()