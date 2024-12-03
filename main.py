#---#---#------[AUTHOR Yuri Evisu]------#---#---#
###----------[ IMPORT LIBRARY ]---------- ###
import requests, os, re, bs4, calendar, sys, json, time, random, datetime, subprocess, logging, base64, uuid
import inquirer
from inquirer import themes
from datetime import datetime
from time import sleep
from time import sleep as jeda
from time import strftime
from random import choice
from pathlib import Path
from rich.console import Console
from rich.markdown import Markdown
from rich.columns import Columns
from rich.text import Text
from rich.panel import Panel
from rich import print as cetak
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
from rich.tree import Tree
from rich.table import Table
from rich.live import Live
from rich.prompt import Prompt
from rich.syntax import Syntax
from rich.layout import Layout
from pyfiglet import figlet_format
from termcolor import colored
from tabulate import tabulate
from alive_progress import alive_bar

# Initialize Console
console = Console()
ses = requests.Session()

###----------[ CALENDAR ]----------###
bulan = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
tgl = datetime.now().day
bln = bulan[(str(datetime.now().month))]
thn = datetime.now().year
tanggal = (str(tgl)+' '+str(bln)+' '+str(thn))
waktu = strftime('%H:%M:%S')
hari = datetime.now().strftime("%A")

# [Previous color definitions remain the same...]

###----------[ IMPROVED BANNER ]----------###
def create_banner():
    banner_text = figlet_format("BOT SHARE", font="slant")
    return colored(banner_text, "cyan")

###----------[ SPINNER ANIMATION ]----------###
def show_spinner(message):
    with Progress(
        SpinnerColumn(spinner_name="dots12"),
        TextColumn("[bold blue]{task.description}"),
        TimeElapsedColumn(),
    ) as progress:
        task = progress.add_task(message, total=None)
        time.sleep(2)

###----------[ IMPROVED MENU LAYOUT ]----------###
def create_menu_layout():
    layout = Layout()
    layout.split_column(
        Layout(name="header"),
        Layout(name="body"),
        Layout(name="footer")
    )
    return layout

###----------[ STATISTICS TABLE ]----------###
def create_stats_table(name, user_id, ip, shares_count=0):
    table = Table(show_header=True, header_style="bold magenta", border_style="blue")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")
    
    table.add_row("Username", name)
    table.add_row("User ID", user_id)
    table.add_row("IP Address", ip)
    table.add_row("Total Shares", str(shares_count))
    table.add_row("Date", tanggal)
    table.add_row("Time", waktu)
    
    return table

###----------[ IMPROVED LOGIN UI ]----------###
def login():
    os.system("clear")
    console.print(create_banner())
    
    console.print(Panel.fit(
        "[bold cyan]Welcome to Facebook Share Bot[/bold cyan]\n"
        "[yellow]Please login using your Facebook cookies[/yellow]",
        border_style="green"
    ))
    
    show_spinner("Preparing login interface...")
    
    questions = [
        inquirer.Text('cookie',
                     message="Please enter your Facebook cookie",
                     validate=lambda _, x: len(x) > 0
        ),
    ]
    
    answers = inquirer.prompt(questions, theme=themes.GreenPassion())
    
    if not answers:
        console.print("[red]Login cancelled[/red]")
        return
        
    cookie = answers['cookie']
    
    with console.status("[bold blue]Validating credentials...") as status:
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
            if find_token:
                open("token.json", "w").write(find_token.group(1))
                open("cookie.json", "w").write(cookie)
                console.print("[green]Login successful![/green]")
                time.sleep(2)
                return True
            else:
                raise Exception("Token not found")
                
        except Exception as e:
            console.print(f"[red]Login failed: {str(e)}[/red]")
            if os.path.exists("token.json"): os.remove("token.json")
            if os.path.exists("cookie.json"): os.remove("cookie.json")
            time.sleep(2)
            return False

###----------[ IMPROVED SHARE BOT ]----------###
def bot_share():
    try:
        token = open("token.json","r").read()
        cok = open("cookie.json","r").read()
        cookie = {"cookie":cok}
        ip = requests.get("https://api.ipify.org").text
        
        user_info = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}",cookies=cookie).json()
        nama = user_info["name"]
        user_id = user_info["id"]

    except Exception as e:
        console.print("[red]Session expired. Please login again.[/red]")
        os.system("rm token.json cookie.json")
        time.sleep(1.5)
        login()
        return

    os.system("clear")
    console.print(create_banner())
    
    # Show user stats
    console.print(create_stats_table(nama, user_id, ip))
    
    # Get share details using inquirer
    questions = [
        inquirer.Text('link',
                     message="Enter the Facebook post link",
                     validate=lambda _, x: len(x) > 0
        ),
        inquirer.Text('shares',
                     message="Enter number of shares",
                     validate=lambda _, x: x.isdigit() and int(x) > 0
        ),
    ]
    
    answers = inquirer.prompt(questions, theme=themes.GreenPassion())
    
    if not answers:
        console.print("[red]Operation cancelled[/red]")
        return
        
    link = answers['link']
    jumlah = int(answers['shares'])
    
    # Initialize progress tracking
    start_time = datetime.now()
    success_count = 0
    
    with alive_bar(jumlah, title='Sharing Progress', bar='classic2', spinner='classic') as bar:
        try:
            for x in range(jumlah):
                header = {"authority": "graph.facebook.com",
                         "cache-control": "max-age=0",
                         "sec-ch-ua-mobile": "?0",
                         "user-agent": ua_random}
                
                post = ses.post(f"https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={token}",
                              headers=header, cookies=cookie).text
                
                if "id" in post:
                    success_count += 1
                    elapsed = str(datetime.now()-start_time).split('.')[0]
                    console.print(f"[green]✓ Share {success_count}/{jumlah} successful[/green]")
                else:
                    console.print("[red]× Share failed[/red]")
                
                bar()
                time.sleep(0.5)  # Prevent rate limiting
                
        except KeyboardInterrupt:
            console.print("\n[yellow]Operation cancelled by user[/yellow]")
            return
        except Exception as e:
            console.print(f"\n[red]Error occurred: {str(e)}[/red]")
            return
    
    # Show final statistics
    elapsed_time = str(datetime.now()-start_time).split('.')[0]
    final_stats = Table(show_header=True, header_style="bold magenta")
    final_stats.add_column("Metric", style="cyan")
    final_stats.add_column("Value", style="green")
    
    final_stats.add_row("Total Attempts", str(jumlah))
    final_stats.add_row("Successful Shares", str(success_count))
    final_stats.add_row("Failed Shares", str(jumlah - success_count))
    final_stats.add_row("Success Rate", f"{(success_count/jumlah)*100:.2f}%")
    final_stats.add_row("Total Time", elapsed_time)
    
    console.print("\n[bold cyan]Share Operation Complete![/bold cyan]")
    console.print(final_stats)

if __name__ == "__main__":
    try:
        if not os.path.exists("token.json") or not os.path.exists("cookie.json"):
            if login():
                bot_share()
        else:
            bot_share()
    except Exception as e:
        console.print(f"[red]Fatal Error: {str(e)}[/red]")
