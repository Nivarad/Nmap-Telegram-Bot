Assignment from Lahav 433 Cyber Unit :

In order to run the script nmap-vuln you will need to install the next dependencies(Linux OS) :

    install nmap
    install nmap-vulners
    install python-nmap package

all methods except those contain vulnerability check can be proccessed only with nmap,
in order to use the vulnrability check you will need to use the NSE engine script to use nmap-vulners



1.install next dependencies by typing these commands to terminal:

    sudo apt-get install nmap
    git clone https://github.com/vulnersCom/nmap-vulners.git
    
2.install python package python-nmap by using pip

    pip install python-nmap

*you will need to modify the nmap-vulners path inside the nmap_vuln class

** The python-nmap can work independently without installing nmap , but if you will use linux , there will be some commands
that need sudo privileges and those can only be given to a predefined script/ tool and not the python package 

now in order to run the script from any user you will need to give nmap root priviliages , so you will need 
to install libcap2 - write these commands:

    sudo apt-get install libcap2-bin
    sudo setcap cap_net_raw,cap_net_admin,cap_net_bind_service+eip $(which nmap)
    getcap $(which nmap)
    for more information check :https://www.maketecheasier.com/run-nmap-without-root-or-sudo/

next : in order to run the telegram bot and to connect it with our nmap-vuln code you will need to install
python-telegram-bot

    pip install python-telegram-bot.
    
***in the Key file you will need to place your own API-KEY you got from bot-father on telegram for your own bot
    
