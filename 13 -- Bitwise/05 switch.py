# beda dari operasi biner sebelumnya
# disini switch cuman ngegeser biner
# misal ada biner 4 = 0000 0100
# di switch >> 2 (digeser ke kanan 2x) maka jadi 0000 0001 (biner jadi 1)

# kalo 6 = 0000 0110
# >> 1 (digeser kanan 1x) maka jadi 0000 0011 (biner jadi 3)

# geser kiri begimane bang? angka dijadiin minus cok
# misal biner 6 
# >> -2 jadi 0001 1000

a = 4
b = 6

print(f"{a} binernya  ", format(a,'08b'))
print("---------------------(>>) shift 2x")
print(a>>2, "----------", format(a>>2,'08b'),"\n")

print(f"{b} binernya  ", format(b,'08b'))
print("---------------------(<<) shift 2x")
print(b>>2, "----------", format(b<<2,'08b'))