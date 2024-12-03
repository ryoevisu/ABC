#---#---#------[AUTHOR Yuri Evisu]------#---#---#
###----------[ IMPORT LIBRARY ]---------- ###
import requests, os, re, bs4, calendar, sys, json, time, random, datetime, subprocess, logging, base64, uuid
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
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
ses=requests.Session()

###----------[ CALENDAR ]----------###
bulan = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
tgl = datetime.now().day
bln = bulan[(str(datetime.now().month))]
thn = datetime.now().year
tanggal = (str(tgl)+' '+str(bln)+' '+str(thn))
waktu = strftime('%H:%M:%S')
hari = datetime.now().strftime("%A")

###----------[ COLORS ]---------- ###
Z = "\x1b[0;90m"     # Black
M = "\x1b[38;5;196m" # Red
H = "\x1b[38;5;46m"  # Green
K = "\x1b[38;5;226m" # Yellow 
B = "\x1b[38;5;44m"  # Blue
U = "\x1b[0;95m"     # Purple
O = "\x1b[0;96m"     # Cyan
P = "\x1b[38;5;231m" # White
J = "\x1b[38;5;208m" # Orange
A = "\x1b[38;5;248m" # Gray
N = '\x1b[0m'        # Default
PT = '\x1b[1;97m'    # Bold White
MT = '\x1b[1;91m'    # Bold Red
HT = '\x1b[1;92m'    # Bold Green
KT = '\x1b[1;93m'    # Bold Yellow
BT = '\x1b[1;94m'    # Bold Blue
UT = '\x1b[1;95m'    # Bold Purple
OT = '\x1b[1;96m'    # Bold Cyan

###----------[ RICH COLORS ]---------- ###
Z2 = "[#000000]" # BLACK
M2 = "[#FF0000]" # RED
H2 = "[#00FF00]" # GREEN
K2 = "[#FFFF00]" # YELLOW
B2 = "[#00C8FF]" # BLUE
U2 = "[#AF00FF]" # PURPLE
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # CYAN
P2 = "[#FFFFFF]" # WHITE
J2 = "[#FF8F00]" # ORANGE
A2 = "[#AAAAAA]" # GRAY

###----------[ USER AGENTS ]---------- ###
ua_default = 'Mozilla/5.0 (Linux; Android 3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.66 Mobile Safari/537.36'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_iphone  = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_lenovo  = 'Mozilla/5.0 (Linux; U; Android 5.0.1; ru-RU; Lenovo A788t Build/LRX22C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.0.950 U3/0.8.0 Mobile Safari/E7FBAF'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_chrome  = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36'
ua_fb      = 'Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]'
ua_random = random.choice([ua_default,ua_samsung,ua_nokia,ua_xiaomi,ua_oppo,ua_vivo,ua_iphone,ua_asus,ua_lenovo,ua_huawei,ua_windows,ua_chrome,ua_fb])

###----------[ LOGO & MENU ]----------###
def logo_menu():
    os.system('clear')
    cetak(nel(f'''
{P2}╔══════════════════════════════════════════════════════╗
{P2}║                  {H2}FACEBOOK SHARE BOT{P2}                    ║
{P2}║                    {M2}VERSION 0.1{P2}                         ║
{P2}╚══════════════════════════════════════════════════════╝

{H2}██████╗  ██████╗ ████████╗    ███████╗██╗  ██╗ █████╗ ██████╗ ███████╗
{H2}██╔══██╗██╔═══██╗╚══██╔══╝    ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝
{H2}██████╔╝██║   ██║   ██║       ███████╗███████║███████║██████╔╝█████╗  
{H2}██╔══██╗██║   ██║   ██║       ╚════██║██╔══██║██╔══██║██╔══██╗██╔══╝  
{H2}██████╔╝╚██████╔╝   ██║       ███████║██║  ██║██║  ██║██║  ██║███████╗
{H2}╚═════╝  ╚═════╝    ╚═╝       ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
''', title=f'{P2} {H2}[ {P2}SHARE BOT MENU {H2}]', subtitle=f'{P2}┌─[ {H2}Created By Yuri Evisu {P2}]',subtitle_align='left', padding=1, style='blue'))

###----------[ LOADING ANIMATION ]----------###
def loading():
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold blue]{task.description}"),
        BarColumn(),
        TimeElapsedColumn(),
    ) as progress:
        task = progress.add_task("[cyan]Loading...", total=100)
        while not progress.finished:
            progress.update(task, advance=0.9)
            time.sleep(0.05)

