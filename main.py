#!/usr/bin/env python3

__author__ = 'audricd'

"""
amdatiutils
ver 0.1.2
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
print('Welcome to AmdAtiUtils v0.1.0 \nWarning: use this software under your responsability.'
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

def getName(adapter=0):
    get_name = subprocess.check_output('aticonfig --odgt --adapter={}'.format(adapter), shell=True)
    odgtn = str(get_name, encoding='ascii')
    lineas = odgtn.split("\n")
    lineanombre = lineas[1]
    nombre = lineanombre[12:]
    print = str(nombre)
    return nombre

def getTemp(adapter=0):
    get_temp = subprocess.check_output('aticonfig --odgt --adapter={}'.format(adapter), shell=True)
    odgtt = str(get_temp, encoding='ascii')
    odgtline = odgtt.replace('\n', ' ')
    lenodgt = len(odgtt)
    temp = odgtt[lenodgt-8:-1]
    nombre = getName(adapter=adapter)
    print("Your "+nombre+" is at "+temp)




def getFanSpeed(adapter=0):
    get_fanspeed = subprocess.check_output('aticonfig --pplib-cmd "get fanspeed {}"'.format(adapter), shell=True)
    fanspeedresult = str(get_fanspeed, encoding='ascii')
    nombre = getName(adapter=adapter)
    print("Your "+nombre+ " fanspeed is going at "+fanspeedresult[70:73])

def setFanSpeed(adapter=0):
    fanspeed0100 = input('Insert value from 0 to 100. 80 is recommended. \n')
    fanspeedset = os.popen('aticonfig --pplib-cmd "set fanspeed {}  '+ fanspeed0100 + '"'.format(adapter))
    nombre = getName(adapter=adapter)
    print("Your " +nombre+" fan speed has been set to {}%".format(fanspeed0100))


def getnumadapters():
    get_adapters = os.popen('aticonfig --list-adapters').read()
    numadapters = get_adapters.count("ATI")
    return numadapters


numadapters = getnumadapters()

#Main Menu
ans = True
while ans:

   print("""
   1.Check your FGLRX driver version
   2.Show your GPU(s)
   3.Check GPU temperature
   4.Check GPU fanspeed
   5.Set GPU fanspeed
   0.Exit/Quit
   """)

   ans = input("What would you like to do? ")


   if ans == "1":
      getdriverver()

   elif ans == "2":
      get_adapters = os.popen('aticonfig --list-adapters').read()
      print(get_adapters)

   elif ans == "3":
      anstempgpuid = input("Which GPU temperature would you like to check? Input GPU ID as shown in option 2\n"
                           "Reminder: you have " + str(numadapters) + " GPU(s). ID of the first one is 0, the second is 1, and so on.\n")
      getTemp(adapter=anstempgpuid)

   elif ans =="4":
      anscheckfanspeed = input("Which GPU fanspeed would you like to check? Input GPU ID as shown in option 2\n"
                               "Reminder: you have " + str(numadapters) + " GPU(s). ID of the first one is 0, the second is 1, and so on.\n")
      getFanSpeed(adapter=anscheckfanspeed)

   elif ans =="5":
      anssetfanspeed = input("Which GPU fanspeed would you like to set? Input GPU ID as shown in option 2\n"
                             "Reminder: you have " + str(numadapters) + " GPU(s). ID of the first one is 0, the second is 1, and so on.\n")
      setFanSpeed(adapter=anssetfanspeed)

   elif ans =="6":
      print(getName(adapter={}).format(adapter))


   elif ans == "0":
      sys.exit()

   else:
      print('\n Not Valid Choice. Try again')
