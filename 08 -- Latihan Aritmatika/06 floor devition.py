# hampir mirip dengan pembagian, hanya saja hasilnya dibulatkan kebawah
# cara kerjanya nampilin hasil yang kehitung aja
# mmisal 10 : 3 kan harusnya 3,3333 kan 
# nah kalo make floor devition ga ada koma koma dibekalang
# jadi cuman nampilin 3 aja

print("floor divition yee..")
angka1 = int(input("masukan angka pertama : "))
angka2 = int(input("masukan angka kedua : "))
hasil = angka1 // angka2
print(f"{angka1} // {angka2} = {hasil}")