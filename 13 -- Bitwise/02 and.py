# operasi biner

# and (&) 
# 0 dengan 0 = 0
# 0 dengan 1 = 0
# 1 dengan 0 = 0
# 1 dengan 1 = 1

a = 4
b = 6

print(f"{a} dengan biner {format(a,'08b')}")
print(f"{b} dengan biner {format(b,'08b')}")
print("-----------------------(&) atau and")
print(f"{a&b} ------------ {format(a&b,'08b')}")

print("\ninget jangan patokin 4 x 6 aturan 24,\ntapi fokus di binernya")

# biner mentok 128

masang1 = int(input("\nMasukan angka pertama : "))
masang2 = int(input("Masukan angka kedua : "))

print(f"{masang1}\n   dengan biner {format(masang1,'08b')} ")
print(f"{masang2}\n   dengan biner {format(masang2,'08b')} ")
print("------------------------(&) atau and")
print(f"{masang1&masang2} \n   ------------ {format(masang1&masang2,'08b')}")