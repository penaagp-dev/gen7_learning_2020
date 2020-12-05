print ("nama cat warna")
print ("6 cat merah harga percat : 10000")
print ("4 cat putih harga percat : 15000")
print ("3 cat hijau harga percat : 20000")
print ("9 cat biru harga percat : 25000")
print ("5 cat kuning harga percat : 30000")
while True :
		a = int(input("masukkan jumlah cat warna yang ingin dibeli = "))
		b = int(input("masukkan harga cat warna  = "))
		c = a * b
		print(" = total harga",c)
		d = input("apakah anda ingin membayarnya? (ya/tidak)= ")
		if(d == "ya") :
			True
		else :
			print("terimah kasih")
			break
