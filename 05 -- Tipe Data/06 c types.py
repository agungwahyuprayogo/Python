"""
karena keterbatasan pyhton dalam mengolah data, apalagi di vscode dia hanya mampu
mengolah data int, string, float, boolean, komplex
tapi ga ada char (huruf) , long (angka banyak) , dll
kita bisa menambahkan nya dengan cara import dari luat
"""
# misalkan pen double
from ctypes import c_double, c
koma_panjang = c_double(9012301.0192651651)
print(koma_panjang, type(koma_panjang))

"""
pilihannya ada banyak selain c_double
ada : 
c_bool
c_int
c_int
c_float
dll

"""