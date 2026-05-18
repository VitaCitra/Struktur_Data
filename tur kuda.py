import time
import os

N = 8

# Gerakan kuda
dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

# Membuat papan
papan = [[-1 for _ in range(N)] for _ in range(N)]

# Cek posisi valid
def aman(x, y):
    return 0 <= x < N and 0 <= y < N and papan[x][y] == -1

# Menampilkan papan bergerak
def tampil():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("VISUALISASI TUR KUDA\n")

    for baris in papan:
        for kotak in baris:
            if kotak == -1:
                print(" . ", end="")
            else:
                print(f"{kotak:2} ", end="")
        print()

    time.sleep(0.1)

# Algoritma backtracking
def solve(x, y, langkah):
    papan[x][y] = langkah
    tampil()

    # Semua kotak telah dikunjungi
    if langkah == N * N - 1:
        return True

    # Coba semua gerakan
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if aman(nx, ny):
            if solve(nx, ny, langkah + 1):
                return True

    # Backtracking
    papan[x][y] = -1
    return False

# Input posisi awal
x = int(input("Posisi awal X (0-7): "))
y = int(input("Posisi awal Y (0-7): "))

# Jalankan program
if solve(x, y, 0):
    print("\nTur Kuda berhasil ditemukan!")
else:
    print("\nTidak ada solusi.")