"""
bitwise itu kaya operasi biner
kek misalkan 2 kalo dibikin biner itu 0000 0010
5 binernya 0000 1001
gini dah 
1 = 0000 0001             5 = 0000 1001
2 = 0000 0010             6 = 0000 1010
3 = 0000 0011             7 = 0000 1110
4 = 0000 0100             8 = 0000 1111
"""
###################################################
"""
kek gitu, nah dibitwise, 
kita ngoperasiin biner make operator or (|) and (&) xor (^) not (~)

"""
###################################################
"""
 OR (|) 
 0 dengan 0 = 0
 0 dengan 1 = 1
 1 dengan 0 = 1
 1 dengan 1 = 1

 jadi ga bisa misalkan 6 or 4 = 10, ga, tapi liat operasi diatas
"""

a = 4
b = 6

print(f"{a} dengan biner",format(a,'08b'))
print(f"{b} dengan biner",format(b,'08b'))
print("-------------------------(|) atau or")
print(a|b,"------------", format(a|b,'08b'))

print("\ninget jangan patokin 4 + 6 aturan 10\ntapi fokus di binernya")

masang1 = int(input("\nMasukan angka pertama : "))
masang2 = int(input("Masukan angka kedua : "))

print(f"{masang1}\n   dengan biner {format(masang1,'08b')} ")
print(f"{masang2}\n   dengan biner {format(masang2,'08b')} ")
print("-------------------------(|) atau or")
print(f"{masang1|masang2} \n   ------------ {format(masang1|masang2,'08b')}")