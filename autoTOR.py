import time
import os
import subprocess
import sys


try:
    import requests
except Exception:
    print('[+] python3 requests is not installed')
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests[socks]'])
    import requests
    print('[!] python3 requests is installed')

try:
    subprocess.check_output(['which', 'tor'])
except subprocess.CalledProcessError:
    print('[+] tor is not installed !')
    subprocess.check_output(['sudo', 'apt', 'update'])
    subprocess.check_output(['sudo', 'apt', 'install', 'tor', '-y'])
    print('[!] tor is installed succesfully')

os.system("clear")


def ma_ip():
    url = 'http://checkip.amazonaws.com'
    proxies = {
        'http': 'socks5://127.0.0.1:9050',
        'https': 'socks5://127.0.0.1:9050',
    }
    get_ip = requests.get(url, proxies=proxies, timeout=20)
    return get_ip.text.strip()


def change():
    os.system("service tor reload")
    print('[+] Your IP has been Changed to : ' + str(ma_ip()))


print(r'''\033[1;32;40m \n
                _          _______
     /\        | |        |__   __|
    /  \  _   _| |_ ___      | | ___  _ __
   / /\ \| | | | __/ _ \     | |/ _ \| '__|
  / ____ \ |_| | || (_) |    | | (_) | |
 /_/    \_\__,_|\__\___/     |_|\___/|_|
                V 2.1
from mrFD
''')
print("\033[1;40;31m http://facebook.com/ninja.hackerz.kurdish/\n")

os.system("service tor start")


time.sleep(3)
print("\033[1;32;40m change your  SOCKES to 127.0.0.1:9050 \n")
os.system("service tor start")

interval = 5

print("Starting infinite IP change every " + str(interval) + " seconds. Press Ctrl+C to stop.")

while True:
    try:
        time.sleep(interval)
        change()
    except KeyboardInterrupt:
        print('\nAuto IP changer is closed.')
        break
    except requests.RequestException as exc:
        print("Could not check IP through Tor: " + str(exc))
