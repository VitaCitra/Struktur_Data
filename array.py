class FixedList:
    def __init__(self, size):
        """
        Membuat list dengan ukuran tetap.
        Semua elemen awalnya bernilai 0.
        """
        if size <= 0:
            raise ValueError("Ukuran harus lebih dari 0")
        self.size = size
        self.data = [0] * size

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index di luar batas")
        return self.data[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index di luar batas")
        self.data[index] = value

    def isi_semua(self, value):
        """Mengisi seluruh elemen dengan nilai tertentu."""
        for i in range(self.size):
            self.data[i] = value

    def tampil(self):
        """Menampilkan seluruh isi list."""
        for item in self.data:
            print(item)


# ==========================
# Contoh Penggunaan
# ==========================

# Membuat list dengan ukuran 6
angka = FixedList(6)

print("Jumlah elemen:", len(angka))

# Mengisi beberapa nilai berbeda
angka[0] = 2
angka[1] = 4
angka[2] = 6
angka[3] = 8
angka[4] = 10
angka[5] = 12

print("\nIsi list:")
angka.tampil()

# Mengambil elemen tertentu
print("\nElemen pada index 4:", angka[4])

# Mengubah semua isi menjadi 99
angka.isi_semua(99)

print("\nIsi list setelah diubah semua:")
angka.tampil()
