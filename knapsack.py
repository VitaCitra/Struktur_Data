import time
import os

barang = [2, 5, 6, 9, 12, 14, 20]
target = 30

# Membersihkan layar
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Menampilkan proses
def tampil(hasil, total, status):
    clear()

    print("VISUALISASI KNAPSACK\n")
    print("Barang tersedia :", barang)
    print("Target          :", target)
    print("\nBarang dipilih  :", hasil)
    print("Total berat     :", total)
    print("Status          :", status)

    time.sleep(0.5)

# Algoritma rekursif
def knapsack(i, total, hasil):

    tampil(hasil, total, "Mencoba")

    # Jika tepat target
    if total == target:
        tampil(hasil, total, "SOLUSI DITEMUKAN")
        return True

    # Jika melebihi target atau habis
    if total > target or i >= len(barang):
        tampil(hasil, total, "Backtracking")
        return False

    # Ambil barang
    if knapsack(i + 1,
                total + barang[i],
                hasil + [barang[i]]):
        return True

    # Tidak ambil barang
    if knapsack(i + 1,
                total,
                hasil):
        return True

    return False

# Jalankan program
if not knapsack(0, 0, []):
    print("\nTidak ada solusi")