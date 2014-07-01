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
    alt.cik()