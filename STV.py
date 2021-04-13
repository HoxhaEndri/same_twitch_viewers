import json
import requests
import sys

if len(sys.argv) == 3:
    url = "https://tmi.twitch.tv/group/user/"+sys.argv[1]+"/chatters"
    url_volpe = requests.get(url)
    url = "https://tmi.twitch.tv/group/user/"+sys.argv[2]+"/chatters"
    url_moccia = requests.get(url)
else:
    url_volpe  = requests.get("https://tmi.twitch.tv/group/user/volpescu/chatters")
    url_moccia = requests.get("https://tmi.twitch.tv/group/user/dariomocciatwitch/chatters")

x = url_volpe.json()
vip_volpe = x['chatters']['vips']
mod_volpe = x['chatters']['moderators']
viewers_volpe = x['chatters']['viewers']

lista_volpe = vip_volpe + mod_volpe + viewers_volpe
lista_volpe.sort()

y = url_moccia.json()
vip_moccia = y['chatters']['vips']
mod_moccia = y['chatters']['moderators']
viewers_moccia = y['chatters']['viewers']

lista_moccia = vip_moccia + mod_moccia + viewers_moccia
lista_moccia.sort()

bastardi = []

for element in lista_volpe:
    for e in lista_moccia:
        if element == e:
            bastardi.append(element)
            break

print(bastardi)

