"""
misal kita pen make dalam sebuah percapakan ye kan

kalo awalnya make single, dalemnya double, diakhiri single lagi
kalo awalnya make double, dalemnya single, diakhiri double lagi
"""
print("ini make petik satu diawal, \npas di percakapan dikasih petik double")

awalSingle1 = '\n"Halo Apa Kabar?"'
awalSingle2 = '"Baik, kamu?"'
awalSingle3 = '"Alhamdulillah Baik Juga"'

print(f"{awalSingle1}\n{awalSingle2}\n{awalSingle3}")

print("\nkalo ini make petik double,\npas di percakapan dikasih petik satu")
awalDouble1 = "'Lama tidak bertemu'"
awalDouble2 = "'Iyanih, pengen ngajak pasti banyak alesan wkwk'"
awalDouble3 = "'haha iya soalnya aku ga pengen'"

print(f"\n\n{awalDouble1}\n{awalDouble2}\n{awalDouble3}")


campur = "\nhari ini adalah hari Jum'at"
print(campur)

# slash sebelum tanda kutip 
# buat ngasih tau kalo tanda kutip tersebut ga langsung mati / diakhir
campur2 = 'hari ini adalah hari Jum\'at'
print(campur2)