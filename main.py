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
def getTemp(adapter=0):
    """
    Gets the temperature of the chosen adapter. Adapter 0 is the defult
    adapter that will be returned if no arguments are provided.
    :rtype : object
    :param adapter: The adapter whose temperature will be returned.
    :return: The temperature of the adapter as a string.
    """
    get_temp = subprocess.check_output('aticonfig --odgt --adapter={}'.format(adapter), shell=True)
    odgt = str(get_temp, encoding='ascii')
    odgtline = odgt.replace('\n', ' ')
    print(odgt[75:82])


def setFanSpeed(gpuid=0):
    fanspeed0100 = input('Insert value from 0 to 100. 80 is recommended. \n')
    fanspeedset = os.popen('aticonfig --pplib-cmd "set fanspeed {}  '+ fanspeed0100 + '"'.format(gpuid))
    print('Your fan speed has been set to {}%'.format(fanspeed0100))


def getnumadapters():
    get_adapters = os.popen('aticonfig --list-adapters').read()
    print(get_adapters)
    numadapters = get_adapters.count("ATI")
    print(numadapters)
    return numadapters


#Main Menu
ans = True
while ans:

   print("""
   1.Check your FGLRX driver version
   2.Show your GPU(s)
   3.Show name and temperature for primary GPU
   4.Manually set fan speed for primary GPU
   0.Exit/Quit
   """)

   ans = input("What would you like to do? ")


   if ans == "1":
      getdriverver()

   elif ans == "2":
      getTemp()

   elif ans == "0":
      sys.exit()

   else:
      print('\n Not Valid Choice. Try again')
