# Lekcja 7 Zadanie Domowe 1
# Przygotuj program, który zamieni stopnie w Celsjuszach na Fahrenheity
# T(°F) = T(°C) × 9/5 + 32

temperatureC = float(input(f'Podaj temperaturę w stopniach Celsjusza: '))
# print("Trwa przeliczanie...")

temperatureF = float(temperatureC * 9/5 + 32)
print(f"Podana przez Ciebie temperatura {temperatureC}C po przeliczeniu na Farenheity to: {temperatureF}F ")
