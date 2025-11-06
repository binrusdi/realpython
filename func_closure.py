# Closure, fungsi yang berada di dalam fungsi (nested function)
"""
Fungsi bisa di deklarasikan didalam suatu fungsi. Penerapannya berguna pada kasus dimana blok kode perlu di eksekusi lebih dari satu kali, tapi 'eksekusinya hanya di dalam fungsi tertentu', atau 'stelah pemanggilan fungsi tertentu'.
"""

'''
Contoh, jika membuat fungsi 'inner()' yang di deklarasikan didalam fungsi 'outer()', Maka:
- FUngsi inner() bisa diakses didalam fungsi outer().
- Fungsi inner() juga bisa diakses dari luar fungsi outer(), asalkan fungsi inner() tersebut dijadikan sebagai 'nilai balik fungsi outer()' -> untuk kemudian ditampung didalam variable, lalu di eksekusi.
'''

def buat_pemrosesan_pesan(pesan):
    def pemrosesan_pesan(nama):
        print(f'Halo {nama}, {pesan}')
    return pemrosesan_pesan # referensi ke fungsi pemrosesan pesan

selamat_datang = buat_pemrosesan_pesan('Selamat datang')
selamat_tinggal = buat_pemrosesan_pesan(('Selamat tinggal'))

selamat_datang('Rusdiana')
# Output: Halo Rusdiana, Selamat datang
selamat_tinggal('Dian')
# Output: Halo Dian, Selamat tinggal