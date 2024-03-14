# operasi Logika dan Boolean
# not , or , and , xor

# XOR ^

# akan true jika boolean berbeda

lgk_1 = False
lgk_2 = True

print(f"nilai dari variable lgk_1 adalah {lgk_1} \nnilai dari variable lgk_2 adalah {lgk_2}")
print(f"jika dibandingkan dengan xor maka akan seperti ini :\n\n")
print(f"jika {lgk_1} xor {lgk_1} maka menjadi : {lgk_1 ^ lgk_1}")
print(f"jika {lgk_1} xor {lgk_2} maka menjadi : {lgk_1 ^ lgk_2}")
print(f"jika {lgk_2} xor {lgk_1} maka menjadi : {lgk_2 ^ lgk_1}")
print(f"jika {lgk_2} xor {lgk_2} maka menjadi : {lgk_2 ^ lgk_2}")