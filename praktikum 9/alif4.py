import shelve

berkas = open("L200190203", "r")
NIM = berkas.readline()
TTL = berkas.readline()
Nama = berkas.readline()
Kota = berkas.readline()
TTL = Kota + TTL

F = shelve.open("Alif.data")
F["Data"] = [NIM, TTL, Nama, Kota]
F.close()
