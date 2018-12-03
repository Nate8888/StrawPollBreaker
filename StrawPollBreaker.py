#!/usr/bin/env python
#
#                                                                    ,,    ,,
#   .M"""bgd mm                                  `7MM"""Mq.        `7MM  `7MM  `7MM"""Yp,                           `7MM
#  ,MI    "Y MM                                    MM   `MM.         MM    MM    MM    Yb                             MM
#  `MMb.   mmMMmm `7Mb,od8 ,6"Yb.`7M'    ,A    `MF'MM   ,M9 ,pW"Wq.  MM    MM    MM    dP `7Mb,od8 .gP"Ya   ,6"Yb.    MM  ,MP'.gP"Ya `7Mb,od8
#    `YMMNq. MM     MM' "'8)   MM  VA   ,VAA   ,V  MMmmdM9 6W'   `Wb MM    MM    MM"""bg.   MM' "',M'   Yb 8)   MM    MM ;Y  ,M'   Yb  MM' "'
#  .     `MM MM     MM     ,pm9MM   VA ,V  VA ,V   MM      8M     M8 MM    MM    MM    `Y   MM    8M""""""  ,pm9MM    MM;Mm  8M""""""  MM
#  Mb     dM MM     MM    8M   MM    VVV    VVV    MM      YA.   ,A9 MM    MM    MM    ,9   MM    YM.    , 8M   MM    MM `Mb.YM.    ,  MM
#  P"Ybmmd"  `Mbmo.JMML.  `Moo9^Yo.   W      W   .JMML.     `Ybmd9'.JMML..JMML..JMMmmmd9  .JMML.   `Mbmmd' `Moo9^Yo..JMML. YA.`Mbmmd'.JMML.
#
#  https://github.com/Adamkadaban
#
#  Verson 1.2 alpha 12/3/2018

import os, signal

try:
    import requests
    import argparse
except ImportError as msg:
    print("[!] Library not installed: " + str(msg))
    os.system('python -m pip install requests')
    os.system('python -m pip install argparse')
    exit()

parser = argparse.ArgumentParser()


parser.add_argument("-v", "--verbose", help="print all output", action='store_true')
parser.add_argument("-t", "--target", type=str, help="target link")
parser.add_argument("-o", "--option", type=str, help="checkbox option id")

args = parser.parse_args()

fp = open('proxies.txt', 'r')
line = fp.readline()
while line:
    proxy = "http://"+line.strip()
    print(proxy)
    url = args.target
    payload = "options="+args.option
    proxyDictionary = {"https": proxy}
    print(proxyDictionary)
    headers = {
        'accept': "/",
        'origin': "https://www.strawpoll.me",
        'x-requested-with': "XMLHttpRequest",
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        'content-type': "application/x-www-form-urlencoded",
        'referer': "https://www.strawpoll.me/16965947",
        'Cookie': 'lang=en',
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
        'cache-control': "no-cache"
    }
    try:
        response = requests.request("POST", url, data=payload, proxies=proxyDictionary, headers=headers)
    except:
        pass

    if args.verbose:
        print(response.text)
    line = fp.readline()



print("Done")