"""
indexing
inget, index selalu dimulai dari 0

jadi misal 
agung
index ke-0 dari agung? jawabanya "a"
"""

nama = "agung wahyu prayogo"

index1 = 0
print(f"index ke {index1} di {nama} berada di", nama[0])

index2 = 1
print(f"index ke {index2} di {nama} berada di", nama[1])

index3 = -1
print(f"index ke {index3} di {nama} berada di", nama[-1])

index4 = 4
print(f"index ke {index4} di {nama} berada di", nama[4])

index5 = -4
print(f"index ke {index5} di {nama} berada di", nama[-4])


masnam = input("Masukan nama anda \n : ")
masdex = int(input("Index keberapa yang ingin dilihat? \n :"))

print(f"nama anda adalah {masnam}, dan index yang ingin dicari adalah {masdex}, maka index dari {masdex} adalah huruf '{masnam[masdex]}'")