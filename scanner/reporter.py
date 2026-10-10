import json


def save_report(scan_result):

    with open("scan_report.json", "w") as file:
        json.dump(scan_result, file, indent=4)