from InquirerPy import inquirer


def menu():
    opcao_menu = inquirer.select(
        message="\n=== HOTEL MANAGER PRO ===\n",
        choices=["Fazer Check-in", "Fazer Check-out", "Marcar quarto como limpo","Vizualizar ocupação", "Sair"]
    ).execute()

def inicializar_hotel():
    numeros_quartos = list(range(101, 151))
    status_quartos = ["livre"] * 50
    hospedes_quartos = [""] * 50
    dias_estadia = [0] * 50

def encontrar_indice_quarto(num_quarto, numeros_quartos):
    try:
        indice_quarto = numeros_quartos.index(num_quarto)
        return indice_quarto
    except ValueError:
        return -1