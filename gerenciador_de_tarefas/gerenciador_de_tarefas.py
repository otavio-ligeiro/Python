def verificar_existencia_da_tarefa(tarefa_pesquisada, tarefas):
    """Retorna se uma tarefa que está sendo pesquisada já existe no gerenciador.

    Args:
        tarefa_pesquisada (dict): dicionário correspondente a uma tarefa no gerenciador
        tarefas (list): lista que contém cada tarefa registrada pelo usuário

    Returns:
        boolean: retorna existência ou não de uma tarefa no gerenciador
    """
    for tarefa in tarefas:
        if tarefa_pesquisada == tarefa["nome_da_tarefa"]:
            return True

    return False


def adicionar_tarefa(tarefas):
    """
    Adiciona uma tarefa ao gerenciador de tarefas do usuário.

    Args:
        tarefas (list): lista que contém cada tarefa registrada pelo usuário
    """

    nome_da_tarefa = input("Digite a tarefa que deseja adicionar: ")
    existencia_da_tarefa = verificar_existencia_da_tarefa(nome_da_tarefa, tarefas)
    if existencia_da_tarefa is False:
        tarefa = {"nome_da_tarefa": nome_da_tarefa, "completa": False}
        tarefas.append(tarefa)
        print(f"A tarefa {nome_da_tarefa} foi adicionada ao seu gerenciador")
    else:
        print(f"A tarefa {nome_da_tarefa} já existe em seu gerenciador")


def ver_tarefas(tarefas):
    """
    Retorna todas as tarefas cadastradas no gerenciador do usuário.

    Args:
        tarefas (list): lista que contém cada tarefa registrada pelo usuário
    """

    for index, tarefa in enumerate(tarefas):
        if tarefa["completa"]:
            print(f"{index + 1}. [X] {tarefa['nome_da_tarefa']}")
        else:
            print(f"{index + 1}. [] {tarefa['nome_da_tarefa']}")


def atualizar_tarefa(tarefas):
    """
    Atualiza o nome da tarefa que o usuário deseja.

    Args:
        tarefas (list): lista que contém cada tarefa registrada pelo usuário
    """

    tarefa_a_ser_atualizada = input("Digite a tarefa que deseja atualizar: ")
    existencia_da_tarefa = verificar_existencia_da_tarefa(
        tarefa_a_ser_atualizada, tarefas
    )
    if existencia_da_tarefa is True:
        for tarefa in tarefas:
            if tarefa_a_ser_atualizada == tarefa["nome_da_tarefa"]:
                tarefa_atualizada = input("Atualize a tarefa: ")
                tarefa["nome_da_tarefa"] = tarefa_atualizada
                print(f"Tarefa atualizada: {tarefa_atualizada}")
            break
    else:
        print(
            f"A tarefa {tarefa_a_ser_atualizada} ainda não existe, logo não pode ser atualizada"
        )


def completar_tarefa(tarefas):
    """
    Completa uma determinada tarefa que o usuário deseja.

    Args:
        tarefas (list): lista que contém cada tarefa registrada pelo usuário
    """

    tarefa_a_ser_completada = input("Digite a tarefa que deseja atualizar: ")
    existencia_da_tarefa = verificar_existencia_da_tarefa(
        tarefa_a_ser_completada, tarefas
    )
    if existencia_da_tarefa:
        for tarefa in tarefas:
            if tarefa_a_ser_completada == tarefa["nome_da_tarefa"]:
                tarefa["completa"] = True
                print(f"Tarefa completa: [X] {tarefa_a_ser_completada}")
            break
    else:
        print(
            f"A tarefa {tarefa_a_ser_completada} ainda não existe, logo não pode ser completada"
        )


def deletar_tarefas_completas(tarefas):
    """
    Deleta todas as tarefas que estão completas do gerenciador.

    Args:
        tarefas (list): lista que contém cada tarefa registrada pelo usuário
    """

    tarefas = [tarefa for tarefa in tarefas if tarefa["completa"] is False]
    ver_tarefas(tarefas)


# Programa principal
tarefas = []
while True:
    print(
        """
          GERENCIADOR DE TAREFAS
          Menu:\n
          1. Adicionar tarefa
          2. Ver tarefas
          3. Atualizar tarefa
          4. Completar tarefa
          5. Deletar tarefas completas
          6. Sair
          """
    )

    try:
        acao_do_usuario = int(input("O que deseja fazer? "))
    except ValueError:
        print("Você inseriu uma opção inválida")

    if (acao_do_usuario < 1) or (acao_do_usuario > 6):
        print("Você inseriu uma opção que não existe no momento")
        continue

    match acao_do_usuario:
        case 1:
            adicionar_tarefa(tarefas)
        case 2:
            ver_tarefas(tarefas)
        case 3:
            atualizar_tarefa(tarefas)
        case 4:
            completar_tarefa(tarefas)
        case 5:
            deletar_tarefas_completas(tarefas)
        case 6:
            break
