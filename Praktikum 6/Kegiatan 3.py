## Program Identitas Data Diri. Dibuat oleh Alif L200190203
Nama = "Alif Putra Baskara"
NIM = 0203
Tinggi = 1.72
Berat = 73
TahunLahir = 2000
Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
type(Aku)
<class 'tuple'>
# Because the "Aku" data is written in parentheses
Aku[0]
2000
# Because the first object in "Aku" data is "TahunLahir", The value of "TahunLahir" is
a = NIM % 4; Aku[a]
2000
# Because the remaining result of 1092 divided by 4 is 0, so the result of Aku[0] is 2000
type(Aku[a])
<class 'int'>
# Because the value of "TahunLahir" is 0, 0 is an integer data type
Aku[a:4}
(1999, 65, 1.72,1092)
# Because the first 4 object in the "Aku" data is "TahunLahir", "Berat", "Tinggi", and "NIM"
type(Aku[4])
<class 'str'>
# Because the fifth object in the "Aku" data is "Nama", The value of "Nama" is "Alif Putra Baskara"
Aku[0] = "ok"

