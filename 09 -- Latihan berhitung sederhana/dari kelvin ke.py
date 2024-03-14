#dari kelvin ke celcius K-273
# dari kelvin ke reamur (4/5 * kelvin) - 273
# dari kelvin ke fahrenheit ((9/5) * (kelvin - 273) + 32)

kelvin = int(input("masukan suhu kelvin : "))

celcius = kelvin - 273
print(celcius,"celcius")

reamur = ((4/5) * (kelvin - 273))
print(reamur,"reamur")

fahrenheit = ((9/5) * (kelvin - 273)) + 32
print(fahrenheit, "fahrenheit")