###----------[ IMPROVED LOGIN ]----------###
def login():
    os.system("clear")
    cetak(nel(f'   {P2}Login Using Facebook Cookies \n\n              {H2}--[ AUTHORIZATION ]--',title=f'{P2} {H2}[ {P2}Welcome {H2}]',width=54,padding=(1,4),style='blue'))
    cetak(nel(f'{P2} Get Cookies From Kiwi Browser Extension',subtitle=f'{P2}┌─[ Cookies Input ]',subtitle_align='left',width=54,padding=1,style='blue'))
    cookie = input(f"{P}   └──> : {H}")
    loading()
    try:
        data = ses.get("https://business.facebook.com/business_locations", headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",
            "referer": "https://www.facebook.com/",
            "host": "business.facebook.com",
            "origin": "https://business.facebook.com",
            "upgrade-insecure-requests" : "1",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type":"text/html; charset=utf-8"
        }, cookies = {"cookie":cookie})
        find_token = re.search("(EAAG\w+)", data.text)
        open("token.json", "w").write(find_token.group(1))
        open("cookie.json", "w").write(cookie)
        cetak(nel(f'{P2} LOGIN SUCCESSFUL',width=24,style=f"#00FF00"))
        time.sleep(2)
        bot_share()
    except:
        os.system("rm token.json cookie.json")
        cetak(nel(f'{P2} INVALID COOKIE',width=22,style=f"#00FF00"))
        time.sleep(1.5) 
        login()

###----------[ IMPROVED SHARE BOT ]----------###
def bot_share():
    try:
        token = open("token.json","r").read()
        cok = open("cookie.json","r").read()
        cookie = {"cookie":cok}
        ip = requests.get("https://api.ipify.org").text
        
        # Get user information
        user_info = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}",cookies=cookie).json()
        nama = user_info["name"]
        id = user_info["id"]

    except:
        os.system("rm token.json cookie.json")
        cetak(nel(f'{P2} COOKIE INVALID!!',width=22,style=f"#00FF00"))
        time.sleep(1.5)
        login()
        
    logo_menu()
    cetak(nel(f'''
{P2} Owner          : {H2}Yuri Evisu 
{P2} Active User    : {H2}{nama} 
{P2} User ID        : {id}
{P2} IP Address     : {ip}
{P2} Current Date   : {hari}, {tanggal}
{P2} Current Time   : {waktu}''',
    title=f'{P2} {H2}[ {P2}User Information {H2}]',
    subtitle_align='left',padding=1,style='blue'))

    cetak(nel(f'{P2}Welcome {H2}{nama}{P2}, Please paste a Facebook Lite post link for optimal sharing.',
    title=f'{P2} {H2}[ {P2}Instructions {H2}]',
    subtitle_align='left',padding=1,style='blue'))

    # Get share details
    cetak(nel(f'{P2} POST LINK',subtitle=f'{P2}┌─',subtitle_align='left',width=25,padding=0,style='blue'))
    link = input(f"{P}   └──> : {H}")
    cetak(nel(f'{P2} NUMBER OF SHARES',subtitle=f'{P2}┌─',subtitle_align='left',width=22,padding=0,style='blue'))
    jumlah = int(input(f"{P}   └──> : {H}"))
    
    # Initialize progress tracking
    cetak(nel(f'{P2} SHARE PROGRESS',subtitle=f'{P2}┌─',subtitle_align='left',width=29,padding=0,style='blue'))
    start_time = datetime.now()
    
    try:
        n = 0
        header = {
            "authority": "graph.facebook.com",
            "cache-control": "max-age=0",
            "sec-ch-ua-mobile": "?0",
            "user-agent": ua_random
        }
        
        with Progress() as progress:
            task = progress.add_task("[cyan]Sharing...", total=jumlah)
            
            for x in range(jumlah):
                n += 1
                post = ses.post(f"https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={token}",
                              headers=header, cookies=cookie).text
                data = json.loads(post)
                if "id" in post:
                    progress.update(task, advance=1)
                    elapsed = str(datetime.now()-start_time).split('.')[0]
                    print(f'{P}\r   └──> {elapsed} Successfully Shared {H}{n}{P} Posts {N} ',end='')
                    sys.stdout.flush()
                else:
                    print("\n")
                    cetak(nel(f'{P2} SHARING STOPPED - POSSIBLE COOKIE ISSUE',width=35,padding=0,style='red'))
                    exit()
                    
    except requests.exceptions.ConnectionError:
        print(f"\n{P}(!) No Internet Connection!")
        exit()

    # Show completion message
    cetak(nel(f'{P2} SHARING COMPLETED SUCCESSFULLY\n{H2}Total Shares: {n}\nTime Elapsed: {elapsed}',
    title=f'{P2} {H2}[ {P2}Complete {H2}]',
    subtitle_align='left',padding=1,style='green'))

if __name__ == "__main__":
    try:
        bot_share()
    except Exception as e:
        cetak(nel(f'{P2} ERROR: {str(e)}',width=35,padding=0,style='red'))
