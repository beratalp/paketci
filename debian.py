#!/usr/bin/python2
# -*- coding: utf-8 -*-

import os
import aletkutusu as alt
import sys


	
def ac(paket_adi,komut_dizini):
	alt.yap("echo -e '\E[0;32m'\"\033[1mPaket açılıyor...\033[0m\"")
	if alt.dizin_varmi("/usr/share/paketci/gecici"):
		pass
	else:
		alt.dizin_yap("/usr/share/paketci/gecici")
	
	# Gerekli geçici dizinleri oluşturuyoruz.
	alt.dizine_gec("/usr/share/paketci/gecici")
	alt.yap("mkdir "+paket_adi)
	alt.dizine_gec("/usr/share/paketci/gecici/"+paket_adi)
	print "Paket için geçici dizin oluşturuluyor: ", alt.dizin_ne()
	print "---------------------------"
	print "Geçici dizinler oluşturuldu"
	print "---------------------------"
	# Komutun verildiği dizinde bulunan kaynak paketi geçici dizine kopyalıyoruz.
	print "Paket geçici dizine kopyalanıyor..."
	alt.dizine_gec(komut_dizini)
	alt.yap("cp " + paket_adi + ".deb " + "/usr/share/paketci/gecici/" + paket_adi)
	alt.dizine_gec("/usr/share/paketci/gecici/"+paket_adi)
	
	#Paketi açıyoruz.
	print "\"" + paket_adi + "\" paketi açılıyor..."
	alt.yap("ar xv " + paket_adi + ".deb")
	
	alt.dizin_yap("/usr/share/paketci/gecici/"+paket_adi+"/control")
	alt.dizin_yap("/usr/share/paketci/gecici/"+paket_adi+"/data")
	
	# "control.tar.gz" ve "data.tar.gz" dosyalarını açıyoruz.
	print "\n\"control.tar.gz\" açılıyor...\n"
	alt.yap("tar xzvf control.tar.gz --directory=control")
	print "\n\"data.tar.gz\" açılıyor...\n"
	alt.yap("tar xzvf data.tar.gz --directory=data")
	print "Paket açıldı"

def bag_test(paket_adi):
	
	alt.yap("echo -e '\E[0;32m'\"\033[1mBağımlılıklar ayrıştırılıyor...\033[0m\"")
	
	# Bağımlılıkların listesini "control" dosyasından alıyoruz.
	alt.dizine_gec("/usr/share/paketci/gecici/"+paket_adi+"/control")
	bgm = open("control","r").readlines()
	
	# "gecici" dizini içine bağımlılık listesini koyuyoruz
	bgm_liste = open("../../bagimliliklar","w")
	
	for satir in bgm:
		# "Depends" ve varsa "Pre-Depends" etiketlerine bakıyoruz.
		ifade = satir.split(': ')
		
		if ifade[0] == "Depends" or ifade[0] == "Pre-Depends":
	
			liste = ifade[1].split(', ')
			# Artırma değeri belirliyoruz ve bağımlılıklar listesini buna göre bir dosyaya yazdırıyoruz.
			art = 0
			while art < len(liste)-1:
					bgm_liste.write("Ad: " + liste[art] + "\n")
					art = art + 1
			
			# Listenin son elemanı döngünün dışında kalıyor, ekliyoruz
			bgm_liste.write("Ad: " + liste[-1])
			
			# Yazma tamamlandı, kapatıyoruz
	bgm_liste.close()

	print "\nBağımlılıkların belirlenmesi tamamlandı!"
	# Bağımlılıkların listesini kullanıcıya sunuyor, ve kurup kurmadığını soruyoruz.
	alt.yap("echo -e '\E[0;31m'\"\033[1m------------------------\033[0m\"")
	alt.yap("echo -e '\E[0;32m'\"\033[1mBAĞIMLILIK LİSTESİ\033[0m\"")
	
	#Bağımlılık kaydını açıyor ve ekrana yazdırıyoruz
	alt.dizine_gec("/usr/share/paketci/gecici/")
	bgm_liste = open("bagimliliklar","r")
	while 1:
		satir = bgm_liste.readline()
		if not satir:
			break
		else:
			print satir
	
	alt.yap("echo -e '\E[0;31m'\"\033[1m------------------------\033[0m\"")
	print "Bağımlılıkları http:\\packages.debian.org adresinden indirebilirsiniz"
	bgm_testi = raw_input("Yukarıda listelenen bağımlılıkları kurdunuz mu? (e/h): ")
	if bgm_testi == "e":
		pass
	elif bgm_testi == "h":
		print "Lütfen yukarıda listelenen bağımlılıkları kurduktan sonra tekrar deneyiniz."
		alt.dizin_sil("/usr/share/paketci/gecici/"+paket_adi)
		
		alt.cik()
	else:
		print "Hata: Geçersiz seçenek girdiniz.\n"
		alt.dizin_sil("/usr/share/paketci/gecici/"+paket_adi)
		alt.cik()


