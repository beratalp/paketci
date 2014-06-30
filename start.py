#!/usr/bin/env python2
# -*- coding:utf-8 -*-

import os
from Tkinter import *
from tkMessageBox import *
import sys

try:
    import ImageTK
except ImportError:
    showerror("Hata","Lütfen ImageTK modülünü yükleyin.Yüklemek için imagetkkur.py' yi root olarak çalıştırın")
    sys.exit()

os.system("tar -xzvf kur.tar.gz")
os.chdir("kur")
os.system("python kur.py")
