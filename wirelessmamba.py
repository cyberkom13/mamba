import os
import sys
import re
import random
import os.path


Menu="""
                                                                                                        

                                                                                                                                                     
@@@  @@@  @@@  @@@  @@@@@@@   @@@@@@@@  @@@       @@@       @@@@@@@@   @@@@@@    @@@@@@      @@@@@@@@@@    @@@@@@   @@@@@@@@@@   @@@@@@@    @@@@@@   
@@@  @@@  @@@  @@@  @@@@@@@@  @@@@@@@@  @@@       @@@       @@@@@@@@  @@@@@@@   @@@@@@@      @@@@@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@  @@@@@@@@  
@@!  @@!  @@!  @@!  @@!  @@@  @@!       @@!       @@!       @@!       !@@       !@@          @@! @@! @@!  @@!  @@@  @@! @@! @@!  @@!  @@@  @@!  @@@  
!@!  !@!  !@!  !@!  !@!  @!@  !@!       !@!       !@!       !@!       !@!       !@!          !@! !@! !@!  !@!  @!@  !@! !@! !@!  !@   @!@  !@!  @!@  
@!!  !!@  @!@  !!@  @!@!!@!   @!!!:!    @!!       @!!       @!!!:!    !!@@!!    !!@@!!       @!! !!@ @!@  @!@!@!@!  @!! !!@ @!@  @!@!@!@   @!@!@!@!  
!@!  !!!  !@!  !!!  !!@!@!    !!!!!:    !!!       !!!       !!!!!:     !!@!!!    !!@!!!      !@!   ! !@!  !!!@!!!!  !@!   ! !@!  !!!@!!!!  !!!@!!!!  
!!:  !!:  !!:  !!:  !!: :!!   !!:       !!:       !!:       !!:            !:!       !:!     !!:     !!:  !!:  !!!  !!:     !!:  !!:  !!!  !!:  !!!  
:!:  :!:  :!:  :!:  :!:  !:!  :!:        :!:       :!:      :!:           !:!       !:!      :!:     :!:  :!:  !:!  :!:     :!:  :!:  !:!  :!:  !:!  
 :::: :: :::    ::  ::   :::   :: ::::   :: ::::   :: ::::   :: ::::  :::: ::   :::: ::      :::     ::   ::   :::  :::     ::    :: ::::  ::   :::  
  :: :  : :    :     :   : :  : :: ::   : :: : :  : :: : :  : :: ::   :: : :    :: : :        :      :     :   : :   :      :    :: : ::    :   : :  
                                                                                                                                                     



 from ascii.co.uk
______________________________

MAMBA's QUICK WIRELESS SCAN 

"""

def show_interfaces():
    os.system("sudo airmon-ng")

def interfaces():
    print("WIRELESS INTERFACES")
    print("\n")
    os.system("sudo airmon-ng|grep phy")
    os.system("sudo airmon-ng|grep phy > interfaces.txt")
    print("\n")

def get_interfaces(interface_file):

    #interfaces_file is the path of the file generated automatically 
    # by function interfaces(): 

    lines=[]
    interfaces=[]
    phys=[]
    interface=[]

    interface_file=open(interface_file,"r")
    lines = interface_file.readlines()

    for i in lines:
        if re.search("phy",i):
            interface = i.split(" ")
            interface= interface[0].split("\t")
            phys.append(interface[0])
            interfaces.append(interface[1])

    return interfaces,phys #Returns a tuple.

def mac_changing(interface):
    print("\n")
    print("Changing MAC...")
    os.system(f"sudo ifconfig {interface} down")
    print("Device down")
    print("\n")
    os.system(f"sudo macchanger -r {interface}")
    print("\n")
    print("New random MAC assigned to device")
    os.system(f"sudo ifconfig {interface} up")
    print("Device up")
    print("MAC changed. \n")

def mac_restorage(interface):
    print("\n")
    print("Restoring MAC...")
    os.system(f"sudo ifconfig {interface} down")
    print("Device down")
    #os.system(f"sudo iwconfig {interface} mode managed")
    os.system(f"sudo macchanger -p {interface}")
    print("New random MAC assigned to device")
    os.system(f"sudo ifconfig {interface} up")
    print("Device up")
    print("MAC Restored. \n")

def monitor_mode_on(choosen_interface):
    #os.system(f"sudo airmon-ng {choosen_interface} start > monitor.txt")
    print("INTERFACE SELECTED ON MANAGED MODE\n")
    os.system(f"sudo airmon-ng|grep {choosen_interface}")
    print("\n")

    print(f"Starting {choosen_interface} in monitor mode...")
    os.system(f"sudo airmon-ng start {choosen_interface}")
    os.system("sudo airmon-ng > monitor.txt")
    print(f"Monitor mode activated.")

