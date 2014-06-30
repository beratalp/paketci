#!/usr/bin/python2
# -*- coding: utf-8 -*-

import os
import sys
import aletkutusu as alt

def start():
	paket1 = "1)PiSi"
	paket2 = "2)dpkg - apt - aptitude"
	paket3 = "3)yum"
	paket4 = "4)Pacman"
	paket5 = "5)SuSe (zypper)"
	paket6 = "6)Diğer"
	os.chdir("/usr/share/paketci")
	yap = open("yapilandir.txt", "w")
	kur = open("kur.txt", "w")
	print paket1
	print paket2
	print paket3
	print paket4
	print "Lütfen paket yöneticinizi seçiniz"
	yapsoru = raw_input("Paket yöneticinizin numarası: ")
	if yapsoru == "1":
		print "Seçtiğiniz paket yöneticisi PiSi(Pardus)"
		yap.write("pisi sr")
		kur.write("pisi it")
	elif yapsoru == "2":
		print "Seçtiğiniz paket yöneticisi dpkg"
		yap.write("aptitude search")
		kur.write("apt-get install")
	elif yapsoru == "3":
		print "Seçtiğiniz paket yöneticisi Yum"
		yap.write("yum search")
		kur.write("yum install")
	elif yapsoru == "4":
		print "Seçtiğiniz paket yöneticisi Pacman(ArchLinux)"
		yap.write("pacman -Ss")
		kur.write("pacman -S")
	elif yapsoru == "5":
                print "Seçtiğiniz paket yöneticisi Zypper(SuSe)"
                yap.write("zypper search")
                kur.write("zypper install")
	
	elif yapsoru == "6":
		print "Elle yapılandırmayı seçtiniz"
		yonetici = raw_input("Paket yöneticiniz ile arama yaptığınız komutu giriniz(Örneğin: 'pisi sr'): ")
		yap.write("%s" %(yonetici))
		kurucu = raw_input("Paket yöneticiniz ile kurulum yaptığınız komutu giriniz: ")
		kur.write("%s" %(kurucu))
	else:
		print "Yapılandırma kullanıcı tarafından iptal edildi!"
