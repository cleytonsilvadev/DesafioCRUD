import db
import mensagens as msg

def main():
   NOVA_TAREFA     = 1
   CONCLUIR_TAREFA = 2
   REMOVER_TAREFA =3
  
   while True:
       msg.exibir_cabecalho()
       msg.exibir_tarefas()
       try:
           # exibe as opções disponíveis
           opcao = int(input("O que deseja fazer? \n1 = Nova tarefa\n2 = Concluir tarefa  \n3 = Remover tarefa \n "))