""" 
nome: Luccas Fialho dos Santos
curso: Análise e Desenvolvimento de Sistemas 
"""

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

def verificaCadastro(opcao, cod_estudante):
  jaCadastrado = False
  for estudante in lista[opcao-1]:
    if cod_estudante in estudante.values():
      jaCadastrado = True
      break
  return jaCadastrado

def incluirEstudante(opcao, cod_estudante):
  nome_estudante = input("Informe o nome do estudante: ")
  cpf_estudante = input("Informe o CPF do estudante: ")

  estudante = {}

  estudante["codigo"] = cod_estudante 
  estudante["nome"] = nome_estudante
  estudante["cpf"] = cpf_estudante

  lista[opcao-1].append(estudante)

def incluir(opcao):
  print("\n===== INCLUSÃO =====\n")
  
  codigo = int(input("Informe o código: "))
        
  if not verificaCadastro(opcao, codigo):
    if opcao == 1:
      incluirEstudante(opcao, codigo)
  else:
    print("\nCódigo já cadastrado!\n")
  
  input("Pressione ENTER para continuar.")
  print("\n")

def listarEstudantes(opcao):
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
    if opcao == 1:
      listarEstudantes(opcao)
  input("\nPressione ENTER para continuar.")
  print("\n")    

def editarEstudante(opcao):
  cod_estudante = int(input("Digite o código do estudante a ser alterado: "))
  flag = True
  for i in range(0, len(lista[opcao-1])):
    estudante = lista[opcao-1][i]
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
 
def editar(opcao):
  print("\n===== ALTERAÇÃO =====\n")
  if verificaVazia(lista, opcao):
    print("Não há nada cadastrado.\n")
  else:
    if opcao == 1:
      editarEstudante(opcao)
    
  input("Pressione ENTER para continuar...")
  print("\n")

def excluirEstudante(opcao):
  cod_estudante = int(input("Digite o código do estudante a ser excluído: "))
  flag = True
  for i in range(0, len(lista[opcao-1])):
    estudante = lista[opcao-1][i]
    if estudante["codigo"] == cod_estudante:
      flag = False
      lista[opcao-1].pop(i)
      print("\nEstudante deletado!\n")
      break
  if flag:
    print("\nEstudante não encontrado!\n")
 
def excluir(opcao):
  print("\n===== EXCLUSÃO =====\n")
  if verificaVazia(lista, opcao):
    print("Não há nada cadastrado.\n")
  else:
    if opcao == 1:
      excluirEstudante(opcao)
  input("Pressione ENTER para continuar...")
  print("\n") 
  
# loop principal do sistema
while True:
  estudantes = []
  turmas = []
  disciplinas = []
  professores = []
  matriculas = []
  
  lista.append(estudantes)
  lista.append(turmas)
  lista.append(disciplinas)
  lista.append(professores)
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
