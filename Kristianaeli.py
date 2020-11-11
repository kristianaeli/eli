
#!/bin/bash
#version 1.0

#MAU NGAPAIN TOT?:V
#RECODE?REEDIT?RECOPYRIGHT?COPAS?
#MALU TOLOL!!!
#KAGA BERMORAL!


#01/08/18

clear
# Variables
b='\033[1m'
u='\033[4m'
bl='\E[30m'
r='\E[31m'
g='\E[32m'
bu='\E[34m'
m='\E[35m'
c='\E[36m'
w='\E[37m'
endc='\E[0m'
enda='\033[0m'
blue='\e[1;34m'
cyan='\e[1;36m'
red='\e[1;31m'

figlet TUAN B4DUT  | lolcat

echo -b "_____________________________________________________________" | lolcat
echo -b "TYPE      : TOOLS INSTALLER $green " |lolcat
echo -b "VERSION   : V.3 " | lolcat
echo -b "TOTALS    : 2 TOOLS " | lolcat
echo -b "AUTHOR    : MANTAN PERAWAN $green " |lolcat
echo -b "ASSOCIATE : INDONESIAN TERMUX ASSOCIATION $green " |lolcat
echo -b "ASSOCIATE : INDONESIAN TERMUX TUTORIAL $green " |lolcat
echo -b "ASSOCIATE : INDONESIAN DARK TERMUX ASSOCIATE $green " |lolcat
echo -b "NOTES     : JELAJAHI SETIAP TOOLS DENGAN BIJAK " | lolcat
echo -b "_____________________________________________________________" | lolcat

sleep 1

###################################################
# CTRL + C
###################################################
trap ctrl_c INT
ctrl_c() {
clear
echo -b $green"[#]> TOOLS YANG KALIAN INSTALL ADA DI DIRECTORY TOOLS GUA " |lolcat
echo -b $green"[#]> Thanks For Using My Tools" |lolcat
sleep 1
echo -b $green"[#]> MANTAN PERAWAN On Your System" |lolcat

echo -b $green"[#]> See you Again SCRIPTKIDDIESðŸ˜Ž :)..." |lolcat
figlet TUAN B4DUT | lolcat
sleep 1
exit
}


lagi=1
while [ $lagi -lt 6 ];
do

echo ""
echo ""

echo -e "######################################" | lolcat
echo -e "#SILAHKAN TUNGGU DAN LIHAT LIST TOOLS#" | lolcat
echo -e "######################################" | lolcat

echo ""
echo -e "============================" | lolcat
echo -e $b "1. Install Tool DarkFb Token${enda}";
echo -e "============================" | lolcat
echo -e $b "2. Install Tool DarkFb Cokies${endcla}";
echo -e "============================" | lolcat
echo -e $b "00. Exit${enda}";
echo -e "============================" | lolcat
echo -e "â•­â”€[PILIH NOMORNYA]"
read -p "   â•°â”€root@./MANTAN PERAWAN=" pil;

#Install Tool DarkFb Token

case $pil in
1) git clone https://github.com/MantanPrawan/khairulfatihin"
echo -e "${y} cd khairulfatihin"
echo -e "${y} python2 khairulfatihin.py"

echo

;;

#Install  Tool DarkFb Cokies

2) git clone https://github.com/cyberlombok/cyberlombok"
echo -e "${y} pkg install git curl python"
echo -e "${y} pkg install ruby"
echo -e "${y} pip install mechanize requests bs4 futures"
echo -e "${y} cd cyberlombok"
echo -e "${y} python cyberlombok.py"

echo

;;

00) echo "AUTHOR: CYBER LOMBOK" | lolcat
echo "CYBER LOMBOK ON YOUR SYSTEM" | lolcat
echo "INDONESIAN TERMUX ASSOCIATION" | lolcat
echo "SEMUA TOOLS YANG KALIAN INSTALL ADA DI DIRECTORY TOOLS GUA" | lolcat
figlet LOMBOK CYBER | lolcat
exit
;;

*) echo "Sorry, Your choices it's not already [T4T]"
esac
done
done

#[696969696969]
#[Mantan Prawan]
