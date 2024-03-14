# fahrenheit ke celcius 5/9 (F-32)
# fahrenheit ke reamur 4/9 (F-32)
# fahrenheit ke kelvin 5/9 (F-32) + 273

fahrenheit = int(input("masukan suhu fahrenheit : "))

celcius = (5/9) * (fahrenheit - 32)
print(celcius, "celcius")

reamur = (4/9) * (fahrenheit - 32)
print(reamur, "reamur")

kelvin = (fahrenheit - 32) * 5/9 + 273.15
print(kelvin, "kelvin")