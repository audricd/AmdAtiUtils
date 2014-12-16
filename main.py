__author__ = 'audricd'
"""amdatiutils
ver 0.0.4
"""
import os
import sys


temp0 = os.popen('aticonfig --odgt --adapter=0')
odgta0 = temp0.readlines()
linea0 = os.popen('aticonfig --odgt --adapter=0').read().replace('\n', ' ')

checkfglrx = os.popen('dmesg | grep fglrx | grep module | grep loaded').read().split()


partesid0temp0 = linea0.split()

parteid0temp0_1 = linea0.partition(" ")

fglrxver = checkfglrx[7] + " " + checkfglrx[8] + " " + checkfglrx[9] + " " + checkfglrx[10]+ " "

if not "ATI" in linea0:
   print "You do not have FGLRX installed"
   sys.exit()


print 'Welcome to AmdAtiUtils v0.0.4'

ans=True
while ans:
 print ("""
 1.Check your FGLRX driver version
 2.Show name and temperature for primary GPU
 3.Manually set fan speed for primary GPU
 0.Exit/Quit
 """)
 ans=raw_input("What would you like to do? ")
 if ans=="1":
  print "You have FGLRX "+ fglrxver +"installed."
 elif ans=="2":
  print "\n Your " + partesid0temp0[3] + " " + partesid0temp0[4] + " " + partesid0temp0[5] + " " + partesid0temp0[6] + " " + partesid0temp0[7] + " is at " + partesid0temp0[12] + " " + u'\u2103'
 elif ans=="3":
  fanspeed0100 = raw_input('Insert value from 0 to 100. 80 is recommended.' +"\n")
  fanspeedset = os.popen('aticonfig --pplib-cmd "set fanspeed 0  '+ fanspeed0100 + '"')
  print 'Your fan speed has been set to ' + fanspeed0100 + '%.'
 elif ans=="0":
  sys.exit()
 else:
  print("\n Not Valid Choice. Try again")