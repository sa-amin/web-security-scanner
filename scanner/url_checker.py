import requests
from colorama import Fore, Style
from scanner.headers_checker import check_headers
from scanner.cookie_checker import check_cookies
from scanner.Banner import banner
from urllib.parse import urlparse
from scanner.reporter import save_report
import time
reset = Style.RESET_ALL


def url_check():
    banner()
    print(Fore.YELLOW+"Please Enter Your Url :")
    url = input(Fore.BLUE+"「"+Fore.GREEN+"UC"+Fore.BLUE+" 」\n  " +
                Fore.CYAN+"↳"+Fore.GREEN+">>>"+Fore.RED+"$"+reset)
    try:
        if not url.startswith(("https://", "http://")):
            url = "https://" + url
        parsed_url = urlparse(url)
        if parsed_url.scheme not in ("http", "https") or not parsed_url.netloc:
            print(Fore.RED + "wrong structure")
            return
        headers = {"User-Agent": "Mozilla/5.0 (WebSecurityScanner/1.0)"}
        response = requests.get(url, timeout=10, headers=headers, verify=True, allow_redirects=True)
        print(Fore.CYAN+f"the status of {response.url} is : ")
        print(f"status code : {response.status_code}")
        response_time = response.elapsed.total_seconds()
        print(f"Response Time : {response_time}")
        print(f"Protocol Type : {urlparse(response.url).scheme}")
        server = response.headers.get("Server")
        print(f"server : {server}")
        redirects = []
        if response.history:
            print(Fore.RED+"[!] Redirect Detected")
            print(f"Redirect Number : {len(response.history)}")
            for number, redirect_response in enumerate(response.history, start=1):
                print(f"[{number}] Status :{redirect_response.status_code}")
                print(f"    URL : {redirect_response.url}")
            print(reset)

            for redirect_response in response.history:
                redirects.append({
                    "status_code": redirect_response.status_code,
                    "url": redirect_response.url
                })
        print("----------------------------")
        print("important headers :")
        header_findings = check_headers(response ,pause_at_end=False)
        # print(header_findings)
        print(reset)
        print("cookies :")
        cookie_findings = check_cookies(response ,pause_at_end=False)
        print("----------------------------")
        print(Fore.YELLOW+"report saved.")
        # print(cookie_findings)
        all_findings = header_findings + cookie_findings
        scan_result = {
            "target": response.url,
            "status_code": response.status_code,
            "response_time": response_time,
            "protocol": urlparse(response.url).scheme,
            "server": server,
            "redirects": redirects,
            "findings": all_findings
        }
        save_report(scan_result)
        # print(response.text[:250])
    except requests.exceptions.Timeout:
        print(Fore.RED + "[!] Request timed out.")
    except requests.exceptions.ConnectionError:
        print(Fore.RED + "[!] Connection failed.")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[!] Request error: {e}")
    finally :
        input(Fore.YELLOW + "\nPress Enter to return to Main..." + reset)


