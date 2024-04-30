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
    while True:
        print(f"***** [{contexto.upper()}] MENU DE OPERAÇÕES *****\n")
        print("(1) Incluir.")
        print("(2) Listar.")
        print("(3) Atualizar.")
        print("(4) Excluir.")
        print("(9) Voltar ao menu principal.\n")
        # Outro Try/Except para lidar com caracteres inválidos
        try:
            opcao_crud = int(input("Informe a opção desejada: "))
            if opcao_crud == 9:
                print("\nVoltando ao menu principal...\n")
                break
            elif opcao_crud == 1:
                incluir(opcao_gerenciamento)
            elif opcao_crud == 2:
                listar(opcao_gerenciamento, contexto)
            elif opcao_crud == 3:
                editar(opcao_gerenciamento)
            elif opcao_crud == 4:
                excluir(opcao_gerenciamento)
            else:
                print("\nOpção inválida! Digite novamente...\n")
        except ValueError:
            print("\nA opção deve ser um número!\n")


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
        if not nome.isalpha():
            print("O nome deve conter apenas letras!")
            while not nome.isalpha():
                nome = input("Informe o nome do estudante: ")
        cpf = input("Informe o CPF do estudante: ")
        if cpf.isalpha():
            print("O CPF deve ser numérico!")
            while cpf.isalpha():
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


def incluirDisciplina(opcao, codigo):
    nome = input("Informe o nome da disciplina: ")

    disciplina = {}

    disciplina["codigo"] = codigo
    disciplina["nome"] = nome

    lista[opcao-1].append(disciplina)
    escreverJSON(lista[opcao-1], dadosDisciplinas)


def incluirTurma(opcao, codTurma):
    turma = {}
    turma["codigo"] = codTurma

    try:
        codProfessor = int(input("Informe o código do Professor: "))
        if not verificaCadastro(2, codProfessor):
            print("Nenhum professor com esse código encontrado!")
            return
        turma["codigo_professor"] = codProfessor
    except ValueError:
        print("Deve ser um número!")
        return

    try:
        codDisciplina = int(input("Informe o código da Disciplina "))
        if not verificaCadastro(3, codDisciplina):
            print("Nenhuma disciplina com esse código encontrada!")
            return
        turma["codigo_disciplina"] = codDisciplina
    except ValueError:
        print("Deve ser um número!")
        return

    lista[opcao-1].append(turma)
    escreverJSON(lista[opcao-1], dadosTurmas)


def incluirMatricula(opcao, codMatricula):
    matricula = {}
    matricula["codigo"] = codMatricula

    try:
        codTurma = int(input("Informe o código da turma: "))
        if not verificaCadastro(4, codTurma):
            print("Nenhuma turma com esse código encontrada!")
            return
        matricula["codigo_turma"] = codTurma
    except ValueError:
        print("Deve ser um número!")
        return

    try:
        codEstudante = int(input("Informe o código do estudante: "))
        if not verificaCadastro(1, codEstudante):
            print("Nenhum estudante com esse código encontrado!")
            return
        matricula["codigo_estudante"] = codEstudante
    except ValueError:
        print("Deve ser um número!")
        return

    lista[opcao-1].append(matricula)
    escreverJSON(lista[opcao-1], dadosMatriculas)


def incluir(opcao):
    print("\n===== INCLUSÃO =====\n")

    try:
        codigo = int(input("Informe o código: "))

        if verificaCadastro(opcao, codigo):
            print("\nCódigo já cadastrado!\n")
        else:
            if opcao == 1 or opcao == 2:
                incluirEstudanteOuProfessor(opcao, codigo)
            elif opcao == 3:
                incluirDisciplina(opcao, codigo)
            elif opcao == 4:
                incluirTurma(opcao, codigo)
            else:
                incluirMatricula(opcao, codigo)
    except ValueError:
        print("\nDeve ser um número!\n")

    input("Pressione ENTER para continuar.")
    print("\n")


def verificaVazia(lista, opcao):
    return len(lista[opcao-1]) == 0


