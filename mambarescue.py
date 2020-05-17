import os
import sys
import re
import random
import os.path


Menu="""
                                                                                                        

                                                                                                                                                     
                                                                                                                       
@@@@@@@@@@    @@@@@@   @@@@@@@@@@   @@@@@@@    @@@@@@      @@@@@@@   @@@@@@@@   @@@@@@    @@@@@@@  @@@  @@@  @@@@@@@@  
@@@@@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@  @@@@@@@@     @@@@@@@@  @@@@@@@@  @@@@@@@   @@@@@@@@  @@@  @@@  @@@@@@@@  
@@! @@! @@!  @@!  @@@  @@! @@! @@!  @@!  @@@  @@!  @@@     @@!  @@@  @@!       !@@       !@@       @@!  @@@  @@!       
!@! !@! !@!  !@!  @!@  !@! !@! !@!  !@   @!@  !@!  @!@     !@!  @!@  !@!       !@!       !@!       !@!  @!@  !@!       
@!! !!@ @!@  @!@!@!@!  @!! !!@ @!@  @!@!@!@   @!@!@!@!     @!@!!@!   @!!!:!    !!@@!!    !@!       @!@  !@!  @!!!:!    
!@!   ! !@!  !!!@!!!!  !@!   ! !@!  !!!@!!!!  !!!@!!!!     !!@!@!    !!!!!:     !!@!!!   !!!       !@!  !!!  !!!!!:    
!!:     !!:  !!:  !!!  !!:     !!:  !!:  !!!  !!:  !!!     !!: :!!   !!:            !:!  :!!       !!:  !!!  !!:       
:!:     :!:  :!:  !:!  :!:     :!:  :!:  !:!  :!:  !:!     :!:  !:!  :!:           !:!   :!:       :!:  !:!  :!:       
:::     ::   ::   :::  :::     ::    :: ::::  ::   :::     ::   :::   :: ::::  :::: ::    ::: :::  ::::: ::   :: ::::  
 :      :     :   : :   :      :    :: : ::    :   : :      :   : :  : :: ::   :: : :     :: :: :   : :  :   : :: ::   
                                                                                                                       
                                                                                                                                                     

 from ascii.co.uk
______________________________

MAMBA's QUICK WIRELESS ADAPTER RESTORING...

"""


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

def monitor_mode_off(monitor_interface):
    monitor_interface=monitor_interface
    os.system(f"sudo airmon-ng stop {monitor_interface}")

def show_interfaces():
    os.system("sudo airmon-ng")

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

def restore_services():
    print("Restoring network processes") 
    os.system("sudo service network-manager start")
    os.system("sudo service avahi-daemon start")
    print("Network processes restored")

#MAIN PROGRAM   
  

print("\n")

print(Menu)


print("\n")

interfaces()
interfaces, phys=get_interfaces("interfaces.txt")
print(interfaces)
print(phys)
print("\n")
selected_interface=input("Please insert the interface you want to rescue: ")

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


monitor_mode_off(selected_interface)

show_interfaces()

restore_services()

