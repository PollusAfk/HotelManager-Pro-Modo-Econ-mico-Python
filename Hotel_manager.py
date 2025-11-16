from InquirerPy import inquirer

# Função do menu principal, mostra as opções e retorna o que o usuário escolheu
def menu():
    opcao_menu = inquirer.select(
        message="\n=== HOTEL MANAGER PRO ===\n",
        choices=[
            "Fazer Check-in",
            "Fazer Check-out",
            "Marcar quarto como limpo",
            "Vizualizar ocupações",
            "Vizualizar ocupação especifica",
            "Sair"
        ]
    ).execute()
    return opcao_menu  # retorno da opção escolhida


# Função pra iniciar todas as listas do hotel (quartos, status, hóspedes e dias)
def inicializar_hotel():
    # usando global pra acessar essas listas no programa inteiro
    global numeros_quartos, status_quartos, hospedes_quartos, dias_estadia
    
    # criando a lista de quartos de 101 até 150
    numeros_quartos = list(range(101, 151))
    
    # marcando todos os quartos como livres no início
    status_quartos = ["Livre"] * 50
    
    # lista vazia onde vou armazenar o nome do hóspede
    hospedes_quartos = [""] * 50
    
    # lista que armazena quantos dias ele vai ficar
    dias_estadia = [0] * 50


# Função pra achar o índice do quarto dentro da lista de quartos
def encontrar_indice_quarto(num_quarto, numeros_quartos):
    try:
        # retorna o índice do quarto dentro da lista
        return numeros_quartos.index(num_quarto)
    except ValueError:
        # caso o número do quarto não exista
        return -1


# Função para realizar o check-in
def fazer_check_in(num_quarto, nome_hospede, num_dias, numeros_quartos, status_quartos, hospedes_quartos, dias_estadia):
    # pegando o índice do quarto
    indice = encontrar_indice_quarto(num_quarto, numeros_quartos)
    
    # se o quarto não existe
    if indice == -1:
        print("Número informado não encontrado, tente novamente")
        return
    
    # se o quarto já está ocupado ou sujo
    elif status_quartos[indice] in ["Ocupado", "Limpeza"]:
        print("O quarto está ocupado ou sujo no momento, tente outro quarto")
        return
    
    # se estiver livre
    else:
        hospedes_quartos[indice] = nome_hospede     # guarda o nome do hóspede
        dias_estadia[indice] = num_dias             # guarda quantos dias ele vai ficar
        status_quartos[indice] = "Ocupado"          # marca como ocupado
        print("Check-in finalizado com sucesso !")


# Função para fazer check-out
def fazer_check_out(num_quarto, numeros_quartos, status_quartos, hospedes_quartos, dias_estadia):
    indice = encontrar_indice_quarto(num_quarto, numeros_quartos)
    
    # se o quarto não existe
    if indice == -1:
        print("Número informado não encontrado, tente novamente")
        return

    # se está ocupado (pode fazer check-out)
    elif status_quartos[indice] == "Ocupado":
        hospedes_quartos[indice] = ""     # limpa o hóspede
        dias_estadia[indice] = 0          # zera os dias
        status_quartos[indice] = "Limpeza" # marca como sujo para limpeza
        print("Check-out finalizado com sucesso !")
    
    # se não está ocupado
    else:
        print("O quarto já está livre ou está sujo, tente novamente revisando os dados!")
        return


# Função para confirmar que o quarto foi limpo
def limpeza_quarto(num_quarto, numeros_quartos, status_quartos):
    indice = encontrar_indice_quarto(num_quarto, numeros_quartos)
    
    # caso o quarto não exista
    if indice == -1:
        print("Número informado não encontrado, tente novamente")
        return
    
    # se o quarto está marcado como limpeza ou manutenção
    elif status_quartos[indice] in ["Limpeza", "Manutenção"]:
        status_quartos[indice] = "Livre"   # libera o quarto
        print("O quarto está limpo, pronto para receber novos hóspedes")
    
    # se o quarto não estava marcado para limpeza
    else:
        print("O quarto não está disponível para limpeza")
        return


# Função para visualizar a ocupação de um único quarto
def vizualizar_ocupacao_especifica(num_quarto, hospedes_quartos, numeros_quartos, status_quartos, dias_estadia):
    indice = encontrar_indice_quarto(num_quarto, numeros_quartos)
    
    # caso o quarto não exista
    if indice == -1:
        print("Número informado não encontrado, tente novamente")
        return
    
    # se está ocupado, mostra todos os detalhes
    elif status_quartos[indice] == "Ocupado":
        print(f"O quarto {num_quarto} se encontra {status_quartos[indice]}, hospedando {hospedes_quartos[indice]}, por {dias_estadia[indice]} dias")
    
    # se não estiver ocupado, só mostra o status
    else:
        print(f"O quarto {num_quarto} se encontra {status_quartos[indice]}")


# Função pra listar todos os quartos com seus status
def vizualizar_ocupacoes(hospedes_quartos, numeros_quartos, status_quartos, dias_estadia):
    for i in range(50):
        # se o quarto estiver ocupado, mostra quem está hospedado e por quantos dias
        if status_quartos[i] == "Ocupado":
            print(f"Quarto {numeros_quartos[i]}: {status_quartos[i]}, hospedando {hospedes_quartos[i]}, por {dias_estadia[i]} dias")
        
        # se estiver livre ou sujo, só mostra o status
        else:
            print(f"Quarto {numeros_quartos[i]}: {status_quartos[i]}")
