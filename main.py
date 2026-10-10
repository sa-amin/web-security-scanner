from scanner.Banner import banner
from colorama import Fore, Style, Back
from scanner.url_checker import url_check
from scanner.headers_checker import check_headers
from scanner.cookie_checker import check_cookies
from urllib.parse import urlparse
import requests

reset = Style.RESET_ALL

while True:
    banner()
    try:
        print(Back.BLUE+Fore.YELLOW+"choose a options : "+reset)
        print(Fore.YELLOW+"[1] Full scan (Also give you a json file)")
        print(Fore.YELLOW+"[2] Headers check")
        print(Fore.YELLOW+"[3] Cookie check")
        print(Fore.YELLOW+"[4] Exit")
        opt = int(input(Fore.BLUE+"「"+Fore.GREEN+"Main"+Fore.BLUE+" 」\n  " +
                        Fore.CYAN+"↳"+Fore.GREEN+">>>"+Fore.RED+"$"+reset))
        if opt == 1:
            url_check()
        elif opt == 2:
            banner()
            print(Fore.GREEN+"enter your url :")
            url = input(Fore.BLUE+"「"+Fore.GREEN+"HC"+Fore.BLUE+" 」\n  " +
                            Fore.CYAN+"↳"+Fore.GREEN+">>>"+Fore.RED+"$"+reset)
            if not url.startswith(("https://", "http://")):
                url = "https://" + url
            parsed_url = urlparse(url)
            if parsed_url.scheme not in ("http", "https") or not parsed_url.netloc:
                print(Fore.RED + "wrong structure")
                continue
            headers = {"User-Agent": "Mozilla/5.0 (WebSecurityScanner/1.0)"}
            response = requests.get(url, timeout=10, headers=headers, verify=True, allow_redirects=True)
            check_headers(response)
        elif opt == 3:
            banner()
            print(Fore.GREEN+"enter your url :")
            url = input(Fore.BLUE+"「"+Fore.GREEN+"CC"+Fore.BLUE+" 」\n  " +
                            Fore.CYAN+"↳"+Fore.GREEN+">>>"+Fore.RED+"$"+reset)
            if not url.startswith(("https://", "http://")):
                url = "https://" + url
            parsed_url = urlparse(url)
            if parsed_url.scheme not in ("http", "https") or not parsed_url.netloc:
                print(Fore.RED + "wrong structure")
                continue
            headers = {"User-Agent": "Mozilla/5.0 (WebSecurityScanner/1.0)"}
            response = requests.get(url, timeout=10, headers=headers, verify=True, allow_redirects=True)
            check_cookies(response)
        elif opt == 4:
            break
        else:
            print(Fore.RED+"wrong option")
    except requests.exceptions.Timeout:
        print(Fore.RED + "[!] Request timed out.")
    except requests.exceptions.ConnectionError:
        print(Fore.RED + "[!] Connection failed.")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[!] Request error: {e}")
    except ValueError:
        print("enter a valid option")
    except Exception as e:
        print(e)
