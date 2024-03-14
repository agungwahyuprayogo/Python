"""
oke kali ini kita akan membahas mengenai break

ya.. sesuai namanya break itu . hmm semacam berhenti gitu atau istirahat (break time)
jadi kalo misalkan kita dah sampe kondisi tertentu untuk break,
maka proses selanjutnya tidakk akan diteruskan karena kondisi tertentu tadi sudah tercapai

so, lets begin to learn about break
"""

angka = 0

while angka < 5:
    angka += 1
    print(f"Angka saat ini -> {angka}")

    if angka == 3:
        print(f"oke dah sampe angka {3}, berhenti")
        break

    print("siap")

print("cukup. berhenti")

"""
jadi kalo pas di run, angka cuman berhenti sampe 3
dan kalo udah sampe 3, kaga dilanjutin lagi
mau berapa pun while yg diminta, mau 100 kek atau berapa kek, 
tapi kalo ada break yang kondisinya terpenuhi, so semua program looping akan berhenti
"""

