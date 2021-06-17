#!/usr/bin/env  python3

import os

os.system("pkg install nmap")
os.system("pkg install figlet")
os.system("clear")
os.system("figlet ULTIMATE SCANNER")
print("""
Ultimate Scanner for websites


1) Basic Info About The Site
2) Fast Port Scan
3) Version Info
4) About USFW
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
	print("Version 1.0")
	os.system("figlet MADE WITH PAIN")
