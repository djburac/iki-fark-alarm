import time
import requests

BOT_TOKEN = "BOT_TOKEN_BURAYA"
CHAT_ID = "CHAT_ID_BURAYA"
API_KEY = "API_KEY_BURAYA"

URL = "https://v3.football.api-sports.io/fixtures?live=all"

HEADERS = {
    "x-apisports-key": API_KEY
}

gonderilen = set()

def telegram(mesaj):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": mesaj
        }
    )

while True:

    try:

        cevap = requests.get(URL, headers=HEADERS).json()

        for mac in cevap["response"]:

            home = mac["teams"]["home"]["name"]
            away = mac["teams"]["away"]["name"]

            hs = mac["goals"]["home"]
            aw = mac["goals"]["away"]

            fark = abs(hs-aw)

            id = str(mac["fixture"]["id"])

            if fark == 2:

                if id+"2" not in gonderilen:

                    telegram(
                        f"🔔 2 FARK\n\n{home} - {away}\n{hs}-{aw}"
                    )

                    gonderilen.add(id+"2")

            if fark == 3:

                if id+"3" not in gonderilen:

                    telegram(
                        f"🔔 3 FARK\n\n{home} - {away}\n{hs}-{aw}"
                    )

                    gonderilen.add(id+"3")

        time.sleep(15)

    except Exception as e:

        print(e)

        time.sleep(30)
