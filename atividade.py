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

      opcao_crud = int(input("Informe a opção desejada: "))

      if opcao_crud == 9:
        print("\n")
        print("Voltando ao menu principal...")
        print("\n")
        break
      elif opcao_crud == 1 or opcao_crud == 2 or opcao_crud == 3 or opcao_crud == 4:
        print("\n")
        print(f"Você selecionou a opção {opcao_crud}")
        print("\n")
      else:
        print("\n")
        print("Opção inválida! Digite novamente...")
        print("\n")
  elif opcao_gerenciamento == 2:
    while True:
      print("***** [PROFESSORES] MENU DE OPERAÇÕES *****")
      print("\n")
      print("(1) Incluir.")
      print("(2) Listar.")
      print("(3) Atualizar.")
      print("(4) Excluir.")
      print("(9) Voltar ao menu principal.")
      print("\n")

      opcao_crud = int(input("Informe a opção desejada: "))

      if opcao_crud == 9:
        print("\n")
        print("Voltando ao menu principal...")
        print("\n")
        break
      elif opcao_crud == 1 or opcao_crud == 2 or opcao_crud == 3 or opcao_crud == 4:
        print("\n")
        print(f"Você selecionou a opção {opcao_crud}")
        print("\n")
      else:
        print("\n")
        print("Opção inválida! Digite novamente...")
        print("\n")
  elif opcao_gerenciamento == 3:
    while True:
      print("***** [DISCIPLINAS] MENU DE OPERAÇÕES *****")
      print("\n")
      print("(1) Incluir.")
      print("(2) Listar.")
      print("(3) Atualizar.")
      print("(4) Excluir.")
      print("(9) Voltar ao menu principal.")
      print("\n")

      opcao_crud = int(input("Informe a opção desejada: "))

      if opcao_crud == 9:
        print("\n")
        print("Voltando ao menu principal...")
        print("\n")
        break
      elif opcao_crud == 1 or opcao_crud == 2 or opcao_crud == 3 or opcao_crud == 4:
        print("\n")
        print(f"Você selecionou a opção {opcao_crud}")
        print("\n")
      else:
        print("\n")
        print("Opção inválida! Digite novamente...")
        print("\n")
  elif opcao_gerenciamento == 4:
    while True:
      print("***** [TURMAS] MENU DE OPERAÇÕES *****")
      print("\n")
      print("(1) Incluir.")
      print("(2) Listar.")
      print("(3) Atualizar.")
      print("(4) Excluir.")
      print("(9) Voltar ao menu principal.")
      print("\n")

      opcao_crud = int(input("Informe a opção desejada: "))

      if opcao_crud == 9:
        print("\n")
        print("Voltando ao menu principal...")
        print("\n")
        break
      elif opcao_crud == 1 or opcao_crud == 2 or opcao_crud == 3 or opcao_crud == 4:
        print("\n")
        print(f"Você selecionou a opção {opcao_crud}")
        print("\n")
      else:
        print("\n")
        print("Opção inválida! Digite novamente...")
        print("\n")
  elif opcao_gerenciamento == 5:
    while True:
      print("***** [MATRICULAS] MENU DE OPERAÇÕES *****")
      print("\n")
      print("(1) Incluir.")
      print("(2) Listar.")
      print("(3) Atualizar.")
      print("(4) Excluir.")
      print("(9) Voltar ao menu principal.")
      print("\n")

      opcao_crud = int(input("Informe a opção desejada: "))

      if opcao_crud == 9:
        print("\n")
        print("Voltando ao menu principal...")
        print("\n")
        break
      elif opcao_crud == 1 or opcao_crud == 2 or opcao_crud == 3 or opcao_crud == 4:
        print("\n")
        print(f"Você selecionou a opção {opcao_crud}")
        print("\n")
      else:
        print("\n")
        print("Opção inválida! Digite novamente...")
        print("\n")
  elif opcao_gerenciamento == 9:
    print("===== ATUALIZAÇÃO =====")
    print("\n")
    print("Finalizando aplicação...")
    break
  else:
    print("Opção inválida! Digite novamente...")
    print("\n")
