import datetime as dt   # import datetime buat format waktu di tanggal lahir
import os               # import os untuk tampilan clear dari terminal ketika run
import string           # tool key random data baru
import random           # tool yang membatu sring untuk membuat key dengan total huruf string sebanyak range(6 yang dibawah)


    # kita buat tamplate dulu, jadi kalo misal datanya ga dimasukin, data defaultnya kaya gini sesuai key nya
tamplate_mahasiswa = {
    "Nama" : "Nama",
    "NIM" : "000000000000",
    "SKS" :  00,
    "Lahir" : dt.datetime(1111,11,11)
}

data_mahasiswa = {} # ini namanya dict kosong kalo cuman '{}' doang

while True: # agar bisa ngulang isi data dengan pertanyaan , ulang? (y/n)
    # lalu kita buat dulu dictionary kosong yang fungsinya buat nyimpen dict kosong sementara tiap input data dict baru

    os.system("cls") # supaya terminal bersih ketika run dari tulisan python

    # kita buat seakan akan ada header diatasnya buat input data baru ke dictionary
    print(f"{"SELAMAT DATANG":^20}")    # kalimat selamat datang, dibuat rata tengah dari total space 20
    print(f"{"DATA MAHASISWA":^20}")
    print(f"-"*20)                      # seolah olah pembatas garis dan 2 tulisan diatas

    # buat variable mahasiswa, yg nyimpen dictionary baru dari inputan berdasarkan key
    mahasiswa = dict.fromkeys(tamplate_mahasiswa.keys()) 
    # jadi variable mahasiswa berdasarkan key dictionary tamplate_mahasiswa

    # lalu kita break down semua keys
    mahasiswa["Nama"] = input("Masukan Nama Anda : ")
    mahasiswa["NIM"] = input("Masukan NIM Anda : ")
    mahasiswa["SKS"] = int(input("Masukan Total SKS Yang Sudah Anda Tempuh : "))
    # untuk tanggal lahir sedikit berbeda, kita harus memecahnya dalam tahun, bulan dan tanggal
    TAHUN_LAHIR = int(input("Input Tahun Kelahiran (YYYY) : "))
    BULAN_LAHIR = int(input("Input Bulan Kelahiran (1-12) : "))
    TANGGAL_LAHIR = int(input("Input Tanggal Kelahiran (1-31) : "))
    # lalu dari 3 variable diatas, dimasukan dalam key mahasiswa
    mahasiswa["Lahir"] = dt.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

    # buat key, dengar string dengan kode ascii random UPPERCASE (huruf besar) dengan banyaknya angka sebanyak 6 buah
    KEY = "".join((random.choice(string.ascii_uppercase) for i in range(6))) # bahasa lainnya gini, kita buat string random yang terdiri dari 6 huruf 
    data_mahasiswa.update({KEY:mahasiswa}) # sebelumnya 'key', datanya ga update dean selalu ketimpa sama data baru gegara 'key' nya itu. makanya diatas dibuat random
    # contoh random key tuh kaya 
 
    # dari tutorial sebelumnya
    print(f"{"KEY":^6} {"Nama":^25} {"NIM":^12} {"SKS":<4} {"Tggl Lahir" :^10}")
    print('-'*60)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        
        NAMA = data_mahasiswa[KEY]["Nama"]
        NIM = data_mahasiswa[KEY]["NIM"]
        SKS = data_mahasiswa[KEY]["SKS"]
        LAHIR = data_mahasiswa[KEY]["Lahir"].strftime("%x")

        print(f"{KEY:^6} {NAMA:^25} {NIM:^12} {SKS:<4} {LAHIR :^10}")

    lanjut_ga = input("Ingin Memasukan Data Lagi? (y/n)")
    if lanjut_ga.lower() != 'y':
        break