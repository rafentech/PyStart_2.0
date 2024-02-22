# Lekcja 6 Zadanie 5
# Zapytaj użytkownika o potrzebne dane i policz pole trapezu

a = int(input('podaj długość podstawy trapezu? '))
b = int(input('podaj długość drugiej podstawy trapezu? '))
h = int(input('podaj wysokość trapezu? '))
area = 1/2 * (a+b) * h
print(f'Pole trapezu o długości podstaw {a} oraz {b} oraz wysokości {h}, wynosi {area}')
