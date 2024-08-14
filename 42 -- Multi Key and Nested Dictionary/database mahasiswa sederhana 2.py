import datetime as dt 

mahasiswa1 = {
    "Nama" : "Agung Wahyu Prayogo",
    "NIM" : 201910225300,
    "SKS" : 89,
    "Lahir" : dt.datetime(2000,5,12) #tahun, bulan, tanggal
}

mahasiswa2 = {
    "Nama" : "Martaulina Simanungkalit",
    "NIM" : 201910225298,
    "SKS" : 90,
    "Lahir" : dt.datetime(2001,7,15) #tahun, bulan, tanggal
}

mahasiswa3 = {
    "Nama" : "Tanti Krisfrida",
    "NIM" : 201910225399,
    "SKS" : 89,
    "Lahir" : dt.datetime(1999,1,1) #tahun, bulan, tanggal
}

# data 3 mahasiswa tadi, kita simpen di satu dict
data_mahasiswa = {
    "MHS001":mahasiswa1,
    "MHS002":mahasiswa2,
    "MHS003":mahasiswa3,
}

# kalo dict kan tiap tampil berantakan, kita rapihin kaya gini
print(f"{'KEY':^6} {'Nama':^25} {"NIM":^12} {"SKS":<4} {"Tggl Lahir" :<10}")
# string, dibikin kolom setara 3 baris gitu maksudnya
"""
jadi diatas itu bukan variable, bukan itung2an
tapi rata kiri

maksudnya? kaya bikin header di excel gitu, nama suatu kolom
nah key itu kan terdiri dari 3 huruf, nah di buat rata ke kiri 6
dengan cara :<6

kalo rata kanan :>6
kalo rata tengah gini :^6

"""
print("-".center(62,"-")) # buat garis tepi pemisah nama kolom biar rapi

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa # variable dalam for, jadi key ini variable yang valuenya tuh mahasiswa
    NAMA = data_mahasiswa[KEY]['Nama'] #variable juga, tapi valuenya dari key yang mahasiswa, dengan key "Nama"
    NIM = data_mahasiswa[KEY]['NIM']
    SKS = data_mahasiswa[KEY]['SKS']
    LAHIR = data_mahasiswa[KEY]['Lahir'].strftime("%x")

    print(f"{KEY:<6} {NAMA:<25} {NIM:<12} {SKS:<4} {LAHIR :^10}")

