"""
di pembahasan yang kedua kali ini kita akan belajar mengenai continue
soal pemgambaran soal continue itu kek mana bisa liat video kelas terbuka
nomer 26 soal continue dan pass menit 03:45 / 07:28

jadi intinya sih kalo misalkan ada ada looping didalamnya ada continue
program yang ada di bawahnya akan diskip dan berlanjut ke program looping selanjutnya
jadi ya cabang yang ada di dalam cabang

biar gampang mahaminya kita buat program saja di bawah
"""

# kita buat variable gampang dulu masih sama kek maren maren
angka_1 = 0 # variable ini nilainya 0
print(f"sekarang adalah angka ke -> {angka_1}") # disini kita intro dulu angka di angka_1 tuh berapa

while angka_1 < 5: # masuk ke while, selama kalo masih kurang dari 5 maka akan ..
    angka_1 += 1 # nambah 1 angka tiap looping
    
    print(f"oke sekarang dah ke : {angka_1}") # nampilin angka sekarang
    print(f"okee") # nampilin print kedua selain angka sekarang

print("cukup\n")

"""
sekilas program diatas dimulai dari 0
ketika 0 kurang dari 5
angka selalu nambah 1 dan dibahawahnya ada tulisan oke skrg.. okee
kalo udah sampe 5 berhenti sampe tulisan cukup

nah sekarang kita liatin kalo ada continue jadinya seperti apa :
"""

angka2 = 0 # oke cukup ganti nama aja, value tetep 0
print(f"program 2".center(20,"-"))
print(f"sekarang adalah angka ke -> {angka2}") 

while angka2 < 5:
    angka2 += 1 
    
    print(f"oke sekarang dah ke : {angka2}") 

    if angka2 == 3: # bedanya disini, kalo angka dah sampe 3, maka :
        print("mantapp") # print mantap 
        continue # lalu continue, yang berarti program yg ada di bawah (okee) di skip

    print(f"okee") # yang ini ga ditampilin karena di skip, ada continue diatas

print("cukup")

"""
okee keliatan ga?? wkwkwk

oke jadi di program pertama kan kalo dah abis cetak angka ada tulisan okee sekarang.. lalu oke
nah berbeda kalo pas ada continue
keliatan disitu kalo udah sampe 3, oke skrg dah.. masih ada, karena diatas continue
sedangkan yg ada di bawah continue (okee) ga ada, soalnya tuh di skip langsung ke looping lagi

trus bagaimana kalo dipindah tulisan oke sekarang ..?
"""

angka3 = 0 # oke cukup ganti nama aja, value tetep 0
print(f"program 3".center(20,"-"))
print(f"sekarang adalah angka ke -> {angka3}") 

while angka3 < 5:
    angka3 += 1 
    

    if angka3 == 3: # bedanya disini, kalo angka dah sampe 3, maka :
        print("mantapp") # print mantap 
        continue # lalu continue, yang berarti program yg ada di bawah (okee) di skip

    print(f"oke sekarang dah ke : {angka3}") 
    print(f"okee") # yang ini ga ditampilin karena di skip, ada continue diatas

print("cukup")

"""
nah keliatan kan, tulisan oke sekarang ada di bawah continue dah ga dilanjutin lagi 
ya karena program apapun yang ada di bawah continue di skip

oke sekian terimakasih
"""