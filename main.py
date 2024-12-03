# ---#---#------[AUTHOR Yuri Evisu]------#---#---#
###----------[ IMPORT LIBRARY ]---------- ###
import requests, os, re, bs4, calendar, sys, json, time, random, datetime, subprocess, logging, base64, uuid
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from time import sleep
from time import sleep as jeda
from time import strftime
from random import choice
from pathlib import Path
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich.text import Text as tekz
from rich.panel import Panel as nel
from rich import print as cetak

###----------[ GLOBAL VARIABLES ]---------- ###
ses = requests.Session()
MAX_WORKERS = 30
SLEEP_INTERVAL = 1

###----------[ CALENDAR ]----------###
bulan = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
tgl = datetime.now().day
bln = bulan[(str(datetime.now().month))]
thn = datetime.now().year
tanggal = (str(tgl)+' '+str(bln)+' '+str(thn))
waktu = strftime('%H:%M:%S')
hari = datetime.now().strftime("%A")

###----------[ WARNA 1 ]---------- ###
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
N = '\x1b[0m'        # WARNA MATI
PT = '\x1b[1;97m'    # PUTIH TEBAL
MT = '\x1b[1;91m'    # MERAH TEBAL
HT = '\x1b[1;92m'    # HIJAU TEBAL
KT = '\x1b[1;93m'    # KUNING TEBAL
BT = '\x1b[1;94m'    # BIRU TEBAL
UT = '\x1b[1;95m'    # UNGU TEBAL
OT = '\x1b[1;96m'    # BIRU MUDA TEBAL

###----------[ WARNA 2 ]---------- ###
Z2 = "[#000000]"     # HITAM
M2 = "[#FF0000]"     # MERAH
H2 = "[#00FF00]"     # HIJAU
K2 = "[#FFFF00]"     # KUNING
B2 = "[#00C8FF]"     # BIRU
U2 = "[#AF00FF]"     # UNGU
N2 = "[#FF00FF]"     # PINK
O2 = "[#00FFFF]"     # BIRU MUDA
P2 = "[#FFFFFF]"     # PUTIH
J2 = "[#FF8F00]"     # JINGGA
A2 = "[#AAAAAA]"     # ABU-ABU

###----------[ USER AGENT ]---------- ###
def random_ua():
    ua_list = [
        'Mozilla/5.0 (Linux; Android 3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.66 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]',
        'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+',
        'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
        'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
        'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
        'Mozilla/5.0 (Linux; U; Android 5.0.1; ru-RU; Lenovo A788t Build/LRX22C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.0.950 U3/0.8.0 Mobile Safari/E7FBAF',
        'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
        'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]'
    ]
    return random.choice(ua_list)

###----------[ LOGO ]----------###
def logo_menu():
    li = '# WELCOME TO FACEBOOK AUTO SHARE TOOL'
    lo = mark(li, style='white')
    sol().print(lo, style='blue')
    banner = f'''
░██████╗██████╗░░█████╗░███╗░░░███╗
██╔════╝██╔══██╗██╔══██╗████╗░████║
╚█████╗░██████╔╝███████║██╔████╔██║
░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║
██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║
╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝

░██████╗██╗░░██╗░█████╗░██████╗░███████╗
██╔════╝██║░░██║██╔══██╗██╔══██╗██╔════╝
╚█████╗░███████║███████║██████╔╝█████╗░░
░╚═══██╗██╔══██║██╔══██║██╔══██╗██╔══╝░░
██████╔╝██║░░██║██║░░██║██║░░██║███████╗
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝
    '''
    cetak(nel(banner,title=f'{P2} {H2}[ {P2}>Yuri Evisu< {H2}]',subtitle_align='left',padding=1,style='red'))

###----------[ LOGIN ]----------###
def login():
    try:
        os.system("clear")
        cetak(nel(f'   {P2}Login Cookies First \n\n              {H2}--[ SUCCESS ]--',title=f'{P2} {H2}[ {P2}Welcome {H2}]',width=54,padding=(1,4),style='blue'))
        cetak(nel(f'{P2} Download Cookies in Kiwi Browser',subtitle=f'{P2}┌─[ Cookies ]',subtitle_align='left',width=54,padding=1,style='blue'))
        cookie = input(f"{P}   └──> : {H}")
        
        with requests.Session() as session:
            try:
                url = "https://business.facebook.com/business_locations"
                headers = {
                    "user-agent": random_ua(),
                    "referer": "https://www.facebook.com/",
                    "host": "business.facebook.com",
                    "origin": "https://business.facebook.com",
                    "upgrade-insecure-requests": "1",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                    "cache-control": "max-age=0",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                    "content-type": "text/html; charset=utf-8"
                }
                cookies = {"cookie": cookie}
                response = session.get(url, headers=headers, cookies=cookies)
                token = re.search("(EAAG\w+)", response.text)
                
                if token:
                    with open("token.json", "w") as f:
                        f.write(token.group(1))
                    with open("cookie.json", "w") as f:
                        f.write(cookie)
                    cetak(nel(f'{P2} LOGIN SUCCEED',width=24,style=f"#00FF00"))
                    time.sleep(2)
                    bot_share()
                else:
                    raise Exception("Token not found")
                    
            except Exception as e:
                os.system("rm token.json cookie.json")
                cetak(nel(f'{P2} COOKIE INVALID',width=22,style=f"#00FF00"))
                time.sleep(1.5)
                login()
    except Exception as e:
        print(f"Error: {str(e)}")
        login()

