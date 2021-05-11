import AutoDiscord
from time import sleep

client = AutoDiscord.Client()

client.foreGroundDiscord()

while True:
    try:
        client.send("@everyone")
        
        if client.getLocation("chill.PNG"):
        	client.chill()
        	sleep(5)

    except AutoDiscord.GuiDoesNotExists:
        break
