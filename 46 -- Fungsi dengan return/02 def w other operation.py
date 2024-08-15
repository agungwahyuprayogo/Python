"""
kita bisa naro def dalam operasi lain
langsung misal aja deh ya
"""

# kuadrat coba sebagai contoh
def kuadrat(angka):
    hasil_kuadrat = angka**2
    return hasil_kuadrat

z = 10 + kuadrat(5) # 10 + (5x5) = 10 + 25 = 35
print(z)

# def kubik(number):
#     hasil_kubik = number**3

# y = 10 + kubik(5)
# print(y)

"""
bener ternyata sepengaruh itu kalo ga make return
kalo kita run tuh yang y = 10 + kubik ...
muncul error gini
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
"""