#!/usr/bin/python2
# -*- coding: utf-8 -*-
import os
import sys

def start():
	print "Paketçi kaldırması başlatılıyor"
	#kaldir = open("~/.paketci.txt","w")
	print "Lütfen kaldıracağınız paketleri tek tek kaldırınız."
	os.system("paketci debian kaldir")
	print  "Kaldırma bitti."
	os.system("rm -rf /usr/share/paketci")
	os.system("rm -rf /usr/bin/paketci")
	print "Paketçi başarıyla kaldırıldı."
