# Przygotuj program, który obliczy pole trójkąta o podanych
# trzech wierzchołkach. (O każdy wierzchołek pytaj osobno)
# 0.5 * ((x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)) - pole trójkąta to połowa z różnicy iloczynów

Xa = float(input(f'Podaj współrzędną pierwszego wierzchołka x1 '))
Ya = float(input(f'Podaj współrzędną pierwszego wierzchołka x2 '))
Xb = float(input(f'Podaj współrzędną pierwszego wierzchołka y1 '))
Yb = float(input(f'Podaj współrzędną pierwszego wierzchołka y2 '))
Xc = float(input(f'Podaj współrzędną pierwszego wierzchołka z1 '))
Yc = float(input(f'Podaj współrzędną pierwszego wierzchołka z2 '))
print(f"Wprowadzone przez Ciebie współprzędne wierzchołków to: Xa={Xa},Xb={Ya} ")
print(f"Wprowadzone przez Ciebie współprzędne wierzchołków to: Ya={Xb},Yb={Yb} ")
print(f"Wprowadzone przez Ciebie współprzędne wierzchołków to: Za={Xc},Zb={Ya} ")
VertexArea =  1/2 * ((Xb-Xa) * (Yc-Ya) - (Yb-Ya) * (Xc-Xa))
print(f"Pole trójkąta wynosi: {VertexArea} ")
