numeros_quartos = list(range(101, 151))  # de 101 a 150
status_quartos = []
hospedes_quartos = []
dias_estadia = []

def status_dosQuarto():
    contador = 0
    while contador < 50:
        status_quartos.append("livre")
        hospedes_quartos.append("")
        dias_estadia.append(0)
        contador += 1
    print("Status dos quartos inicializado com sucesso.")
print("Quarto:", numeros_quartos[i])
print("Status:", status_quartos[i])
print("Hóspede:", hospedes_quartos[i])
print("Dias:", dias_estadia[i])

