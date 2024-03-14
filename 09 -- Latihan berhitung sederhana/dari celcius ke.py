# dari cecius ke reamur rumusnya 4/5 * C
# dari cecius ke farenheit rumusnya 9/5 * C
# dari cecius ke kelvin rumusnya C + 273

celcius = float(input("masukan suhu dalam celcius : "))
print("suhu", celcius, "celcius")

reamur = (4/5) * celcius
print(reamur, "reamur")

farenheit = ((9/5) * celcius) + 32
print(farenheit, "farenheit")

kelvin = celcius + 273.15
print(kelvin, "kelvin")