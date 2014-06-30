#!/usr/bin/python2
# -*- coding: utf-8 -*-


import os
import sys
import shutil
import debian


# Dizin işlemleri komutları
def dizine_gec(dizin):
	os.chdir(dizin)
	
def dizin_yap(dizin):
	os.mkdir(dizin)

def dizin_sil(dizin):
	shutil.rmtree(dizin)

def dizin_varmi(dizin):
	return os.path.exists(dizin)

def dizin_ne():
	return os.getcwd()

def dizin_listele(dizin):
	return os.walk(dizin)

# Diğer kısayollar
def yap(komut):
	os.system(komut)
	
def cik():
	sys.exit()

def dosyami(dosya):
	return os.path.isfile(dosya)

def dosyakopyala(dosya):
	os.system("cp %s" %(dosya))

#def guncelle():
#        os.mkdir("guncelle")
#	os.chdir("guncelle")
#	os.system("wget http://paketci.googlecode.com/files/paketciprealpha3unstable.tar.gz")
#	os.system("tar -xzvf paketciprealpha1.5.tar.gz")
#	os.system("./paketci_kur")
#	os.system("cd .. && rm -rf guncelle")
#	os.system("echo -e '\E[0;32m'\"\033[1mPaketçi yükseltmesi tamamlandı.\033[0m\"")
#	sys.exit()
def indir(site):
        os.system("wget %s"%(site))
	
