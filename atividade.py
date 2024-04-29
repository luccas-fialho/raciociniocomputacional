""" 
nome: Luccas Fialho dos Santos
curso: Análise e Desenvolvimento de Sistemas 
"""

import json

dadosEstudantes = "estudantes.json"
dadosProfessores = "professores.json"
dadosDisciplinas = "disciplinas.json"
dadosTurmas = "turmas.json"
dadosMatriculas = "matriculas.json"

lista = []

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

def verificaCadastro(opcao, codigo):
  jaCadastrado = False
  for obj in lista[opcao-1]:
    if codigo in obj.values():
      jaCadastrado = True
      break
  return jaCadastrado

def recuperaJSON(nome_arquivo):
  try:
    with open(nome_arquivo, "r") as arquivo:
      lista = json.load(arquivo)
    return lista
  except:
    return []
  
def escreverJSON(lista, nome_arquivo):
  with open(nome_arquivo, "w") as arquivo:
    json.dump(lista, arquivo)

def incluirEstudanteOuProfessor(opcao, codigo):
  if opcao == 1:
    nome = input("Informe o nome do estudante: ")
    cpf = input("Informe o CPF do estudante: ")
  else:
    nome = input("Informe o nome do professor: ")
    cpf = input("Informe o CPF do professor: ")
  
  pessoa = {}

  pessoa["codigo"] = codigo
  pessoa["nome"] = nome
  pessoa["cpf"] = cpf
  
  lista[opcao-1].append(pessoa)
  if opcao == 1:
    escreverJSON(lista[opcao-1], dadosEstudantes)
  else:
    escreverJSON(lista[opcao-1], dadosProfessores)

def incluir(opcao):
  print("\n===== INCLUSÃO =====\n")
  
  codigo = int(input("Informe o código: "))
        
  if not verificaCadastro(opcao, codigo):
    if opcao == 1 or opcao == 2:
      incluirEstudanteOuProfessor(opcao, codigo)
  else:
    print("\nCódigo já cadastrado!\n")
  
  input("Pressione ENTER para continuar.")
  print("\n")

def listarEstudantesOuProfessores(opcao):
  print("Lista de Estudantes:" if opcao == 1 else "Lista de Professores:")
  for obj in lista[opcao-1]:
    cod = obj["codigo"]
    nome = obj["nome"]
    cpf = obj["cpf"]
    print(f"Código: {cod}, Nome: {nome}, CPF: {cpf}")

def verificaVazia(lista, opcao):
  return len(lista[opcao-1]) == 0

def listar(opcao):
  print("\n===== LISTAGEM =====\n")
  if verificaVazia(lista, opcao):
    print("Não há nada cadastrado ainda.")
  else:
    if opcao == 1 or opcao == 2:
      listarEstudantesOuProfessores(opcao)
  input("\nPressione ENTER para continuar.")
  print("\n")    

def editarEstudanteOuProfessor(opcao):
  if opcao == 1:
    codigo = int(input("Digite o código do estudante a ser alterado: "))
  else:
    codigo = int(input("Digite o código do professor a ser alterado: "))
  
  if verificaCadastro(opcao, codigo):
    for i in range(0, len(lista[opcao-1])):
      pessoa = lista[opcao-1][i]
      if pessoa["codigo"] == codigo:
        codigoPessoa = int(input("Informe o novo código: "))
        nome = input("Informe o novo nome: ")
        cpf = input("Informe o novo CPF: ")

        pessoa["codigo"] = codigoPessoa
        pessoa["nome"] = nome
        pessoa["cpf"] = cpf
        print("Informações alteradas!\n")
        break
  else:
    print("\nCódigo não encontrado!\n")
  
  escreverJSON(lista[opcao-1], dadosEstudantes) if opcao == 1 else escreverJSON(lista[opcao-1], dadosProfessores)
 
def editar(opcao):
  print("\n===== ALTERAÇÃO =====\n")
  if verificaVazia(lista, opcao):
    print("Não há nada cadastrado.\n")
  else:
    if opcao == 1 or opcao == 2:
      editarEstudanteOuProfessor(opcao)
    
  input("Pressione ENTER para continuar...")
  print("\n")

def excluirCadastro(opcao):
  codigo = int(input("Digite o código do cadastro a ser excluído: "))
  
  if verificaCadastro(opcao, codigo):
    for i in range(0, len(lista[opcao-1])):
      obj = lista[opcao-1][i]
      if obj["codigo"] == codigo:
        lista[opcao-1].pop(i)
        print("\nCadastro deletado!\n")
        break
  else:
    print("\nCadastro não encontrado!\n")
    
  if opcao == 1:
    escreverJSON(lista[opcao-1], dadosEstudantes)
  elif opcao == 2:
    escreverJSON(lista[opcao-1], dadosProfessores)
 
def excluir(opcao):
  print("\n===== EXCLUSÃO =====\n")
  if verificaVazia(lista, opcao):
    print("Não há nada cadastrado.\n")
  else:
    if opcao == 1 or opcao == 2:
      excluirCadastro(opcao)
  input("Pressione ENTER para continuar...")
  print("\n") 
  
# loop principal do sistema
while True:
  estudantes = recuperaJSON(dadosEstudantes)
  professores = recuperaJSON(dadosProfessores)
  disciplinas = []
  turmas = []
  matriculas = []
  
  lista.append(estudantes)
  lista.append(professores)
  lista.append(disciplinas)
  lista.append(turmas)
  lista.append(matriculas)
  
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
            incluir(opcao_gerenciamento)
          elif opcao_crud == 2:
            listar(opcao_gerenciamento)
          elif opcao_crud == 3:
            editar(opcao_gerenciamento)
          elif opcao_crud == 4:
            excluir(opcao_gerenciamento)
          else:
            print("\nOpção inválida! Digite novamente...\n")
        except ValueError:
          print("\nA opção deve ser um número!\n")
    elif opcao_gerenciamento == 2:
      while True:
        menuSecundario("professores")
        # Outro Try/Except para lidar com caracteres inválidos
        try:
          opcao_crud = int(input("Informe a opção desejada: "))
          if opcao_crud == 9:
            print("\nVoltando ao menu principal...\n")
            break
          elif opcao_crud == 1:
            incluir(opcao_gerenciamento)
          elif opcao_crud == 2:
            listar(opcao_gerenciamento)
          elif opcao_crud == 3:
            editar(opcao_gerenciamento)
          elif opcao_crud == 4:
            excluir(opcao_gerenciamento)
          else:
            print("\nOpção inválida! Digite novamente...\n")
        except ValueError:
          print("\nA opção deve ser um número!\n")
    elif opcao_gerenciamento == 3:
      print("EM DESENVOLVIMENTO\n")
    elif opcao_gerenciamento == 4:
      print("EM DESENVOLVIMENTO\n")
    elif opcao_gerenciamento == 5:
      print("EM DESENVOLVIMENTO\n")
    elif opcao_gerenciamento == 9:
      print("===== ATUALIZAÇÃO =====\n")
      print("Finalizando aplicação...")
      break
    else:
      print("Opção inválida! Digite novamente...\n")
  except ValueError:
    print("\nA opção deve ser um número!\n")
