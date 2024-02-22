# Lekcja 6 Zadanie 1
# Odbierz od użytkownika liczbę. Wyświetl odpowiednią
# informację w zależności czy ta liczba jest parzysta.
# Liczba parzysta dzieli się przez 2 bez reszty.

number = int(input(f'Podaj liczbę, sprawdzimy czy jest parzysta: '))
if number % 2 == 0:
    print(f'Liczba {number} jest parzysta! ')
else:
    print(f'Liczba {number} jest nieparzysta! ')
