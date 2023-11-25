
def luas_segitiga_siku():
	bidang_datar = 'segitiga'
	alas =int(input('masukan alas: '))
	tinggi =int(input('masukan tinggi:' ))
	luas = 0,5* alas* tinggi

	return bidang_datar, luas 

def luas_persegi():
	bidang_datar = 'persegi'
	sisi =int(input('masukan sisi: '))
	luas = sisi * sisi
	
	return bidang_datar, luas
	
def luas_lingkaran():
	bidang_datar ='lingkaran'
	r =int(input('masukan jari2:' ))
	luas =3,14 * (r * r)
	
	return bidang_datar, luas
	
if __name__ == "__main__":
	print("1. luas segitiga siku")
	print("2. luas persegi")
	print("3. luas lingkaran")
	
	pilih_menu = int(input("pilih menu:" ))
	if pilih_menu == 1:
		luas_persegi ()
	elif pilih_menu == 2:
		luas_persegi ()
	elif pilih_menu == 3:
		luas_persegi ()
	elif pilih_menu == 4:
		luas_persegi ()
		
	print("luas {} adalah: {}" .format(hasil[1], hasil[4] ))
