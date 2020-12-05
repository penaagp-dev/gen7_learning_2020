print (" *****Pemesanan Baju Online***** ")

a= raw_input(" Nama Pembeli = ")
b= raw_input(" Warna Baju = ")
c= input(" Lingkar Dada (CM) = ")	

if c<90:
	print("Ukuran Baju  S")
elif c<96:
	print("Ukuran Baju M")
elif c<104:
	print("Ukuran Baju L")
elif c<106:
	print("Ukuran Baju XL")
elif c<114:
	print("Ukuran Baju XXL")
elif c<120:
	print("Ukuran Baju 4L")
elif c<124:
	print("Ukuran Baju 5L")
elif c>124:
	print("Ukuran Baju Oversize")
	
	
print ("Terimakasih")