def kur(paket_adi):
	
	alt.dizine_gec("/usr/share/paketci/kayit/debian")
	if alt.dizin_varmi(paket_adi):
		alt.yap("rm -rf "+paket_adi)
		
	# Paketin adıyla bir dizin oluşturuyoruz, buraya silme kaydı gelecek.	
	alt.dizine_gec("/usr/share/paketci/kayit/debian")
	alt.yap("mkdir "+paket_adi)
	print "---------------------------------"
	print "Silme kaydı başarıyla oluşturuldu"
	print "---------------------------------"
	
	# Varsa preinst script'ini çalıştırıyoruz.
	alt.dizine_gec("/usr/share/paketci/gecici/"+paket_adi+"/control")
	if alt.dosyami("preinst"):
		alt.yap("echo -e '\E[0;32m'\"\033[1mKurulum öncesi işlemler yapılıyor...\033[0m\"")
		alt.yap("./preinst install")
		alt.yap("echo -e '\E[0;32m'\"\033[1mKurulum öncesi işlemler tamamlandı.\033[0m\"")
	
	# Dosyaları kopyalıyoruz.
	print "Kurulum başlıyor..."
	alt.dizine_gec("/usr/share/paketci/gecici/"+paket_adi+"/data")
	alt.yap("cp * / -r")
	
	
	# Varsa postinst script'ini çalıştırıyoruz
	alt.dizine_gec("/usr/share/paketci/gecici/"+paket_adi+"/control")
	if alt.dosyami("postinst"):
		alt.yap("echo -e '\E[0;32m'\"\033[1mKurulum sonrası işlemler yapılıyor...\033[0m\"")
		alt.yap("./postinst configure")	
		alt.yap("echo -e '\E[0;32m'\"\033[1mKurulum sonrası işlemler tamamlandı.\033[0m\"")
	
	print "Kaldırma kayıtları oluşturuluyor"
	# Eğer varlarsa prerm ve postrm scriptlerini kaydediyoruz.
	alt.dizine_gec("/usr/share/paketci/gecici/"+paket_adi+"/control")
	if alt.dosyami("prerm"):
		alt.yap("echo -e '\E[0;32m'\"\033[1mKaldırma öncesi işlemleri kaydediliyor...\033[0m\"")
		alt.yap("cp prerm "+"/usr/share/paketci/kayit/debian/"+paket_adi)
	
	if alt.dosyami("postrm"):
		alt.yap("echo -e '\E[0;32m'\"\033[1mKaldırma sonrası işlemleri kaydediliyor...\033[0m\"")
		alt.yap("cp postrm "+"/usr/share/paketci/kayit/debian/"+paket_adi)
	
		
	# Kopyalamadan sonra ileride paketin kaldırılabilmesi için "kayit" dizini altına yukarıdaki komut ile kopyalanmış
	# dosyaların listesini kaydediyoruz.
	alt.dizine_gec("/usr/share/paketci/kayit/debian/"+paket_adi)
	kayit = open("silme_kaydi","w")
	
	# İleride dosyaların sağlamlığının kontrol edilebilmesi için tüm dosyaların md5sum değerlerini topluyoruz.
	kontrol = open("kontroller","w")
	
	
	# "silme_kaydi" dosyasındaki tüm satırlar, paket kaldırılmak istenirse "rm -rf [satir]" komutundan geçirilecek
	for kok, dizinler, dosyalar in alt.dizin_listele("/usr/share/paketci/gecici/"+paket_adi+"/data"):
    		for isim in dosyalar:
			# HemenKur'a ait dizin parçalarını kayda geçirmiyoruz.
			uzunluk = len("/usr/share/paketci/gecici/"+paket_adi+"/data")
			
        		kayit.write(os.path.join(kok, isim)[uzunluk:])
			kayit.write("\n")
			
			# Burada kurulum sırasında sisteme yerleştirilen her dosyanın md5sum değerini kaydediyoruz.
			# İleride dosyaların bozuk olup olmadığı bu sayede kontrol edilebilecek.
			if os.path.isfile(os.path.join(kok, isim)):
				temp = 0
				metin = ""
				while temp  != len(os.path.join(kok, isim)):
					if os.path.join(kok, isim)[temp] == " ":
						metin = metin + "\\" + os.path.join(kok, isim)[temp]
					else:
						metin = metin +os.path.join(kok, isim)[temp]
					temp = temp + 1	
				
				md5_degeri = os.popen("md5sum "+metin).readline()
				
				# Dosyaların yolundan paketci/gecici kısımlarını çıkarıyoruz.
				md5_yaz = md5_degeri.split(" ")[0]
				dosya_yolu = md5_degeri.split(" ")[2][uzunluk:]
				kontrol.write(md5_yaz + " " + dosya_yolu)
				
				metin = ""
	
	
	
	# "silme_kaydi"nı ve kontrol'ü kapatıyoruz
	kayit.close()
	kontrol.close()
	
	# "gecici" dizinindeki paketimizi kaldırıyoruz.
	alt.dizine_gec("/usr/share/paketci/gecici")
	alt.yap("rm -rf "+paket_adi)
		
	print "\nİleride paketin kaldırılabilmesi için kayıt oluşturuldu."
	print "Bağımlılık listesi yeniden oluşturuluyor"
	
	# Belki kullanıcıya lazım olur diye bağmlılıkları tekrar listeliyoruz.
	print "Gerekirse diye bağımlılık listesi bir kez daha belirtiliyor"
	alt.yap("echo -e '\E[0;31m'\"\033[1m------------------------\033[0m\"")
	alt.yap("echo -e '\E[0;32m'\"\033[1mBAĞIMLILIK LİSTESİ\033[0m\"")
	
	#Bağımlılık kaydını açıyor ve ekrana yazdırıyoruz
	alt.dizine_gec("/usr/share/paketci/gecici/")
	bgm_liste = open("bagimliliklar","r")
	while 1:
		satir = bgm_liste.readline()
		if not satir:
			break
		else:
			print satir
	
	alt.yap("echo -e '\E[0;31m'\"\033[1m------------------------\033[0m\"")
        
	
	# İşimiz bittiğine göre "gecici" dizinindeki herşeyi kaldırıyoruz.
	alt.dizine_gec("/usr/share/paketci/gecici")
	alt.yap("rm -rf *")


