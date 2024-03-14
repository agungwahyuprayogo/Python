from numpy import float16


print("=====INTERGER=====")

interger = 1
print(interger, type(interger)) # type buat ngecek tipe data di interger apa

print("")
flt = float(interger) # nama variable sebelumnya float, tapi malah jadi error 
#kalo bisa nama variablenya jangan float, nanti dibawah malah jadi error
string = str(interger)
boolean = bool(interger)

print(f"dari interger {interger} dengan tipe data ", type(interger),"\n")
# ga bakal berubah
print(f"ke float menjadi {flt}", type(flt))
# value dari variable yg awalnya 1 ketika diubah jadi float jadi 1.0
print(f"ke string menjadi {string}", type(string))
# tetep jadi 1 , hanya saja 1 disini menjadi karakter (dianggap huruf) karena string
print(f"ke boolean menjadi {boolean}", type(boolean))
# kalo nilainya 0 jadi false, selain 0 jadi true

"""
kalo ke float jadi ada tambahan .0 dibelakang
kalo ke string jadi sama, bedanya 0 string
kalo ke boolean, diluar angka 0 True 
"""

tdi = 10
print("\n\ntdi memiliki nilai =", tdi, "bertipe data", type(tdi))
print("") # ngasih jarak atau enter kalo di keyboard

tdf = float(tdi)
tds = str(tdi)
tdb = bool(tdi)

print("value dari tdf menjadi", tdf, "dengan tipe data", type(tdf))
print("value dari tds menjadi", tds, "dengan tipe data", type(tds))
print("value dari tdb menjadi", tdb, "dengan tipe data", type(tdb))

