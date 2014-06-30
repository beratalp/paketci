#!/usr/bin/python2
# -*- coding: utf-8 -*-
import os
import sys
import aletkutusu as alt


def kaldir():
	print "RPM paketleri için kaldırma henüz desteklenmemektedir"
	print "Ancak yüklediğiniz paketleri görebilirsiniz."
	print "Listeleniyor..."
	liste = open("/usr/share/paketci/rpm/kayit/liste.txt","r")
	for satir in liste:
		print satir
	sorsoru = raw_input("Yeni sürümde bu özellik gelmiş olabilir. Yeni sürüme geçilsin mi: ")
	if sorsoru == "evet":
		print "Paketçi yeni sürüme güncelleniyor"
		alt.yap("paketci guncelle")
	alt.cik()