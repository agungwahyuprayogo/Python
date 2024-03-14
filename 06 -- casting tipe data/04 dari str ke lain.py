print("===Dari String ke Tipe Data Laen===")

string = 10.999
print("nilai pada variable string adalah",string,"dan bertipe",type(string))

# ubah ke tipe data lain

interger = int(string)
flt = float(string)
boolean = bool(string)

print("nilai pada variable interger adalah",interger,"dan bertipe",type(string))
print("nilai pada variable flt adalah",flt,"dan bertipe",type(flt))
print("nilai pada variable boolean adalah",boolean,"dan bertipe",type(boolean))

# print("\n\n===Bakalan Error===")
# # error karena cuman bisa casting tipe data angka (ke int & float)
# # kek diatas
# # kalo casting dari huruf ke boolean masih bisa (hasilnya true)
# string = "agung"
# print("nilai pada variable string adalah",string,"dan bertipe",type(string))

# # ubah ke tipe data lain

# # interger = int(string)
# # flt = float(string)
# boolean = bool(string)

# # print("nilai pada variable interger adalah",interger,"dan bertipe",type(string))
# # print("nilai pada variable flt adalah",flt,"dan bertipe",type(flt))
# print("nilai pada variable boolean adalah",boolean,"dan bertipe",type(boolean))

