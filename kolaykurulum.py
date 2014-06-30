#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys
import os
import aletkutusu as alt
import paketci_yapilandir as pakyap

def start():
	menu1 = "1)RPM işlemleri"
	menu2 = "2)Deb işlemleri"
	menu3 = "3)Ayarlar"
	menu4 = "4)Yardım"
	menu5 = "5)Programdan Çıkış"
	print menu1
	print menu2
	print menu3
	print menu4
	soru1 = raw_input("Lütfen yapmak istediğiniz işlemi seçiniz: ")
	if soru1 == "1":
		print "RPM işlemleri"
		secenek1 = "1)Kur"
		secenek2 = "2)Kaldır"
		print secenek1
		print secenek2
		soru2 = raw_input("Lütfen yapmak istediğiniz işlemi seçiniz: ")
		if soru2 == "1":
			print "RPM kurma menüsü"
			soru3 = raw_input("Lütfen paketin tam adresini yazınız: ")
			print "Kurulum başlıyor"
			os.system("paketci redhat %s" %(soru3))
			print "RPM kurulumu tamamlandı!"
			alt.cik()
		if soru2 == "2":
			print "RPM kaldırma başlatılıyor..."
			os.system("paketci rpmkaldir")
			alt.cik()
			
	if soru1 == "2":
		print "Deb işlemleri"
		secenek3 = "1)Kur"
		secenek4 = "2)Kaldır"
		print secenek3
		print secenek4
		soru4 = raw_input("Lütfen yapmak istediğiniz işlemi seçiniz: ")
		if soru4 == "1":
			print "Deb kurma menüsü"
			soru5 = raw_input("Paketin tam adını yazınız: ")
			print "Kurulum başlıyor..."
			os.system("paketci debian %s" %(soru5))
			print "Deb kurulumu tamamlandı"
			alt.cik()
		if soru4 == "2":
			print "Deb kaldırma menüsü"
			os.system("paketci debian kaldir")
			alt.cik()
			
	if soru1 == "3":
		print "Ayarlar menüsü"
		secenek5 = "1)Yapılandır"
		secenek6 = "2)Güncelle"
		secenek7 = "3)Paketçi' yi sistemden kaldır"
		secenek8 = "4)Programdan çık"
		print secenek5
		print secenek6
		print secenek7
		print secenek8
		soru6 = raw_input("Lütfen yapmak istediğiniz işlemi seçiniz: ")
		if soru6 == "1":
			print "Yapılandırma başlatılıyor..."
			pakyap.start()
			alt.cik()
		if soru6 == "2":
			alt.yap("paketci guncelle")
			alt.cik()
		if soru6 == "3":
			os.system("paketci kaldir")
			alt.cik()
		if soru6 == "4":
			alt.cik()
			
	if soru1 == "4":
		print "Yardım menüsü"
		secenek9 = "1)Desteklenen dağıtımlar ve paketlerin listesi"
		secenek10 = "2)Hakkında"
		secenek11 = "3)Yardım alt menüsü"
		print secenek9
		print secenek10
		print secenek11
		soru7 = raw_input("Lütfen yapmak istediğiniz işlemi seçiniz: ")
		if soru7 == "1":
			os.system("paketci destek")
			alt.cik()
		if soru7 == "2":
			os.system("paketci hakkinda")
			alt.cik()
		if soru7 == "3":
			secenek12 = "1) Web sitesi"
			secenek13 = "2) Yardım"
			print secenek12
			print secenek13
			soru8 = raw_input("Lütfen yapmak istediğiniz işlemi seçiniz: ")
			if soru8 == "1":
				print "http://code.google.com/p/paketci"
				alt.cik()
			if soru8 == "2":
				os.system("paketci yardim")
				alt.cik()
			
		





































