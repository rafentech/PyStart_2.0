# Lekcja 6 Zadanie 3
# Napisz program, który zapyta użytkownika o temperaturę.
# Jeśli będzie 10 stopni lub zimniej wypisz “zostań w domu”
# Jeśli będzie więcej niż 10, ale mniej niż 20 wypisz “weź kurtkę!”
# W każdym innym przypadku wypisz “Baw się dobrze”

temperature = int(input(f' Podaj aktualną temperaturę na zewnątrz: '))
if temperature <= 10:
    print('Zostań w domu')
elif 10 < temperature < 20:
    print('Weź kurtkę')
else:
    print('Baw się dobrze')
