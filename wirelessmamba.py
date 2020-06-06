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
                                                                                                                                                     
Generated at: ascii.co.uk
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
    os.system(f"echo bssid={ap_bssid}>> monitor.txt")
    os.system(f"sudo airodump-ng -M --bssid {ap_bssid} --channel {channel} -w {random_n} {monitor_interface}")
    
def dump_ap1(monitor_interface, ap_bssid, essid):
    random_n=random.randint(1,9999)
    monitor_interface=monitor_interface
    ap_bssid=ap_bssid
    essid=essid
    os.system(f"echo bssid={ap_bssid}/essid={essid}>> monitor.txt")
    os.system(f"sudo airodump-ng -M --bssid {ap_bssid} --essid {essid} -w {random_n} {monitor_interface}")
    
def dump_ap2(monitor_interface, ap_bssid, essid, channel):
    random_n=random.randint(1,9999)
    monitor_interface=monitor_interface
    ap_bssid=ap_bssid
    essid=essid
    channel=channel
    os.system(f"echo bssid={ap_bssid}/essid={essid}>> monitor.txt")
    os.system(f"sudo airodump-ng -M --bssid {ap_bssid} --essid {essid} --channel {channel} -w {random_n} {monitor_interface}")

def check_networks(choosen_interface):
    os.system(f"sudo iwlist {choosen_interface} scan > networks.txt")

def get_networks():
    net_file=open("networks.txt","r")
    net_lines=net_file.readlines()

    mac_addresses=[]
    channels=[]
    essids=[]

    net_file.close()


    for i in net_lines:
        if re.search("Address: ",i):
            mac_address_line=i.replace("\n","")
            mac_address_line=mac_address_line.split("Address: ")
            mac_addresses.append(mac_address_line[1])

        if re.search("Channel:",i):
            channel_line=i.replace("\n","")
            channel_line=channel_line.split(":")
            channels.append(channel_line[1])

        if re.search("ESSID:",i):
            essid_line=i.replace("\n","")
            essid_line=essid_line.split(":")
            essids.append(essid_line[1])

    return mac_addresses,channels,essids
    
def show_networks(device_mac_address_list, channel_list, essid_list):

    if len(device_mac_address_list) == len(channel_list) and len(device_mac_address_list) == len(essid_list):

        counter=0

        for i in range(len(device_mac_address_list)):
            #print(f"{counter}. BSSID:{device_mac_address_list[counter]}, CHANNEL:{channel_list[counter]}, ESSID:{essid_list[counter]}")
            print(f"{i}. BSSID:{device_mac_address_list[i]}, CHANNEL:{channel_list[i]}, ESSID:{essid_list[i]}")
            counter +=1 

        print("\n")
    
    else: 
        print("Error with the different list length...")
        sys.exit()


#1.BSSID/CHANNEL (Just for unknown ESSIDs)
#2.BSSID/ESSID
#3.BSSID/CHANNEL/ESSID


def select_network_BC(device_mac_address_list, channel_list): 

    selection=int(input("Please select an option: "))
    print(f"{selection}. BSSID:{device_mac_address_list[selection]}, CHANNEL:{channel_list[selection]}")
    

    return device_mac_address_list[selection], channel_list[selection]

def select_network_BE(device_mac_address_list, essid_list): 

    selection=int(input("Please select an option: "))
    print(f"{selection}. BSSID:{device_mac_address_list[selection]}, ESSID:{essid_list[selection]}")

    return device_mac_address_list[selection], essid_list[selection]

def select_network_BCE(device_mac_address_list, channel_list, essid_list):

    selection=int(input("Please select an option: "))
    print(f"{selection}. BSSID:{device_mac_address_list[selection]}, CHANNEL:{channel_list[selection]}, ESSID:{essid_list[selection]}")

    return device_mac_address_list[selection], channel_list[selection], essid_list[selection]


#PART 1  WIRELESS INTERFACE EXTRACTION

print("\n")


print(Menu)


print("\n")

interfaces()
interfaces, phys=get_interfaces("interfaces.txt")
print(interfaces)

print("\n")

selected_interface=input("Please insert the interface you want to use: ")
check_networks(selected_interface)

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

    print("Which AP do you want to monitor?")
    print("\n")
    print("According what you'd like to do, select the following options:")
    print("1.BSSID/CHANNEL (Just for unknown ESSIDs)")
    print("2.BSSID/ESSID")
    print("3.BSSID/CHANNEL/ESSID")
    print("4.Manual Mode")
    print("5.Exit")
    print("\n")

    option=input("Select options: ")
    exit_var=False

    if option == "1":
        continuity= False 

        bssids=[]
        channels=[]
        essids=[]

        bssids, channels, essids=get_networks()
        show_networks(bssids,channels,essids)
        bssid, channel=select_network_BC(bssids,channels)

        dump_ap0(monitor_interface, bssid, channel)

    elif option == "2": 
        continuity= False 

        bssids=[]
        channels=[]
        essids=[]

        bssids, channels, essids=get_networks()
        show_networks(bssids,channels,essids)
        bssid, essid=select_network_BE(bssids,essids)

        dump_ap1(monitor_interface, bssid, essid)

    elif option == "3": 
        continuity= False 

        bssids=[]
        channels=[]
        essids=[]
        bssids, channels, essids=get_networks()
        show_networks(bssids,channels,essids)
        bssid, channel, essid=select_network_BCE(bssids, channels, essids)

        dump_ap2(monitor_interface, bssid, essid, channel)

    
    elif option == "4": 

        continuity= False

        continuity2=True

        while continuity2 == True:
             

            print("\n")
            print("MANUAL MODE")
            print("Which AP do you want to monitor?")
            print("\n")
            print("According what you'd like to do, select the following options:")
            print("1.BSSID/CHANNEL (Just for unknown ESSIDs)")
            print("2.BSSID/ESSID")
            print("3.BSSID/CHANNEL/ESSID")
            print("4.Exit")
            print("\n")

            option2=input("Select options: ")

            if option2=="1":
                continuity2= False
                print("\n")
                bssid= input("Insert BSSID: ")
                channel = input("Insert Channel: ")
                dump_ap0(monitor_interface, bssid, channel)
                
            elif option2=="2":
                continuity2= False
                bssid= input("Insert BSSID: ")
                essid = input("Insert ESSID: ")
                dump_ap1(monitor_interface, bssid, essid)

                
            elif option2=="3":
                continuity2= False
                print("\n")
                bssid= input("Insert BSSID: ")
                channel = input("Insert Channel: ")
                essid = input("Insert ESSID: ")

                dump_ap2(monitor_interface, bssid, essid, channel)

            elif option2=="4":
                continuity2= False

    elif option =="5": 
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


    
        
