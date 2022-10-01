Assignment from Lahav 433 Cyber Unit :

In order to run the script nmap-vuln you will need to install the next dependencies(Linux OS) :

    install nmap
    install python-nmap package

all methods except those contain vulnerability check can be proccessed only with nmap,the reason you will need to install nmap is because some flags may need root privileges and thos ecan granted to nmap as a software and not python-nmap as a library, if you wish you can still run it through the root user.



1.install next dependencies by typing these commands to terminal:

    sudo apt-get install nmap
    
2.install python package python-nmap by using pip

    pip install python-nmap



now, because nmap requires root privileges for many flags , unless you will use root or sudo - you will need to give nmap special root priviliages , so you will need 
to install libcap2 so write these commands:

    sudo apt-get install libcap2-bin
    sudo setcap cap_net_raw,cap_net_admin,cap_net_bind_service+eip $(which nmap)
    getcap $(which nmap)
    
    for more information check :https://www.maketecheasier.com/run-nmap-without-root-or-sudo/

next : in order to run the telegram bot and to connect it with our nmap-vuln code you will need to install
python-telegram-bot

    pip install python-telegram-bot.
    
**in the Key file you will need to place your own API-KEY you got from bot-father on telegram for your own bot
    
now you can enter terminal , locate the telegram_nmap_bot.py and execute it ,don't forget to use sudo/root or just adding --privileged in nmap_vuln if you used libcap2 .