def phy_for_interface(interfaces,phys,selected_interface):

    interfaces=interfaces
    phys=phys
    selected_interface=selected_interface
    
    return phys[interfaces.index(selected_interface)]

def get_monitor_interface(monitor_interface_file, phy):
    phy=phy
    file=open(monitor_interface_file,"r")
    r_content=file.readlines()

    for i in r_content:
        if re.search(phy,i):
            interface_line = i.split(" ")
            interface_line= interface_line[0].split("\t")
            interface=interface_line[1]

    return interface

def monitor_mode_off(monitor_interface):
    monitor_interface=monitor_interface
    os.system(f"sudo airmon-ng stop {monitor_interface}")

def kill_net_process():
    os.system("sudo airmon-ng check kill")

def restore_services():
    print("Restoring network processes") 
    os.system("sudo service network-manager start")
    os.system("sudo service avahi-daemon start")
    print("Network processes restored")

def dump_all(choosen_interfaces):
    choosen_interface=choosen_interfaces
    os.system(f"sudo airodump-ng -M {choosen_interface}|grep WPA")

def dump_ap0(monitor_interface, ap_bssid, channel):
    random_n=random.randint(1,9999)
    monitor_interface=monitor_interface
    ap_bssid=ap_bssid
    channel=channel
    os.system(f"sudo airodump-ng -M --bssid {ap_bssid} --channel {channel} -w {random_n} {monitor_interface}")

def dump_ap1(monitor_interface, ap_bssid, essid):
    random_n=random.randint(1,9999)
    monitor_interface=monitor_interface
    ap_bssid=ap_bssid
    essid=essid
    os.system(f"sudo airodump-ng -M --bssid {ap_bssid} --essid {essid} -w {random_n} {monitor_interface}")

def dump_ap2(monitor_interface, ap_bssid, essid, channel):
    random_n=random.randint(1,9999)
    monitor_interface=monitor_interface
    ap_bssid=ap_bssid
    essid=essid
    channel=channel
    os.system(f"sudo airodump-ng -M --bssid {ap_bssid} --essid {essid} --channel {channel} -w {random_n} {monitor_interface}")

#PART 1  WIRELESS INTERFACE EXTRACTION

print("\n")


print(Menu)


print("\n")

interfaces()
interfaces, phys=get_interfaces("interfaces.txt")
print(interfaces)
print(phys)
print("\n")
selected_interface=input("Please insert the interface you want to use: ")

print("\n")

for i in interfaces:
    print(i)
    if re.search(selected_interface,i):
        continuity=1
        break
    
    else:
        continuity=0

if continuity==0:
    print("Wrong wireless interface selected, choose another one...")
    sys.exit()

mac_changing(selected_interface) 

kill_net_process()

monitor_mode_on(selected_interface)

phy=phy_for_interface(interfaces,phys, selected_interface)

monitor_interface=get_monitor_interface("monitor.txt", phy)

print(f"The interface in monitor mode is {monitor_interface}")

mac_changing(monitor_interface)

dump_all(monitor_interface)

while continuity== True:

    print("Which AP doy want to monitor?")
    print("\n")
    print("According what you'd like to do, select the following options:")
    print("1.BSSID/CHANNEL")
    print("2.BSSID/ESSID")
    print("3.BSSID/CHANNEL/ESSID")
    print("4.Exit")
    print("\n")

    option=input("Select options: ")
    exit_var=False

    if option == "1":
        continuity= False 
        bssid=input("Insert BSSID: ")
        channel=input("Insert channel: ")
        dump_ap0(monitor_interface, bssid, channel)
    elif option == "2": 
        continuity= False 
        bssid=input("Insert BSSID: ")
        essid=input("Insert ESSID: ")
        dump_ap1(monitor_interface, bssid, essid)
    elif option == "3": 
        continuity= False 
        bssid=input("Insert BSSID: ")
        essid=input("Insert ESSID: ")
        channel=input("Insert channel: ")
        dump_ap2(monitor_interface, bssid, essid, channel)
    elif option =="4": 
        print("See you!")
        print("\n")
        continuity= False 
        
    else:
        print("No-Option was selected...")
        print("Please try again!")
        print("\n")


monitor_mode_off(monitor_interface)

show_interfaces()

mac_restorage(selected_interface)

restore_services()


    
        
