import requests
import time

token = "ODI0OTkzNTk5Mjg3OTg0MTkw.YI_jrA.ds3LZhNrpDIUncKS0Oy80AFikzA"  # token
channelId = "828950450203525150"  # channel id

while True:
    requests.post("https://discord.com/api/v8/channels/" +
                  channelId + "/messages", json={"content": "!d bump"},
                  headers={"Authorization": token})
    time.sleep(7210)