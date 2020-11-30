#untuk aplikasi zodiaknya maaf tidak sy kerja sampai selesai
#zodiak yang bisa tampil hanya (aquarius,cancer,pisces,aries ya :) )
#ini hanya sebagai referensi buat kalian
#sy yakin kalian bisa berkreasi lebih dari ini
#ini fungsi yang pertama yang menampilkan >>>>>
def garis():
	print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

#ini fungsi yang menampilkan --------	
def garis1():
	print ("------------------------------------------")
	
#ini perulangan while yang selalu mengulang jika hasilnya masih tetap benar
while True :
	#pemanggilan fungsi
	garis()
	
	#output string
	print ("\t Aplikasi Zodiak")
	garis()
	
	#input pada python
	a= int(input("masukan tanggal lahir  = "))
	b= input("masukan bulan lahir = ")
	
	#kondisi pada python yang memuat beberapa operator seperti operator logical (or dan and), perbandingan (== dan <=)
	#kondisi di sini untuk menentukan zodiak seseorang
	if (a <= 18 and a >= 1 and b == "februari" or a <= 31 and a >= 20 and b == "januari" ):
		garis1()
		print ("zodiak anda adalah =aquarius")
	#kondisi kedua yang menggunakan elif, tidak jauh berbeda dengan kondisi yang pertama
	elif (a <= 30 and a >= 21 and b == "juni" or a <= 31 and a >= 22 and b == "juli" ):
		garis1()
		print ("zodiak anda adalah =cancer")
	elif (a <= 29 and a >= 19 and b == "februari" or a <= 20 and a >= 1 and b == "maret" ):
		garis1()
		print ("zodiak anda adalah = pisces")
	elif (a <= 31 and a >= 21 and b == "maret" or a <= 19 and a >= 1 and b == "april" ):
		garis1()
		print ("zodiak anda adalah = aries")
	else :
		garis1()
		print ("input salah")
	garis()	
	
	#input untuk jika anda ingin mengulanginya lagi
	c = input("apakah anda ingin mengulanginya lagi? (y/t)")
	
	#kondisi yang memilah antara mengulang lagi atau tidak
	#kondisi di sini yang menentukan apakah perulangan bernilai True atau Perulangan berhenti
	if (c == "y"):
		True
	else:
		garis1()
		print( "Semongko Guys :) " )
		break
