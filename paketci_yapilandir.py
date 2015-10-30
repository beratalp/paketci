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
	paket6 = "6)Other"
	os.chdir("/usr/share/paketci")
	yap = open("yapilandir.txt", "w")
	kur = open("kur.txt", "w")
	print paket1
	print paket2
	print paket3
	print paket4
	yapsoru = raw_input("Enter the number for your package managar: ")
	if yapsoru == "1":
		print "The chosen package manager is PiSi (Pardus)"
		yap.write("pisi sr")
		kur.write("pisi it")
	elif yapsoru == "2":
		print "You've chosen dpkg (Ubuntu - Debian)"
		yap.write("aptitude search")
		kur.write("apt-get install")
	elif yapsoru == "3":
		print "You've choesen Yum"
		yap.write("yum search")
		kur.write("yum install")
	elif yapsoru == "4":
		print "You've chosen Pacman (ArchLinux)"
		yap.write("pacman -Ss")
		kur.write("pacman -S")
	elif yapsoru == "5":
                print "You've chosen zypper (SuSe)"
                yap.write("zypper search")
                kur.write("zypper install")
	
	elif yapsoru == "6":
		print "Manual configuration is starting..."
		yonetici = raw_input("What is the search command of your package manager: ")
		yap.write("%s" %(yonetici))
		kurucu = raw_input("What is the installation command of your package manager: ")
		kur.write("%s" %(kurucu))
	else:
		print "Error. Configuration aborted."
