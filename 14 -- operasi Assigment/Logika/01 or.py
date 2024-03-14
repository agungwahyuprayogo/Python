# ga cuman berlaku di operasi aritmatika, assignment juga bisa dilakukan di bitwise

#misal a = True
# a | False = True (karena False or True = True)

a = False
print(f"a awal adalah {a}")

a |= False
print(f"setelah di or kan dengan 'False' menjadi '{a}'")

a |= True
print(f"setelah di or kan dengan 'True' menjadi '{a}'")

a |= True
print(f"setelah di or kan dengan 'True' menjadi '{a}'")
