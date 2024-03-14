# ga cuman berlaku di operasi aritmatika, assignment juga bisa dilakukan di bitwise

#misal a = True
# a &= False = True (karena False and True = True)

a = False
print(f"a awal adalah {a}")

a &= False
print(f"setelah di and kan dengan 'False' menjadi '{a}'")

a &= True
print(f"setelah di and kan dengan 'True' menjadi '{a}'")

b = True
print(f"\nb awal adalah {b}")

b &= True
print(f"setelah di and kan dengan 'True' menjadi '{b}'")

b &= False
print(f"setelah di and kan dengan 'False' menjadi '{b}'")