###----------[ IMPROVED SHARE FUNCTION ]----------###
def share_post(url, token, cookie):
    try:
        headers = {
            "authority": "graph.facebook.com",
            "cache-control": "max-age=0",
            "sec-ch-ua-mobile": "?0",
            "user-agent": random_ua()
        }
        data = {
            "link": url,
            "published": "0",
            "access_token": token
        }
        response = requests.post(
            "https://graph.facebook.com/v13.0/me/feed",
            params=data,
            headers=headers,
            cookies={"cookie": cookie}
        )
        return response.json().get("id") is not None
    except Exception:
        return False

###----------[ IMPROVED BOT SHARE ]----------###
def bot_share():
    try:
        os.system('clear')
        token = open("token.json", "r").read()
        cookie = open("cookie.json", "r").read()
        cookie_dict = {"cookie": cookie}
        
        # Get user information
        ip = requests.get("https://api.ipify.org").text
        user_info = requests.get(
            f"https://graph.facebook.com/me?fields=name,id&access_token={token}",
            cookies=cookie_dict
        ).json()
        nama = user_info.get("name")
        uid = user_info.get("id")
        
        # Post comment
        requests.post(
            f"https://graph.facebook.com/826244541950192/comments/?message={kom1}&access_token={token}",
            headers={"cookie": cookie}
        )
        
        # Display menu
        os.system('clear')
        logo_menu()
        cetak(nel(f'''
{P2} Owner      : {H2}Yuri Evisu 
{P2} User Active     : {H2}{nama} 
{P2} You Id          : {uid}
{P2} You Ip          : {ip}
{P2} Current Date    : {hari}, {tanggal}''',
        title=f'{P2} {H2}[ {P2}User Information {H2}]',
        subtitle_align='left',
        padding=1,
        style='blue'))
        
        # Get share details
        cetak(nel(f'{P2}Hello {H2}{nama}{P2}, copy the post link must be from Facebook Lite otherwise an error will occur when the bot share process runs.',
              title=f'{P2} {H2}[ {P2}Notes {H2}]',
              subtitle_align='left',
              padding=1,
              style='blue'))
        
        cetak(nel(f'{P2} LINK POST',subtitle=f'{P2}┌─',subtitle_align='left',width=25,padding=0,style='blue'))
        link = input(f"{P}   └──> : {H}")
        cetak(nel(f'{P2} AMOUNT OF SHARES',subtitle=f'{P2}┌─',subtitle_align='left',width=22,padding=0,style='blue'))
        jumlah = int(input(f"{P}   └──> : {H}"))
        cetak(nel(f'{P2} AUTO SHARE ONGOING',subtitle=f'{P2}┌─',subtitle_align='left',width=29,padding=0,style='blue'))
        
        # Perform sharing with ThreadPoolExecutor
        start_time = datetime.now()
        success_count = 0
        
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = [executor.submit(share_post, link, token, cookie) for _ in range(jumlah)]
            for i, future in enumerate(futures):
                if future.result():
                    success_count += 1
                    elapsed = str(datetime.now() - start_time).split('.')[0]
                    print(f'{P}\r   └──> {elapsed} Successfully Shared {H}{success_count}{P} Post {N} ', end='')
                    sys.stdout.flush()
                time.sleep(SLEEP_INTERVAL)
        
        print("\n\nSharing completed!")
        
    except Exception as e:
        print(f"\nError: {str(e)}")
        os.system("rm token.json cookie.json")
        cetak(nel(f'{P2} AUTO SHARE STOP POSSIBLE INVALID COOKIES',width=35,padding=0,style='red'))
        exit()

###----------[ MAIN ]----------###
if __name__ == "__main__":
    try:
        os.system('git pull')
    except:
        pass
    try:
        os.mkdir('OK')
    except:
        pass
    try:
        os.mkdir('CP')
    except:
        pass
    bot_share()
