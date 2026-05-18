import time
import os

# Membersihkan layar
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Menampilkan papan
def tampil(papan, n):
    clear()
    print("VISUALISASI N-QUEENS\n")

    for i in range(n):
        for j in range(n):
            if papan[i] == j:
                print(" Q ", end="")
            else:
                print(" . ", end="")
        print()

    time.sleep(0.3)

# Mengecek posisi aman
def aman(papan, baris, kolom):
    for i in range(baris):
        if papan[i] == kolom or \
           papan[i] - i == kolom - baris or \
           papan[i] + i == kolom + baris:
            return False
    return True

# Backtracking
def solve(papan, baris, n):
    if baris == n:
        tampil(papan, n)
        return True

    for kolom in range(n):

        if aman(papan, baris, kolom):
            papan[baris] = kolom
            tampil(papan, n)

            if solve(papan, baris + 1, n):
                return True

            # Backtracking
            papan[baris] = -1
            tampil(papan, n)

    return False

# Input ukuran papan
n = int(input("Masukkan ukuran papan: "))

# Inisialisasi papan
papan = [-1] * n

# Jalankan program
if solve(papan, 0, n):
    print("\nSolusi ditemukan!")
else:
    print("\nTidak ada solusi.")