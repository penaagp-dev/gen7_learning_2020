print('daftar harga barang elektronik')
print('1,kipas angin : 250000')
print('2,setrika : 150000')
print('3,rice cooker : 300000')
print('4,kulkas : 2000000')
print('5,mesin cuci : 3000000')
while True :
	a = int(input('masukan jumlah barang yang ingin di beli ='))
	b = int(input('masukan harga barang yang di beli ='))
	c = a * b
	print ("total =",c)
	d = input ("apakah anda ingin membeli barang yang lain? (yes/no)")
	if (d == "ya") :
		True
	else :
		print ("thank you")
		break
