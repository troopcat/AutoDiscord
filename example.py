import AutoDiscord

client = AutoDiscord.Client()

while True:
	try:

		client.joinLive()
		
	except AutoDiscord.GuiDoesNotExists:
		print("bulunamadı")
		continue