nome, idade, estado = "Edynilson", 26, "PE"
if idade >= 18:
    print(f"{nome} é maior de idade")
else:
    print(f"{nome} é menor de idade")

if estado == "AC":
    print(f"Acre")
elif estado == "BA":
    print(f"Bahia")
elif estado == "PE":
    print(f"Pernambuco")
else:
    print(f"Inválido")