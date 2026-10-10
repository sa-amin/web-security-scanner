from colorama import Fore , Style
reset = Style.RESET_ALL
import time

def check_cookies(response , pause_at_end=True):
    cookie = response.cookies
    findings = []
    cookie_checks = {
        "Secure": "Cookie is sent only over HTTPS",
        "HttpOnly": "Helps prevent JavaScript access to the cookie",
        "SameSite": "Helps control cross-site cookie sending"
    }
    for i in cookie:
        if i.secure:
            print(Fore.GREEN +
                  f"[+] {i.name} secure\n {cookie_checks['Secure']}")
        else:
            print(Fore.RED+f"[-] {i.name} secure\n {cookie_checks['Secure']}")
            findings.append({
                "type": "cookie_security",
                "name": i.name,
                "issue": "Missing Secure flag",
                "description": cookie_checks["Secure"]
            })
        if i._rest.get("HttpOnly"):
            print(Fore.GREEN +
                  f"[+] {i.name} HttpOnly\n {cookie_checks['HttpOnly']}")
        else:
            print(
                Fore.RED+f"[-] {i.name} no HttpOnly\n {cookie_checks['HttpOnly']}")
            findings.append({
                "type": "cookie_security",
                "name": i.name,
                "issue": "Missing HttpOnly flag",
                "description": cookie_checks["HttpOnly"]
            })
        same_site = i._rest.get("SameSite")
        if same_site is None:
            print(Fore.RED + f"[-] {i.name} SameSite is missing")
            findings.append({
                "type": "cookie_security",
                "name": i.name,
                "issue": "Missing SameSite attribute",
                "description": cookie_checks["SameSite"]
            })
        else:
            print(Fore.GREEN + f"[+] {i.name} SameSite: {same_site}")
        print("----------\n")
    print(reset)
    if pause_at_end:
        input(Fore.YELLOW + "\nPress Enter to return to Main..." + reset)
    return findings