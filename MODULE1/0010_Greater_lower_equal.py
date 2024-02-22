# Lekcja 6 Zadanie 2
# Odbierz od użytkownika dwie wartości. Porównaj je ze sobą.
# Sprawdź, która jest większa lub czy są sobie równe.


number1 = int(input(f'Podaj pierwszą liczbę: '))
number2 = int(input(f'Podaj drugą liczbę: '))
if number1 == number2:
    print(f'Liczba {number1} i {number2} są równe! ')
elif number1 > number2:
    print(f'Liczba {number1} jest większa od {number2}')
else:
    print(f'Liczba {number2} jest większa od {number1}')

