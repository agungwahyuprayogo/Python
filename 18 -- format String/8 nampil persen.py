# cara nampilin persen di format

angka = 19
koma = 0.45

print(f"{koma:%}") 
# kalo make % doang, jadi 45.000000%
# gimana biar ga banyak
print(f"{koma:.2%}")
# kalo .2% berarti, jadiin persen tapi 2 angka setelah koma
# jadinya  45.00%
print(f"{koma:.3%}")
# kalo .2% jadi 45.000%
print(f"{koma:.0%}") 
# kalo cuman dikasih 0, jadinya 45%