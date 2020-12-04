print('daftar harga handpone')
print('xiaomi redmi 9A=1.350.000')
print('vivo Y51 8/128 =3.599.000')
print('samsung A21s =2.499.000')
print('oppo reno 4pro =6.720.000')
while True :
	a = int(input('masukan jumlah handpone yang mau di pesan = '))
	b = int(input('masukan jumlah harga handpone = '))
	c = a * b
	print('total = ',c)
	d = input("apakah anda masih ingin memesan handpone? (ya/tidak)")
	if(d == "ya") :
		True
	else :
		print("thank you :)")
		break