def kaldir():
	
	paket_listesi={}
	art = 1
	alt.dizine_gec("/usr/share/paketci/kayit/debian")
	for kok, dizinler, dosyalar in alt.dizin_listele("/usr/share/paketci/kayit/debian"):
		if dizinler != []:
			for k in dizinler:
				paket_listesi[art]=k
				art = art + 1
		else:
			pass
		
	# Kaldırılabilecek paket yoksa hata veriyoruz.
	if paket_listesi == {}:
		print "Paket kurmadınız."
		alt.cik()
	
	alt.yap("echo -e '\E[0;32m'\"\033[1mKaldırılabilir paketlerinin listesi:\033[0m\"")
	print "\n".join("%s) %s" % (k,v) for k,v in paket_listesi.items())
	
	paket_adi = ""
	paket_no = input("Lütfen kaldırmak istediğiniz paketin numarasını girin: ")
	try:
		paket_adi = paket_listesi[paket_no]
	except:
		print "Geçersiz bir numara girdiniz."
		alt.cik()
	
	# Eğer varsa prerm script'i çalıştırılacak.
	alt.dizine_gec("/usr/share/paketci/kayit/debian/"+paket_adi)
	if alt.dosyami("prerm"):
		alt.yap("echo -e '\E[0;32m'\"\033[1mKaldırma öncesi işlemler yapılıyor...\033[0m\"")
		alt.yap("./prerm remove")
		alt.yap("echo -e '\E[0;32m'\"\033[1mKaldırma öncesi işlemler tamamlandı.\033[0m\"")
	
	
	# "kur" ile oluşturduğumuz "silme_kaydi" dosyasındaki tüm dosyalara "rm -rf" uygulayacağız.
	if not alt.dizin_varmi("/usr/share/paketci/kayit/debian/"+paket_adi):
		print "Böyle bir paket yok!"
		alt.cik()
	alt.dizine_gec("/usr/share/paketci/kayit/debian/"+paket_adi)
	silme = open("silme_kaydi","r")
	while 1:
    		satir = silme.readline()
    		if not satir: # Başka satır kalmadıysa çık.
        		break
    		alt.yap("rm -rf "+satir)
	silme.close()
	
	# Eğer varsa postrm script'i çalıştırılacak.
	alt.dizine_gec("/usr/share/paketci/kayit/debian/"+paket_adi)
	if alt.dosyami("postrm"):
		alt.yap("echo -e '\E[0;32m'\"\033[1mKaldırma sonrası işlemler yapılıyor...\033[0m\"")
		alt.yap("./postrm remove")
		alt.yap("echo -e '\E[0;32m'\"\033[1mKaldırma sonrası işlemler tamamlandı.\033[0m\"")
	
	# Kaldırma tamamlandı Kullanıcıyı bilgilendiriyoruz.
	alt.yap("echo -e '\E[0;31m'\"\033[1m------------------------\033[0m\"")
	alt.yap("echo -e '\E[0;32m'\"\033[1mPaket başarıyla kaldırıldı!\033[0m\"")
	alt.yap("echo -e '\E[0;31m'\"\033[1m------------------------\033[0m\"")
	#Son olarak "kayit/debian" altındaki paketimize ait klasörü siliyoruz.
	alt.dizine_gec("/usr/share/paketci/kayit/debian/")
	alt.dizin_sil(paket_adi)
	print "Paket kayıtlardan temizlendi"
	print "Paketin ana dosyaları silindi"
	print "Lütfen bağımlılıkları da kaldırınız"
	
	
