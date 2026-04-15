import requests
from  bs4 import BeautifulSoup
import os
from datetime import datetime
import discord

#your need to make a file for this to work properly

TOKEN = #insert token
USER_ID =  #insert user id


date = datetime.today().strftime("%Y-%m-%d")
with open("freegame","r+") as file:
    content = file.read()
    if date not in content:
        x = requests.get("https://store.steampowered.com/search/?maxprice=free&supportedlang=english&specials=1&ndl=1")
        soup = BeautifulSoup(x.content, 'html.parser')
        divy = soup.find_all("span" , {"class": "title"})
        cleantext = BeautifulSoup(str(divy),"lxml").text
        if cleantext not in content:
            
            file.seek(0)
            file.write(date+"\n")
            file.write(cleantext)
            file.truncate()
            print("zmiana")
            intents = discord.Intents.default()
            client = discord.Client(intents=intents)
            @client.event
            async def on_ready():
                user = await client.fetch_user(USER_ID)
                await user.send(cleantext)
                await client.close()
            client.run(TOKEN)
