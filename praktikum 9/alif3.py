import shelve

berkas = open("L200190203", "r")
F = shelve.open("Alif.data")
print (F["Data"][2])
print (F["Data"][0])
print (F["Data"][3])
