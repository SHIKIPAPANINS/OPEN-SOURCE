#-----------CREATED BY SHIKIPAPANINS-----------#
#-----------TOOLS BY TERMUX COMMAND SETUP-----------#

#------------[ IMPORT ]------------#

import os , time
#-------------[ COLOR ]-------------#
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
#--------------[ LOGO ]--------------#
logo = ("""
\033[1;34m
███████╗███████╗████████╗██╗   ██╗██████╗ 
██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗
███████╗█████╗     ██║   ██║   ██║██████╔╝
╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝ 
███████║███████╗   ██║   ╚██████╔╝██║     
╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝
\033[1;91m ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 \033[1;92m┃ [\033[1;91m✓\033[1;92m] CREATOR   \033[1;91m: \033[1;92mSHIKI TEODORO
\033[1;23m ┃ [\033[1;91m✓\033[1;99m] GITHUB    \033[1;91m: \033[1;99mSHIKIPAPANINS
\033[1;93m ┃ [\033[1;91m✓\033[1;97m] TOOL      \033[1;91m: \033[1;97mTERMUX COMMAND SETUP 
\033[1;92m ┃ [\033[1;91m✓\033[1;96m] REPIIT    \033[1;91m: \033[1;96mSHIKITEODORO         
 \033[1;33m┃ [\033[1;91m✓\033[1;937m] FBLINK    \033[1;91m: \033[1;92mwww.facebook.com/shikiteodoro      
\033[1;17m ┃ [\033[1;91m✓\033[1;92m] VERSION   \033[1;91m: \033[1;33m1.0        
 \033[1;37m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
manu = (f"""{RED}
[1] BASIC SETUP
[2] CONTACT WITH ME
[3] JOIN MESSENGER
[4] EXIT
""")

def setup():
    os.system('''apt update && apt upgrade && pkg update && pkg upgrade && pkg install python && pkg install python2 && pkg install python3 && pkg install git && pip install requests && pip2 install requests && pip2 install requests pip install mechanize && pip install mechanize && pip install lolcat && pip install requests bs4 && pip install rich && pip install ruby && pip install futures && pip2 install futures && pip install requirements && pip install espeak && pip install pycurl && pip2 install pycurl && pip2 install pycryptodomex && termux-setup-storage''')

def join():
    os.system('xdg-open https://www.facebook.com/shikiteodoro')

def main():
   os.system('clear')
   print(logo)
   print('')
   print(manu)
   option = input(f'{GREEN}CHOOSE : ')
   if option == '1':
      setup()
   if option == '2':
        join()
   if option == '3':
    os.system('xdg-open https://m.me/j/Abap0mtYvPwGlcFT/')
   if option == '4':
         exit

main()