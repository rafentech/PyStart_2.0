# Lekcja 4 Zadanie 1
# Zapytaj użytkownika o wzrost i wagę i policz jego BMI
# BMI - masa w kg/(wzrost w metrach)2)

height = float(input('Ile masz wzrostu?'))
weight = float(input('Ile ważysz?'))
BMI = weight / ((height / 100) ** 2)
print(f'Dziękuję za podanie danych, Twoj wzrost to {height}, waga {weight} a BMI wynosi {BMI} ')
