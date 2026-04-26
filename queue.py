import time
import random
import os
from collections import deque

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# =============================
# VISUAL QUEUE
# =============================
def show_queue(q, title="QUEUE"):
    clear()
    print(f"=== {title} ===")
    print("FRONT -> ", end="")
    for item in q:
        print(f"[{item}]", end=" ")
    print("<- REAR")
    time.sleep(1)

# =============================
# KASUS 1: PRINTER QUEUE
# =============================
def printer_queue():
    q = deque(["laporan.pdf", "tugas.docx", "foto.jpg"])
    while q:
        show_queue(q, "Printer Queue")
        print(f"Mencetak: {q[0]}")
        time.sleep(1)
        q.popleft()
    print("Semua selesai!")
    time.sleep(2)

# =============================
# KASUS 2: HOT POTATO
# =============================
def hot_potato():
    q = deque(["A", "B", "C", "D", "E"])
    num = 3

    while len(q) > 1:
        for _ in range(num):
            q.append(q.popleft())
            show_queue(q, "Hot Potato (Oper)")
        print(f"{q[0]} tersingkir!")
        q.popleft()
        time.sleep(1)

    print(f"Pemenang: {q[0]}")
    time.sleep(2)

# =============================
# KASUS 3: ANTRIAN RS (PRIORITY)
# =============================
def hospital_queue():
    pq = [
        ("Budi", 3),
        ("Ani", 0),
        ("Citra", 2),
        ("Dedi", 0),
        ("Eka", 1)
    ]

    pq.sort(key=lambda x: x[1])  # urut prioritas

    for patient in pq:
        clear()
        print("=== ANTRIAN RS ===")
        for p in pq:
            print(f"{p[0]} (prioritas {p[1]})")
        print(f"\nDipanggil: {patient[0]}")
        time.sleep(1)

    print("Semua pasien selesai!")
    time.sleep(2)

# =============================
# KASUS 4: BFS
# =============================
def bfs_visual():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': [],
        'F': []
    }

    visited = set()
    q = deque(['A'])
    visited.add('A')

    while q:
        show_queue(q, "BFS Queue")
        node = q.popleft()
        print(f"Proses: {node}")
        time.sleep(1)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)

# =============================
# KASUS 5: SIMULASI LOKET
# =============================
def ticket_simulation():
    q = deque()
    agents = [0, 0]  # waktu sisa tiap agen

    for t in range(10):
        clear()
        print(f"Waktu: {t}")

        # kedatangan random
        if random.random() < 0.5:
            q.append(f"P{t}")
            print(f"Penumpang datang: P{t}")

        # agen melayani
        for i in range(len(agents)):
            if agents[i] == 0 and q:
                customer = q.popleft()
                agents[i] = random.randint(1, 3)
                print(f"Agen {i} melayani {customer}")

            if agents[i] > 0:
                agents[i] -= 1

        show_queue(q, "Antrian Tiket")

# =============================
# MAIN MENU
# =============================
while True:
    clear()
    print("=== VISUALISASI QUEUE ===")
    print("1. Printer Queue")
    print("2. Hot Potato")
    print("3. Antrian Rumah Sakit")
    print("4. BFS")
    print("5. Simulasi Loket")
    print("0. Keluar")

    pilih = input("Pilih: ")

    if pilih == "1":
        printer_queue()
    elif pilih == "2":
        hot_potato()
    elif pilih == "3":
        hospital_queue()
    elif pilih == "4":
        bfs_visual()
    elif pilih == "5":
        ticket_simulation()
    elif pilih == "0":
        break