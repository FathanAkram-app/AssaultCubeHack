from pymem import *
from pymem.process import *
import time

pm = pymem.Pymem("ac_client.exe")

# Memory Offset adress
# 00FEA0C8 + F8 = Health
# 150 = Primary Ammo
# 13C = Secondary Ammo
# 158 = Grenade

# Address utama yang gak bakal ganti walaupun gamenya ditutup 
# kita namakan base static address
baseStaticAddress = 0x00509B74
# kita ambil dynamic address yang di simpan di static address
base = pm.read_int(baseStaticAddress)
# beberapa offset, data bisa di manipulasi menggunakan 
# base ditambah value dibawah ini
# dengan contoh variable base adalah rumah, 
# dan variable dibawah adalah ruangan yang ingin kita pakai
health = 0xf8
primaryAmmo = 0x150
secondaryAmmmo = 0x13C
grenade = 0x158
# ini adalah contoh penulisan value memory di python pymem
# pm.write_int(base+health, value)

while True:
    print(base)
    print("Assault Cube Hack by FTHN")
    print("[1]Set Your Health")
    print("[2]Set Your Primary Ammo")
    print("[3]Set Your Secondary Ammo")
    print("[4]Set Your Grenade")
    userInput = input("choose a number:")
    if int(userInput) == 1:
        value = int(input("Health Value: "))
        pm.write_int(base+health, value)
        print("Your health has been set to %s"%value)
        time.sleep(1)
    elif int(userInput) == 2:
        value = int(input("Primary Ammo Value: "))
        pm.write_int(base+primaryAmmo, value)
        print("Your primary ammo has been set to %s"%value)
        time.sleep(1)
    elif int(userInput) == 3:
        value = int(input("Secondary Ammo Value: "))
        pm.write_int(base+secondaryAmmmo, value)
        print("Your Secondary ammo has been set to %s"%value)
        time.sleep(1)
    elif int(userInput) == 4:
        value = int(input("Grenade Value: "))
        pm.write_int(base+grenade, value)
        print("Your Grenade has been set to %s"%value)
        time.sleep(1)
    


