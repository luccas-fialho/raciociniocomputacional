""" 
nome: Luccas Fialho dos Santos
curso: Análise e Desenvolvimento de Sistemas 
"""

lista_estudantes = []

def menuPrincipal():
  print("----- MENU PRINCIPAL -----\n")
  print("(1) Gerenciar estudantes.")
  print("(2) Gerenciar professores.")
  print("(3) Gerenciar disciplinas.")
  print("(4) Gerenciar turmas.")
  print("(5) Gerenciar matrículas.")
  print("(9) Sair.\n")

def menuSecundario(contexto):
  print(f"***** [{contexto.upper()}] MENU DE OPERAÇÕES *****\n")
  print("(1) Incluir.")
  print("(2) Listar.")
  print("(3) Atualizar.")
  print("(4) Excluir.")
  print("(9) Voltar ao menu principal.\n")

def incluirEstudante():
  print("\n===== INCLUSÃO =====\n")
  jaCadastrado = False
  cod_estudante = int(input("Informe o código do estudante: "))

  for estudante in lista_estudantes:
    if cod_estudante in estudante.values():
      jaCadastrado = True
      break
            
  if not jaCadastrado:
    nome_estudante = input("Informe o nome do estudante: ")
    cpf_estudante = input("Informe o CPF do estudante: ")

    estudante = {}

    estudante["codigo"] = cod_estudante 
    estudante["nome"] = nome_estudante
    estudante["cpf"] = cpf_estudante

    lista_estudantes.append(estudante)
  else:
    print("\nCódigo de estudante já cadastrado!\n")
  
  input("Pressione ENTER para continuar.")
  print("\n")

def listarEstudantes():
  print("\n===== LISTAGEM =====\n")
  if len(lista_estudantes) == 0:
    print("Não há estudantes cadastrados.")
  else:
    for estudante in lista_estudantes:
      cod = estudante["codigo"]
      nome = estudante["nome"]
      cpf = estudante["cpf"]
      print(f"Código: {cod}, Nome: {nome}, CPF: {cpf}")
  input("\nPressione ENTER para continuar.")
  print("\n")    
  
def editarEstudante():
  print("\n===== ALTERAÇÃO =====\n")
  if len(lista_estudantes) == 0:
    print("Não há estudantes cadastrados.\n")
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
        print("Informações do estudante alteradas!\n")
        break
    if flag:
      print("\nEstudante não encontrado!\n")
  input("Pressione ENTER para continuar...")
  print("\n")
 
def excluirEstudante():
  print("\n===== EXCLUSÃO =====\n")
  if len(lista_estudantes) == 0:
    print("Não há estudantes cadastrados.\n")
  else:
    cod_estudante = int(input("Digite o código do estudante a ser excluído: "))
    flag = True
    for i in range(0, len(lista_estudantes)):
      estudante = lista_estudantes[i]
      if estudante["codigo"] == cod_estudante:
        flag = False
        lista_estudantes.pop(i)
        print("\nEstudante deletado!\n")
        break
    if flag:
      print("\nEstudante não encontrado!\n")
  input("Pressione ENTER para continuar...")
  print("\n") 
  
# loop principal do sistema
while True:
  menuPrincipal()

  # Try/Except para lidar com entrada de caracteres inválidos
  try:
    opcao_gerenciamento = int(input("Informe a opção desejada: "))
    print("\n")

    if opcao_gerenciamento == 1:
      while True:
        menuSecundario("estudantes")
        # Outro Try/Except para lidar com caracteres inválidos
        try:
          opcao_crud = int(input("Informe a opção desejada: "))
          if opcao_crud == 9:
            print("\nVoltando ao menu principal...\n")
            break
          elif opcao_crud == 1:
            incluirEstudante()
          elif opcao_crud == 2:
            listarEstudantes()
          elif opcao_crud == 3:
            editarEstudante()
          elif opcao_crud == 4:
            excluirEstudante()
          else:
            print("\nOpção inválida! Digite novamente...\n")
        except ValueError:
          print("\nA opção deve ser um número!\n")
    elif opcao_gerenciamento == 2 or opcao_gerenciamento == 3 or opcao_gerenciamento == 4 or opcao_gerenciamento == 5:
      print("EM DESENVOLVIMENTO\n")
    elif opcao_gerenciamento == 9:
      print("===== ATUALIZAÇÃO =====\n")
      print("Finalizando aplicação...")
      break
    else:
      print("Opção inválida! Digite novamente...\n")
  except ValueError:
    print("\nA opção deve ser um número!\n")
