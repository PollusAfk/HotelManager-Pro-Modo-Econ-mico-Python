from InquirerPy import inquirer

def inicializar_hotel():
    global numeros_quartos, status_quartos, hospedes_quartos, dias_estadia
    numeros_quartos = list(range(101, 151))
    status_quartos = ["Livre"] * 50
    hospedes_quartos = [""] * 50
    dias_estadia = [0] * 50

def encontrar_indice_quarto(num_quarto, numeros_quartos):
    try:
        return numeros_quartos.index(num_quarto)
    except ValueError:
        return -1

def fazer_check_in(num_quarto, nome_hospede, num_dias, numeros_quartos, status_quartos, hospedes_quartos, dias_estadia):
    indice = encontrar_indice_quarto(num_quarto, numeros_quartos)
    if indice == -1:
        print("Número informado não encontrado, tente novamente")
        return
    elif status_quartos[indice] in ["Ocupado", "Limpeza"]:
        print("O quarto está ocupado ou sujo no momento, tente outro quarto")
        return
    else:
        hospedes_quartos[indice] = nome_hospede
        dias_estadia[indice] = num_dias
        status_quartos[indice] = "Ocupado"
        print("Check-in finalizado com sucesso !")

def fazer_check_out(num_quarto, numeros_quartos, status_quartos, hospedes_quartos, dias_estadia):
    indice = encontrar_indice_quarto(num_quarto, numeros_quartos)
    if indice == -1:
        print("Número informado não encontrado, tente novamente")
        return
    elif status_quartos[indice] == "Ocupado":
        hospedes_quartos[indice] = ""
        dias_estadia[indice] = 0
        status_quartos[indice] = "Limpeza"
        print("Check-out finalizado com sucesso !")
    else:
        print("O quarto já está livre ou está sujo, tente novamente revisando os dados!")
        return

def limpeza_quarto(num_quarto, numeros_quartos, status_quartos):
    indice = encontrar_indice_quarto(num_quarto, numeros_quartos)
    if indice == -1:
        print("Número informado não encontrado, tente novamente")
        return
    elif status_quartos[indice] in ["Limpeza", "Manutenção"]:
        status_quartos[indice] = "Livre"
        print("O quarto está limpo, pronto para receber novos hóspedes")
    else:
        print("O quarto não está disponível para limpeza")
        return

def vizualizar_ocupacao_especifica(num_quarto, hospedes_quartos, numeros_quartos, status_quartos, dias_estadia):
    indice = encontrar_indice_quarto(num_quarto, numeros_quartos)
    if indice == -1:
        print("Número informado não encontrado, tente novamente")
        return
    elif status_quartos[indice] == "Ocupado":
        print(f"O quarto {num_quarto} se encontra {status_quartos[indice]}, hospedando {hospedes_quartos[indice]}, por {dias_estadia[indice]} dias")
    else:
        print(f"O quarto {num_quarto}: se encontra {status_quartos[indice]}")

def vizualizar_ocupacoes(hospedes_quartos, numeros_quartos, status_quartos, dias_estadia):
    for i in range(50):
        if status_quartos[i] == "Ocupado":
            print(f"Quarto {numeros_quartos[i]}: {status_quartos[i]}, hospedando {hospedes_quartos[i]}, por {dias_estadia[i]} dias")
        else:
            print(f"Quarto {numeros_quartos[i]}: {status_quartos[i]}")

def menu():
    global opcao_menu
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
    if opcao_menu == "Vizualizar ocupações":
        vizualizar_ocupacoes(hospedes_quartos, numeros_quartos, status_quartos, dias_estadia)
    elif opcao_menu == "Vizualizar ocupação especifica":
        num_quarto = int(input("Qual o número do quarto? "))
        vizualizar_ocupacao_especifica(num_quarto, hospedes_quartos, numeros_quartos, status_quartos, dias_estadia)
    elif opcao_menu == "Fazer Check-in":
        num_quarto = int(input("Qual o número do quarto? "))
        nome_hospede = input("Qual o nome do hóspede? ")
        num_dias = int(input("Quantos dias de estadia? "))
        fazer_check_in(num_quarto, nome_hospede, num_dias, numeros_quartos, status_quartos, hospedes_quartos, dias_estadia)
    elif opcao_menu == "Fazer Check-out":
        num_quarto = int(input("Qual o número do quarto? "))
        fazer_check_out(num_quarto, numeros_quartos, status_quartos, hospedes_quartos, dias_estadia)
    elif opcao_menu == "Marcar quarto como limpo":
        num_quarto = int(input("Qual o número do quarto? "))
        limpeza_quarto(num_quarto, numeros_quartos, status_quartos)
    else:
        print("Saindo do sistema...")
    return opcao_menu

inicializar_hotel()
menu()
while opcao_menu != "Sair":
    menu()
