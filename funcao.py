def area(comprimento, largura):
    area_terreno = comprimento * largura
    return area_terreno

cm = float(input("Digite o comprimento do terreno em metros: "))
lg = float(input("Digite a largura do terreno em metros: "))

resultado = area(comprimento, largura)
print("A área do terreno é:", resultado, "metros quadrados.")
