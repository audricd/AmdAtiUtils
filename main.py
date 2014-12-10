__author__ = 'audricd'
"""amdatiutils
ver 0.0.1
"""
import os
f = os.popen('aticonfig --odgt --adapter=0')
odgta0 = f.readlines()
linea0 = os.popen('aticonfig --odgt --adapter=0').read().replace('\n', '')
#print linea0



temp10000 = linea0[73]
temp01000 = linea0[74]
temp00100 = linea0[75]
temp00010 = linea0[76]
temp00001 = linea0[77]
#print temp10000 + temp01000 + temp00100 + temp00010 + temp00001
print "Your GPU#0 is at ", temp10000 + temp01000 + temp00100 + temp00010 + temp00001 + " " + u'\u2103'