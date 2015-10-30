#!/usr/bin/python2
# -*- coding: utf-8 -*-
import os
import sys

def start():
	print "Removing paketci..."
	os.system("rm -rf /usr/share/paketci")
	os.system("rm -rf /usr/bin/paketci")
	print "Paketci has removed from your system."
