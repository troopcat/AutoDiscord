import AutoDiscord

client = AutoDiscord.Client()

client.foreGroundDiscord()

while True:
    try:
        client.send("@everyone")
        
        if client.getLocation("chill.PNG"):
        	client.chill()

    except AutoDiscord.GuiDoesNotExists:
        break
