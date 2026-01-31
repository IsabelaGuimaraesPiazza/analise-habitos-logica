dias = ["Seg", "Ter", "Qua", "Qui", "Sex"]
sono = [6, 8, 7, 5, 8]
estudo = [2, 4, 3, 1, 5]

produtividade = []

for i in range(len(dias)):
    if sono[i] < 7:
        produtividade.append("Baixa")
    elif sono[i] >= 7 and estudo[i] >= 3:
        produtividade.append("Alta")
    else:
        produtividade.append("Média")

for i in range(len(dias)):
    print(f"{dias[i]} - Produtividade: {produtividade[i]}")
