# Array digunakan untuk menyimpan list barang-barang di toko
items = ["beras", "gula", "minyak", "tepung", "telur"]

# Menampilkan semua barang yang tersedia di toko
print("Barang yang tersedia di toko: ")
for item in items:
    print("-", item)

# Menambahkan barang baru ke dalam toko
items.append("kecap")

# Menghapus barang dari toko
items.remove("telur")
# Menampilkan barang yang tersedia di toko setelah perubahan
print("\nBarang yang tersedia di toko setelah perubahan: ")
for item in items:
    print("-", item)

# Menghitung jumlah barang yang tersedia di toko
num_items = len(items)
print("\nJumlah barang yang tersedia di toko: ", num_items)

# Mencari indeks dari sebuah barang di toko
index = items.index("minyak")
print("\nIndeks barang 'minyak' di toko: ", index)

# Menampilkan barang di indeks tertentu di toko
print("\nBarang di indeks ke-2: ", items[2])

# Mengubah harga barang di toko menggunakan array dua dimensi
# Array kedua digunakan untuk menyimpan harga setiap barang
prices = [["beras", 10000], ["gula", 12000], ["minyak", 15000], ["tepung", 5000], ["kecap", 3000]]

# Menampilkan harga barang di toko
print("\nHarga barang di toko: ")
for item, price in prices:
    print("-", item, ": Rp", price)

# Mengubah harga barang
prices[0][1] = 12000
prices[1][1] = 14000
prices[2][1] = 17000
prices[3][1] = 6000
prices[4][1] = 3500

# Menampilkan harga barang setelah diubah
print("\nHarga barang setelah diubah: ")
for item, price in prices:
    print("-", item, ": Rp", price)