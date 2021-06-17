#!/usr/bin/env  python3


import os

os.system("pkg install nmap -y")
os.system("pkg install figlet -y")
os.system("clear")
os.system("figlet ULTIMATE SCANNER")
print("""
Ultimate Scanner for websites

1) Basic Info About The Site
2) Fast Port Scan
3) Version Info
4) About USFW
5) DDos Attack
6)SqlInjection
7)Update
""")
WhatDoYouWant = input("Choose a Number")

if WhatDoYouWant=="1":
	os.system("clear")
	WebSite= input ("Enter the Web Site:")
	os.system("whois "+WebSite)
elif WhatDoYouWant=="2":
	os.system("clear")
	WebSite=input("Enter the Web Site:")
	os.system("nmap "+WebSite)
elif WhatDoYouWant=="3":
	os.system("clear")
	Website=input("Enter the Web Site:")
	os.system("nmap -sV "+Website)
elif WhatDoYouWant=="4":
	os.system("clear")
	print("MADE BY EA")
	print("Version 2.3")
	os.system("figlet MADE WITH PAIN")
elif WhatDoYouWant=="5":
	os.system("clear")
	os.system("git clone https://github.com/cyweb/hammer")
	print("now write cd hammer to console then python3 hammer.py")

elif WhatDoYouWant=="6":
	os.system("clear")
	os.system("git clone https://github.com/payloadbox/sql-injection-payload-list")
	os.system("clear")
	os.system("figlet Done!!!")


elif WhatDoYouWant=="7":
	os.system("git clone https://github.com/mantryt/USFW")
	os.system("clear")
	os.system("figlet Updated")
 
