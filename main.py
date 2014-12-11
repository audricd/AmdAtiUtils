__author__ = 'audricd'
"""amdatiutils
ver 0.0.1
"""
import os
f = os.popen('aticonfig --odgt --adapter=0')
odgta0 = f.readlines()
linea0 = os.popen('aticonfig --odgt --adapter=0').read().replace('\n', '')


partes = linea0.split()

parte1 = linea0.partition(" ")

if "ATI" in linea0:
   print "Your " + partes[3] + " " + partes[4] + " " +partes[5] + " " + partes[6] + " " + partes[7] + " is at " + partes[12] + " " + u'\u2103'
else:
   print "You do not have FGLRX installed"

