nb=raw_input("Nama barang=")
bb=input("Banyak barang=")
hb=input("Harga barang=")

byr=bb*hb
if byr<100000:
	tby=byr
	print"Total bayar=",byr

if byr>100000 and byr<=300000:
	tby=byr-(byr*0.05)
	print"Total bayar=",byr
	
if byr>300000:
	tby=byr-(byr*0.01)
	print"Total bayar=",byr
	
	
