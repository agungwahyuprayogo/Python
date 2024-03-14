# ga cuman berlaku di operasi aritmatika, assignment juga bisa dilakukan di bitwise

#misal a = True
# a ^= False = True (karena False xor True = True)

# jadi true kalo berbeda

a = False
print(f"a awal adalah {a}")

a ^= False
print(f"setelah di xor kan dengan 'False' menjadi '{a}'")

a ^= True
print(f"setelah di xor kan dengan 'True' menjadi '{a}'")

b = True
print(f"\nb awal adalah {b}")

b ^= True
print(f"setelah di xor kan dengan 'True' menjadi '{b}'")

b ^= False
print(f"setelah di xor kan dengan 'False' menjadi '{b}'")
# disini jadi false karena sebelumnya hasilnya false di xor ke false, jadinya balik ke false