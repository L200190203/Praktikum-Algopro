berkas = open("L200190203", "w")
berkas.write("L200190203\n")
berkas.write("23-09-2000\n")
berkas.write("Alif Putra Baskara\n")
berkas.write("Madiun")
berkas.close()

berkas = open ("L200190203", "r")
NIM = berkas.readline()
TTL = berkas.readline()
Nama = berkas.readline()
Kota = berkas.readline()

print (Nama)
print (Kota,TTL)
print (NIM)
