#Perubahan 1
print ("\t aplikasi kalkulator sederhana")

def penjumlahan(a,b):
	c = a + b
	return c
	
def pengurangan(a,b):
	c = a - b 
	return c

while True :
	print ("Pilih operator = ")
	print ("1. Penjumlahan")
	print ("2. pengurangan")
	p = input("Pilih operator penjumlahan : ")
	a = int(input("masukan nilai 1 = "))
	b = int(input("masukan nilai 2 = "))
	
	if (p == "1"):
		
		print ("hasil penjumlahan = ", penjumlahan(a,b))
	elif (p == "2"):
		
		print ("hasil pengurangan = ", pengurangan(a,b))
	else :
		("input salah")
	print ("apakah anda ingin mengulanginya lagi? (y/t)")
	d = input("Masukan pilihan = ")
	
	if (d == "y"):
		True
	elif (d == "t"):
		print ("terima kasih :) ")
		break

