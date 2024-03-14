# operasi biner

# not (~) 
# not kebanyakan kan anu ya, kalo 0 jadi 1, 1 jadi 0
# di operasi bitwise misalkan kita naro 1, kalo di not jadi -2
# kenapa -2? (ga bisa naro gambar njir)
# karena kalo minus dimulai dari -1 (0 ga bisa minus, makanya yg pertama dari -1)
# misal lain kalo kita not 9, jadi -10 karena minus pertama kali dari -1

a = 4
b = 6
c = -2
d = -5

print(f"{a} = ", format(a,"08b"))
print("--------------(~) not")
print(~a, " ", format(~a,"08b"),"\n")

print(f"{b} = ", format(b,"08b"))
print("--------------(~) not")
print(~b, " ", format(~b,"08b"),"\n")

print(f"{c} = ", format(c,"08b"))
print("--------------(~) not")
print(~c, " ", format(~c,"08b"),"\n")

print(f"{d} = ", format(d,"08b"))
print("--------------(~) not")
print(~d, " ", format(~d,"08b"),"\n")

"""
trus begimane biar 0 jadi 1 dan 1 jadi 0? 
kita flip dengan operasi XOR
"""

print("====FLIP====")
e = 0b11111111
print(f"{a} = ", format(a,"08b"))
print("--------------(V) not")
print(e^a, "", format(e^a,"08b"),"\n")

print(f"{b} = ", format(b,"08b"))
print("--------------(V) flip")
print(e^b, "", format(e^b,"08b"),"\n")

print(f"{c} = ", format(c,"08b"))
print("--------------(V) not")
print(e^c, "", format(e^c,"08b"),"\n")

print(f"{d} = ", format(d,"08b"))
print("--------------(V) not")
print(e^d, "", format(e^d,"08b"),"\n")

print("ternyata ga bisa buat angka minus")