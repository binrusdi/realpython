# Closure, fungsi yang berada di dalam fungsi (nested function)
"""
Fungsi bisa di deklarasikan didalam suatu fungsi. Penerapannya berguna pada kasus dimana blok kode perlu di eksekusi lebih dari satu kali, tapi 'eksekusinya hanya di dalam fungsi tertentu', atau 'stelah pemanggilan fungsi tertentu'.
"""

'''
Contoh, jika membuat fungsi 'pemrosesan_pesan()' yang di deklarasikan didalam fungsi 'buat_pemrosesan_pesan()', Maka:
- Fungsi pemrosesan_pesan() bisa diakses didalam fungsi buat_pemrosesan_pesan().
- Fungsi pemrosesan_pesan() juga bisa diakses dari luar fungsi buat_pemrosesan_pesan(), asalkan fungsi pemrosesan_pesan() tersebut dijadikan sebagai 'nilai balik fungsi buat_pemrosesan_pesan()' -> untuk kemudian ditampung didalam variable, lalu di eksekusi.
'''

def buat_pemrosesan_pesan(pesan):
    def pemrosesan_pesan(nama):
        print(f'Halo {nama}, {pesan}')
    return pemrosesan_pesan # referensi ke fungsi pemrosesan pesan

selamat_datang = buat_pemrosesan_pesan('Selamat datang') # Fungsi luar
selamat_tinggal = buat_pemrosesan_pesan(('Selamat tinggal'))

selamat_datang('Rusdiana') # Fungsi dalam
# Output: Halo Rusdiana, Selamat datang
selamat_tinggal('Dian')
# Output: Halo Dian, Selamat tinggal