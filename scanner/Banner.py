from colorama import Fore, Style
import os
import subprocess
import time
import shutil


def reset():
    print(Style.RESET_ALL)


def run_neofetch():
    """اجرای neofetch فقط اگه نصب باشه"""
    if shutil.which("neofetch"):      # بررسی وجود دستور در PATH
        subprocess.run("neofetch", shell=True)
    else:
        print(Fore.RED + "[!] neofetch not found. Skipping...")


def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    run_neofetch()
    time.sleep(1)
    lines = [
        Fore.GREEN + r""" █     █░▓█████  ▄▄▄▄     ██████ ▓█████  ▄████▄  """,
        r"""▓█░ █ ░█░▓█   ▀ ▓█████▄ ▒██    ▒ ▓█   ▀ ▒██▀ ▀█  """,
        r"""▒█░ █ ░█ ▒███   ▒██▒ ▄██░ ▓██▄   ▒███   ▒▓█    ▄ """,
        r"""░█░ █ ░█ ▒▓█  ▄ ▒██░█▀    ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒""",
        r"""░░██▒██▓ ░▒████▒░▓█  ▀█▓▒██████▒▒░▒████▒▒ ▓███▀ ░""",
        r"""░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░""",
        r"""  ▒ ░ ░   ░ ░  ░▒░▒   ░ ░ ░▒  ░ ░ ░ ░  ░  ░  ▒   """,
        r"""  ░   ░     ░    ░    ░ ░  ░  ░     ░   ░        """,
        r"""    ░       ░  ░ ░            ░     ░  ░░ ░      """,
        r"""                      ░                 ░         """
    ]

    for line in lines:
        print(line)
        time.sleep(0.1)
    print(Fore.YELLOW+"""
────────────────────────────────────────
    WEB SECURITY SCANNER
Version 1.0
────────────────────────────────────────

Lightweight Security Toolkit""")
    reset()
