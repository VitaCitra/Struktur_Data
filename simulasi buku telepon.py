# Simulasi Buku Telepon Sederhana

buku_telepon = {}

def tambah_kontak():
    nama = input("Masukkan nama: ")
    nomor = input("Masukkan nomor telepon: ")
    buku_telepon[nama] = nomor
    print("Kontak berhasil ditambahkan!\n")

def cari_kontak():
    nama = input("Masukkan nama yang dicari: ")
    if nama in buku_telepon:
        print(f"Nomor {nama} adalah {buku_telepon[nama]}\n")
    else:
        print("Kontak tidak ditemukan.\n")

def tampilkan_semua():
    if not buku_telepon:
        print("Buku telepon kosong.\n")
    else:
        print("Daftar Kontak:")
        for nama, nomor in buku_telepon.items():
            print(f"{nama} : {nomor}")
        print()

def menu():
    while True:
        print("=== MENU BUKU TELEPON ===")
        print("1. Tambah Kontak")
        print("2. Cari Kontak")
        print("3. Tampilkan Semua Kontak")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            tambah_kontak()
        elif pilihan == "2":
            cari_kontak()
        elif pilihan == "3":
            tampilkan_semua()
        elif pilihan == "4":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.\n")

menu()