'''\
# Author: ardianpramana
#
# 1. Bilangan prima hanya bisa dibagi 1 dan bilangan itu sendiri
# 2. Bilangan prima dimulai dari 2
# 3. Pilih angka x, bandingkan x dengan rentang angka dibawahnya (2 sampai x-1)
# 
# Contoh dibawah ini merupakan program mencetak 20 bilangan prima
#
'''

jml = 0
bil = 0 # inisiasi bilangan prima dimulai dari 2

while jml < 20:
    isPrima = True               # reset boolean isPrima tiap perulangan/ pencarian bilangan prima

    if  bil == 0 or bil == 1:
        isPrima = False

    for i in range(2,bil):       # [2,3,...,bil - 1]
        if bil % i == 0:         # Jika ada bilangan yang habis dibagi bilangan lain selain 1 dan bil
            isPrima = False      
            break                # Keluar dari iterasi for loop
    if isPrima:                  # Jika isPrima tetap True, maka bil dicetak
        print bil,
        jml += 1                 # Tambah jumlah bilangan prima yang berhasil ditemukan
    bil += 1                     # Tambah nilai bil untuk iterasi selanjutnya
