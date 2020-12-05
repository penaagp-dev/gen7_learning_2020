print('daftar menu makanan dan minuman')
print('harga bakso : 15.000')
print('harga jus jeruk : 5.000')
print('harga sate : 10.000')
print('harga ayam goreng : 12.000')
print('harga tempe goreng: 8.000')
while True :
	a = int(input('masukan jumlah menu yang akan di pesan = '))
	b = int(input('masukan jumlah harga menu = '))
	c = a * b
	print("total = ",c)
	d = input("apakah anda ingin memesan ulang? (ya/tidak)")
	if(d == "ya") :
		True
	else :
		print("Thank You :)")
		break
