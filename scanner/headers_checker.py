import time
from colorama import Fore, Style
reset = Style.RESET_ALL


def check_headers(response, pause_at_end=True):
    print(reset)
    findings = []
    check_header = response.headers
    security_headers = {
        "Content-Security-Policy": {
            "description": "Helps reduce XSS and content injection risks",
            "severity": "Medium"
        },

        "X-Content-Type-Options": {
            "description": "Prevents MIME type sniffing",
            "severity": "Low"
        },

        "X-Frame-Options": {
            "description": "Helps prevent clickjacking",
            "severity": "Medium"
        },

        "Strict-Transport-Security": {
            "description": "Helps enforce HTTPS connections",
            "severity": "Medium"
        }
    }
    for sh, info in security_headers.items():
        if sh in check_header:
            print(Fore.GREEN+f"[+]{sh} :\n {info['description']}")
        else:
            print(
                Fore.RED + f"[{info['severity'].upper()}] Missing {sh}\n {info['description']}")
            findings.append({
                "type": "missing_header",
                "name": sh,
                "severity": info["severity"],
                "description": info["description"]
            })
    print(reset)
    if pause_at_end:
        input(Fore.YELLOW + "\nPress Enter to return to Main..." + reset)
    return findings
