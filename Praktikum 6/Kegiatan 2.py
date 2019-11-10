Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ## Program Akun
>>> ## Dibuat oleh Alif L200190203
>>> import random
>>> angka = random.randint(0,1000)
>>> 
>>> Nama = 'Alif Putra Baskara'
>>> TanggalLahir = '23 September 2000'
>>> NamaSingkat = Nama[0] + '. ' + Nama[1] + '. ' + Nama[2] + '. ' + Nama [3:18]
>>> Username = Nama[0] + TanggalLahir[0] + TanggalLahir[13:17]
>>> Password = Nama[0:4] + str(angka)
>>> print(NamaSingkat)
A. l. i. f Putra Baskara
>>> print (Username)
A22000
>>> print(Password)
Alif671
>>> print (Nama)
Alif Putra Baskara
>>> 
