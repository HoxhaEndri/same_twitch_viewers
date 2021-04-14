import json
import requests
import sys

def totalviewers(data):
    names = data['chatters']['vips'] + data['chatters']['moderators'] + data['chatters']['viewers']
    names.sort()
    return names

if len(sys.argv) >= 3:
    url = "https://tmi.twitch.tv/group/user/"+sys.argv[1]+"/chatters"
    url_volpe = requests.get(url)
    url = "https://tmi.twitch.tv/group/user/"+sys.argv[2]+"/chatters"
    url_moccia = requests.get(url)
else:
    url_volpe  = requests.get("https://tmi.twitch.tv/group/user/volpescu/chatters")
    url_moccia = requests.get("https://tmi.twitch.tv/group/user/dariomocciatwitch/chatters")

x = url_volpe.json()

lista_volpe = totalviewers(x)

y = url_moccia.json()

lista_moccia = totalviewers(y)

bastardi = []

for element in lista_volpe:
    for e in lista_moccia:
        if element == e:
            bastardi.append(element)
            break

print(bastardi)

