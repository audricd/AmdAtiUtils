__author__ = 'audricd'
"""amdatiutils
ver 0.0.3
"""
import os
temp0 = os.popen('aticonfig --odgt --adapter=0')
odgta0 = temp0.readlines()
linea0 = os.popen('aticonfig --odgt --adapter=0').read().replace('\n', '')


partes = linea0.split()

parte1 = linea0.partition(" ")

if not "ATI" in linea0:
   print "You do not have FGLRX installed"
   import sys
   sys.exit()


print 'Welcome to AmdAtiUtils v0.0.3'

ans=True
while ans:
    print ("""
    1.Show name and temperature for primary GPU
    2.Manually set fan speed for primary GPU
    0.Exit/Quit
    """)
    ans=raw_input("What would you like to do? ")
    if ans=="1":
      print "\n Your " + partes[3] + " " + partes[4] + " " +partes[5] + " " + partes[6] + " " + partes[7] + " is at " + partes[12] + " " + u'\u2103'
    elif ans=="2":
      fanspeed0100 = raw_input('Insert value from 0 to 100. 80 is recommended.' +"\n")
      fanspeedset = os.popen('aticonfig --pplib-cmd "set fanspeed 0  '+ fanspeed0100 + '"')
      print 'Your fan speed have been set to ' + fanspeed0100 + '%.'

    elif ans=="0":
        import sys
        sys.exit()
    elif ans !="":
      print("\n Not Valid Choice. Try again")