def kontrol(paket_adi):
	
	
	alt.dizine_gec("/usr/share/paketci/kayit/debian/"+paket_adi)
	
	# Geçici değişkenleri oluşturuyoruz
	deger = ""
	md5 = ""
	dosya = ""
	
	# md5sum kayıtlarını açıyor ve tek tek kontrol ediyoruz.
	kontroller = open ("kontroller","r")
	while 1:
    		satir = kontroller.readline()
    		if not satir: # Başka satır kalmadıysa çık.
        		break
    		
		# O anki satırın değerini md5sum ve dosya olarak ikiye bölüyor ve kontrolü yapıyoruz.
		deger = satir.split(" ")
		md5 = deger[0]
		dosya = deger[1][:-1]

		
		if alt.dosyami(dosya):

			if os.popen("md5sum "+dosya).readline()[0:32] == md5:
				print dosya + "   ... " + "\033[01;32mTAMAM\033[0m"
			else:
				print dosya +    "... " + "\033[01;31mHATALI\033[0m"
		else:
			print dosya + "   ... " + "\033[01;31mSİLİNMİŞ\033[0m"
	
	# İşimiz bitti, kontroller dosyasını kapatıyoruz.
	kontroller.close()
	
	# Son olarak kullanıcıyı bilgilendiriyoruz.
	alt.yap("echo -e '\E[0;32m'\"\033[1mKurulum kontrolü tamamlandı.\033[0m\"")
	print "Lütfen yukarıdaki listede \"HATALI\" veya \"SİLİNMİŞ\" olarak gözüken dosyalarınızı (eğer varsa) kontrol edin."
	alt.yap("echo -e '\E[0;32m'\"\033[1mKurulum tamamlandı!.\033[0m\"")


	
