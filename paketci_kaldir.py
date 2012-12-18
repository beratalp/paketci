#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

def start():
	print "Paketçi kaldırması başlatılıyor"
	kaldir = open("~/.paketci.txt","w")
	print "Lütfen kaldıracağınız paketleri tek tek kaldırınız."
	os.system("paketci debian kaldir")
	print  "Kaldırma bitti."
	os.system("rm -rf /usr/share/paketci")
	os.system("rm -rf /usr/bin/paketci")
	print "Paketçi başarıyla kaldırıldı."
	soru = raw_input("Paketçi ile beraber kurulan bağımlılıklar silinsin mi: ")
	if soru == evet:
		print "RPM2cpio kaldırılıyor..."
		os.system("rm -rf /usr/bin/rpm2cpio")
		print "RPMextract kaldırılıyor..."
		os.system("rm -rf /usr/bin/rpmextract")
		print "Paketçi ve bağımlılıkları başarıyla kaldırıldı"
	else:
		print "Bağımlılıklar kaldırılmıyor"
	sys.exit()

