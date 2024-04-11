""" 
nome: Luccas Fialho dos Santos
curso: Análise e Desenvolvimento de Sistemas 
"""

lista_estudantes = []

# loop principal do sistema
while True:
  print("----- MENU PRINCIPAL -----")
  print("\n")
  print("(1) Gerenciar estudantes.")
  print("(2) Gerenciar professores.")
  print("(3) Gerenciar disciplinas.")
  print("(4) Gerenciar turmas.")
  print("(5) Gerenciar matrículas.")
  print("(9) Sair.")
  print("\n")

  # Try/Except para lidar com entrada de caracteres inválidos
  try:
    opcao_gerenciamento = int(input("Informe a opção desejada: "))
    print("\n")

    if opcao_gerenciamento == 1:
      while True:
        print("***** [ESTUDANTES] MENU DE OPERAÇÕES *****")
        print("\n")
        print("(1) Incluir.")
        print("(2) Listar.")
        print("(3) Atualizar.")
        print("(4) Excluir.")
        print("(9) Voltar ao menu principal.")
        print("\n")

        # Outro Try/Except para lidar com caracteres inválidos
        try:
          opcao_crud = int(input("Informe a opção desejada: "))

          if opcao_crud == 9:
            print("\n")
            print("Voltando ao menu principal...")
            print("\n")
            break
          elif opcao_crud == 1:
            print("\n")
            print("===== INCLUSÃO =====")
            print("\n")
            cod_estudante = 0
            nome_estudante = input("Informe o nome do estudante: ")
            cpf_estudante = input("Informe o CPF do estudante: ")

            dic = {}

            dic["codigo"] = cod_estudante + (len(lista_estudantes) + 1)
            dic["nome"] = nome_estudante
            dic["cpf"] = cpf_estudante

            lista_estudantes.append(dic)
            input("Pressione ENTER para continuar.")
            print("\n")
          elif opcao_crud == 2:
            print("\n")
            print("===== LISTAGEM =====")
            print("\n")
            if len(lista_estudantes) == 0:
              print("Não há estudantes cadastrados.")
              print("\n")
            else:
              for nome in lista_estudantes:
                print(f"- {nome}")
            input("Pressione ENTER para continuar.")
            print("\n")
          elif opcao_crud == 3:
            if len(lista_estudantes) == 0:
              print("Não há estudantes cadastrados.")
              print("\n")
            else:
              cod_estudante = int(input("Digite o código do estudante a ser alterado: "))
              flag = True
              for i in range(0, len(lista_estudantes)):
                estudante = lista_estudantes[i]
                if estudante["codigo"] == cod_estudante:
                  flag = False
                  cod_estudante = int(input("Informe o novo código do estudante: "))
                  nome_estudante = input("Informe o novo nome do estudante: ")
                  cpf_estudante = input("Informe o novo CPF do estudante: ")

                  estudante["codigo"] = cod_estudante
                  estudante["nome"] = nome_estudante
                  estudante["cpf"] = cpf_estudante
                  print("Estudante alterado!\n")
                  break
              if flag:
                print("Estudante não encontrado!\n")
              input("Pressione ENTER para continuar...")
          elif opcao_crud == 4:
            if len(lista_estudantes) == 0:
              print("Não há estudantes cadastrados.")
              print("\n")
            else:
              cod_estudante = int(input("Digite o código do estudante a ser excluído: "))
              flag = True
              for i in range(0, len(lista_estudantes)):
                estudante = lista_estudantes[i]
                if estudante["codigo"] == cod_estudante:
                  flag = False
                  lista_estudantes.pop(i)
                  print("Estudante deletado!\n")
                  break
              if flag:
                print("Estudante não encontrado!\n")
              input("Pressione ENTER para continuar...")
          else:
            print("\n")
            print("Opção inválida! Digite novamente...")
            print("\n")
        except ValueError:
          print("\n")
          print("A opção deve ser um número!")
          print("\n")
    elif opcao_gerenciamento == 2 or opcao_gerenciamento == 3 or opcao_gerenciamento == 4 or opcao_gerenciamento == 5:
      print("EM DESENVOLVIMENTO")
      print("\n")
    elif opcao_gerenciamento == 9:
      print("===== ATUALIZAÇÃO =====")
      print("\n")
      print("Finalizando aplicação...")
      break
    else:
      print("Opção inválida! Digite novamente...")
      print("\n")
  except ValueError:
    print("\n")
    print("A opção deve ser um número!")
    print("\n")