def listar(opcao, contexto):
    print("\n===== LISTAGEM =====\n")
    if verificaVazia(lista, opcao):
        print("Não há nada cadastrado ainda.")
    else:
        print(f"Lista de {contexto}:")
        for obj in lista[opcao-1]:
            for chave, valor in obj.items():
                print(f"{chave.capitalize()}: {valor}", end=" ")
            print()
    input("\nPressione ENTER para continuar.")
    print("\n")


def editar(opcao):
    print("\n===== ALTERAÇÃO =====\n")
    if verificaVazia(lista, opcao):
        print("Não há nada cadastrado.\n")
    else:
        try:
            codigo = int(input("Digite o código a ser alterado: "))

            if verificaCadastro(opcao, codigo):
                for i in range(0, len(lista[opcao-1])):
                    obj = lista[opcao-1][i]
                    if obj["codigo"] == codigo:
                        codigoObj = int(input("Informe o novo código: "))
                        if verificaCadastro(opcao, codigoObj):
                            print("\nCódigo já cadastrado!\n")
                            return
                        if opcao == 1 or opcao == 2:
                            nome = input("Informe o novo nome: ")
                            cpf = input("Informe o novo CPF: ")
                            obj["cpf"] = cpf
                            obj["nome"] = nome
                        if opcao == 4:
                            codProfessor = int(
                                input("Informe o código do professor: "))
                            codDisciplina = int(
                                input("Informe o código da disciplina: "))
                            obj["codigo_professor"] = codProfessor
                            obj["codigo_disciplina"] = codDisciplina
                        if opcao == 5:
                            codTurma = int(
                                input("Informe o código da Turma: "))
                            codEstudante = int(
                                input("Informe o código do Estudante: "))
                            obj["codigo_turma"] = codTurma
                            obj["codigo_estudante"] = codEstudante

                        obj["codigo"] = codigoObj
                        print("Informações alteradas!\n")
                        break
            else:
                print("\nCódigo não encontrado!\n")
        except ValueError:
            print("Deve ser um número!")

    if opcao == 1:
        escreverJSON(lista[opcao-1], dadosEstudantes)
    elif opcao == 2:
        escreverJSON(lista[opcao-1], dadosProfessores)
    elif opcao == 3:
        escreverJSON(lista[opcao-1], dadosDisciplinas)
    elif opcao == 4:
        escreverJSON(lista[opcao-1], dadosTurmas)
    else:
        escreverJSON(lista[opcao-1], dadosMatriculas)

    input("Pressione ENTER para continuar...")
    print("\n")


def excluir(opcao):
    print("\n===== EXCLUSÃO =====\n")
    if verificaVazia(lista, opcao):
        print("Não há nada cadastrado.\n")
        return

    try:
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
            input("Pressione ENTER para continuar... ")
            return
    except ValueError:
        print("\nDeve ser um número!")

    if opcao == 1:
        escreverJSON(lista[opcao-1], dadosEstudantes)
    elif opcao == 2:
        escreverJSON(lista[opcao-1], dadosProfessores)
    elif opcao == 3:
        escreverJSON(lista[opcao-1], dadosDisciplinas)
    elif opcao == 4:
        escreverJSON(lista[opcao-1], dadosTurmas)
    else:
        escreverJSON(lista[opcao-1], dadosMatriculas)
    input("Pressione ENTER para continuar... ")
    print("\n")


# loop principal do sistema
while True:
    estudantes = recuperaJSON(dadosEstudantes)
    professores = recuperaJSON(dadosProfessores)
    disciplinas = recuperaJSON(dadosDisciplinas)
    turmas = recuperaJSON(dadosTurmas)
    matriculas = recuperaJSON(dadosMatriculas)

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
            menuSecundario("estudantes")
        elif opcao_gerenciamento == 2:
            menuSecundario("professores")
        elif opcao_gerenciamento == 3:
            menuSecundario("disciplinas")
        elif opcao_gerenciamento == 4:
            menuSecundario("turmas")
        elif opcao_gerenciamento == 5:
            menuSecundario("matriculas")
        elif opcao_gerenciamento == 9:
            print("===== ATUALIZAÇÃO =====\n")
            print("Finalizando aplicação...")
            break
        else:
            print("Opção inválida! Digite novamente...\n")
    except ValueError:
        print("\nA opção deve ser um número!\n")
