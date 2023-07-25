# ------- Import Library's
import os, sys

try:
    import requests
except:
    os.system('pip3 install requests')
import requests
import threading
from threading import active_count
import urllib

n_threads = 400
threads = []
print('\033[1;32m••••••••••••••\033[1;33developer  \033[1;32m••••••••\033[1;33mTele: @nnnb50')
print()
link1 = "https://t.me/V_T_4/6"


#################
def view2(proxy):
    links = [link1]
    for i in links:
        channel = i.split('/')[3]
        msgid = i.split('/')[4]
        send_seen(channel, msgid, proxy)


###############
def send_seen(channel, msgid, proxy):
    s = requests.Session()
    proxies = {
        'http': proxy,
        'https': proxy,
    }
    try:
        a = s.get("https://t.me/" + channel + "/" + msgid,
                  timeout=10, proxies=proxies)
        cookie = a.headers['set-cookie'].split(';')[0]
    except Exception as e:
        return False
    h1 = {"Accept": "*/*", "Accept-Encoding": "gzip, deflate, br",
          "Accept-Language": "en-US,en;q=0.9,fa;q=0.8,de;q=0.7", "Connection": "keep-alive", "Content-Length": "5",
          "Content-type": "application/x-www-form-urlencoded",
          "Cookie": cookie, "Host": "t.me", "Origin": "https://t.me",
          "Referer": "https://t.me/" + channel + "/" + msgid + "?embed=1", "Sec-Fetch-Dest": "empty",
          "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "User-Agent": "Chrome"}
    d1 = {"_rl": "1"}
    try:
        r = s.post('https://t.me/' + channel + '/' + msgid + '?embed=1',
                   json=d1, headers=h1, proxies=proxies)
        key = r.text.split('data-view="')[1].split('"')[0]
        now_view = r.text.split('<span class="tgme_widget_message_views">')[1].split('</span>')[0]
        if now_view.find("K") != -1:
            now_view = now_view.replace("K", "00").replace(".", "")
    except Exception as e:
        return False
    h2 = {"Accept": "*/*", "Accept-Encoding": "gzip, deflate, br",
          "Accept-Language": "en-US,en;q=0.9,fa;q=0.8,de;q=0.7", "Connection": "keep-alive", "Cookie": cookie,
          "Host": "t.me",
          "Referer": "https://t.me/" + channel + "/" + msgid + "?embed=1", "Sec-Fetch-Dest": "empty",
          "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "User-Agent": "Chrome",
          "X-Requested-With": "XMLHttpRequest"}
    try:
        i = s.get('https://t.me/v/?views=' + key, timeout=10,
                  headers=h2, proxies=proxies)
        if (i.text == "true"):
            print('\033[1;32mDone Add View ✅:\033[1;33m' + now_view)
    except Exception as e:
        return False
    try:
        h3 = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9,fa;q=0.8,de;q=0.7",
            "Cache-Control": "max-age=0", "Connection": "keep-alive", "Cookie": cookie, "Host": "t.me",
            "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1", "Upgrade-Insecure-Requests": "1", "User-Agent": "Chrome"}
        s.get("https://t.me/" + channel + "/" + msgid, headers=h3,
              timeout=10, proxies=proxies)
    except Exception as e:
        return False


with open("auto/http.txt", 'r') as file:
    f = open("proxies.txt", "w")
    for line in file:
        uss = line.strip()
        https = requests.get(f"{uss}",
                             proxies=urllib.request.getproxies(), timeout=5).text
        f.write(https)
    f.close()
file.close()
with open("auto/socks4.txt", 'r') as fi:
    f = open("socks.txt", "w")
    for line in fi:
        uss = line.strip()
        print(uss)
        ss = requests.get(f"{uss}",
                             proxies=urllib.request.getproxies(), timeout=5).text
        f.write(ss)
    f.close()
fi.close()




def checker(proxy):
    proxies = {
        'http': proxy,
        'https': proxy,
    }
    try:
        view2(proxy)
    except Exception as e:
        return False


def start():
    list = open('proxies.txt', 'r')
    proxies = list.readlines()
    list.close()
    for i in proxies:
        if i =='\n':
            break
        while active_count() > n_threads:
            liiii = 9
        thread = threading.Thread(target=checker, args=(i,))
        threads.append(thread)
        thread.start()

    list = open('socks.txt', 'r')
    proxies = list.readlines()
    list.close()
    for i in proxies:
        p = i.split('\n')[0]
        if not p:
            continue
        while active_count() > n_threads:
            lii7ii = 99
        pr = "socks5://" + p
        thread = threading.Thread(target=checker, args=(pr,))
        threads.append(thread)
        thread.start()

    return True


def process(run_for_ever: bool = False):
    try:
        if run_for_ever:
            while True:
                start()
        else:
            start()
    except Exception:
        pass


process(True)