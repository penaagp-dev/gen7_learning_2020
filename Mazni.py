print('harga sepatu terbaru 2020')
print('New Joemen J 67s : 238.900')
print('Paulmax 8112 Navy : 450.000')
print('Crocodile Boots : 245.000')
print('Karrimori ax2 : 850.000')
print('Kodachi Medona : 600.000')
while True :
	a = int(input('masukan jumlah barang yang di pesan = '))
	b = int(input('masukan jumlah harga sepatu = '))
	c = a * b
	print("total = ",c)
	d = input("apakah anda ingin memesan ulang? (ya/tidak)")
	if(d == "ya") :
		True
	else :
		print("Terima kasih sudah belanja di toko kami:)")
		break
		
