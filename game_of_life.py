import time

# Ukuran papan (berbeda dari sebelumnya)
TINGGI = 5
LEBAR = 7

# 0 = mati, 1 = hidup
grid = [
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [1, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0]
]

def tampil(grid):
    for baris in grid:
        for sel in baris:
            if sel == 1:
                print("*", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

def cek_tetangga(grid, r, c):
    jumlah = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            
            nr = r + i
            nc = c + j
            
            if 0 <= nr < TINGGI and 0 <= nc < LEBAR:
                jumlah += grid[nr][nc]
    return jumlah

def update_generasi(grid):
    papan_baru = []
    
    for r in range(TINGGI):
        baris = []
        for c in range(LEBAR):
            tetangga = cek_tetangga(grid, r, c)
            
            if grid[r][c] == 1:
                if tetangga == 2 or tetangga == 3:
                    baris.append(1)
                else:
                    baris.append(0)
            else:
                if tetangga == 3:
                    baris.append(1)
                else:
                    baris.append(0)
        
        papan_baru.append(baris)
    
    return papan_baru


# Jalankan simulasi (lebih banyak generasi)
for generasi in range(6):
    print("Generasi ke-", generasi)
    tampil(grid)
    grid = update_generasi(grid)
    time.sleep(1)
