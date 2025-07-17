import requests

def scan_ports_for_flg():
    for port in range(0, 10000):
        try:
            url = f"http://127.0.0.1:{port}/admin"
            response = requests.get(url, timeout=0.1)
            if "FLG" in response.text:
                print(f"[+] Found flag on port {port}!")
                print(response.text)
                return
        except requests.RequestException:
            continue
    print("[-] No FLG found.")

if __name__ == "__main__":
    scan_ports_for_flg()
