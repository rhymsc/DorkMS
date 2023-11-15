# !/usr/bin/env/python3
# This Python file uses the following encoding: utf-8

from __future__ import print_function
try:
    from googlesearch import search
    import tldextract
except ImportError:
    print("")

import sys
import time

if sys.version[0] in "2":
    print("\n[x] Not Supported For python 2.x Use Python 3.x \n")
    print("\n\n\tRhyRU9 \033[1;91mI LOOTING \033[0m😃\n\n")
    exit()

class colors:
    CRED2 = "\33[91m"
    CBLUE2 = "\33[94m"
    ENDC = "\033[0m"

banner = ("""
          ______ _          ______ _   _  _____  
          | ___ \ |         | ___ \ | | ||  _  | 
          | |_/ / |__  _   _| |_/ / | | || |_| | 
          |    /| '_ \| | | |    /| | | |\____ | 
          | |\ \| | | | |_| | |\ \| |_| |.___/ / 
          \_| \_|_| |_|\__, \_| \_|\___/ \____(_)
                        __/ |                    
                       |___/                     
""")

for col in banner:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0025)

x = ("""
                Github:  https://github.com/rhymsc """)
for col in x:
    print(colors.CBLUE2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

y = "\n\t\tlet's Play \n"
for col in y:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

z = "\n"
for col in z:
    print(colors.ENDC + col, end="")
    sys.stdout.flush()
    time.sleep(0.4)

try:
    data = input("\n[+] Do You Like To Save The Output In A File? (Y/N) ").strip()
    l0g = ("")

except KeyboardInterrupt:
        print("\n")
        print("\033[1;91m[!] Interruption..!\033[0")
        time.sleep(0.5)
        print("\n\n\t\033[1;91m[!] use sparingly \033[0m\n\n")
        time.sleep(0.5)
        sys.exit(1)

def logger(data):
    file = open((l0g) + ".txt", "a")
    file.write(str(data))
    file.write("\n")
    file.close()

if data.startswith("y" or "Y"):
    l0g = input("[~] Give The File a Name: ")
    print("\n" + "  " + "»" * 78 + "\n")
    logger(data)
else:
    print("[!] Saving is Skipped...")
    print("\n" + "  " + "»" * 78 + "\n")

def dorks():
    try:
        dork = input("\n[+] Dork Search Query: ")
        amount = input("[+] Number Of Websites To Display: ")
        print("\n ")

        requ = 0

        for result in search(dork, tld="com", lang="en", num=int(amount), start=0, stop=None, pause=2):
            ext = tldextract.extract(result)
            if ext.subdomain:
                full_url = f"https://{ext.subdomain}.{ext.domain}.{ext.suffix}"
            else:
                full_url = f"http://{ext.domain}.{ext.suffix}"
            
            print(full_url)
            time.sleep(0.1)
            requ += 1
            if requ >= int(amount):
                break

            data = (full_url)

            logger(data)
            time.sleep(0.1)

    except KeyboardInterrupt:
            print("\n")
            print("\033[1;91m[!] Interruption..!\033[0")
            time.sleep(0.5)
            print("\n\n\t\033[1;91m[!] use sparingly \033[0m\n\n")
            time.sleep(0.5)
            sys.exit(1)

    print("[•] Done... Exiting...")
    print("\n\t\t\t\t\033[34mRhyRU9\033[0m")
    print("\t\t\033[1;91m[!] use sparingly \033[0m\n\n")
    sys.exit()

# =====# Main #===== #
if __name__ == "__main__":
    dorks()
