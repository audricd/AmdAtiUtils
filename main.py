#!/usr/bin/env python3

__author__ = 'audricd'

"""
amdatiutils
ver 0.0.5
"""

import os
import sys
import subprocess

#detects fglrx
linea0 = os.popen('aticonfig --odgt --adapter=0').read().replace('\n', ' ')
if not "ATI" in linea0:

   print('You do not have FGLRX installed')
   sys.exit()

#welcome message
print('Welcome to AmdAtiUtils v0.0.5. \nWarning: use this software under your responsability.'
      ' Overclocking and setting wrong fan speed can damage your hardware.')



#gets/splits info of the GPU
partesid0temp0 = linea0.split()

#gets driver version + date
def getdriverver():
    checkfglrx = os.popen('dmesg | grep fglrx | grep module | grep loaded').read().split()
    fglrxver = checkfglrx[7:11]
    print("\n You are using FGLRX driver version {} {} {} {}".format(fglrxver[0],
                                                                     fglrxver[1],
                                                                     fglrxver[2],
                                                                     fglrxver[3],))
    return fglrxver

#gets temperature for adapter0
def gettemp0():
   get_temp0 = subprocess.check_output('aticonfig --odgt --adapter=0', shell=True)
   temp = str(get_temp0)
   temp = temp[79:84]
   return temp


#Main Menu
ans = True
while ans:

   print("""
   1.Check your FGLRX driver version
   2.Show name and temperature for primary GPU
   3.Manually set fan speed for primary GPU
   0.Exit/Quit
   """)

   ans = input("What would you like to do? ")


   if ans == "1":
      getdriverver()

   elif ans == "2":
      print("\n Your {} {} {} {} {} is at {}°C ".format(partesid0temp0[3],
                                                        partesid0temp0[4],
                                                        partesid0temp0[5],
                                                        partesid0temp0[6],
                                                        partesid0temp0[7],
                                                        gettemp0()))

   elif ans == "3":
      fanspeed0100 = input('Insert value from 0 to 100. 80 is recommended. \n')
      fanspeedset = os.popen('aticonfig --pplib-cmd "set fanspeed 0  '+ fanspeed0100 + '"')
      print('Your fan speed has been set to {}%'.format(fanspeed0100))


   elif ans == "0":
      sys.exit()

   else:
      print('\n Not Valid Choice. Try again')
