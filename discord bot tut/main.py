from urllib import response
import discord
import os
import random
import requests
import json
client = discord.Client()


def get_inspireAPI_quote():
    response = requests.get("https://zenquotes.io/api/random")
    jsonData = json.loads(response.text)
    quote = jsonData[0]['q'] + ""


@client.event
async def on_ready():
    # event that happens when the bot is ready and working
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:  # if message author is the bot
        return
    # if the message is a $hello command
    if message.content.startswith('$inspire'):
        await message.channel.send('Hello')

    word = ''
    for char in message.content:
        word += char
    words = word.split()
    for word in words:
        if word == "sigma":
            with open(r"C:\Users\Sam\Documents\Programming\Python GIT REPO\discord bot tut\sigmaMaleQuotes.txt", "r") as quotes:
                lines = quotes.readlines()
                randNum = random.randint(0, len(lines) - 1)
                randomQuote = lines[randNum]
                await message.channel.send("'Sigma' detected: ")
                await message.channel.send(randomQuote)


# this actually runs the bot
# you can just paste the key directly here, instead of using an env file
client.run(os.environ['TOKEN'])
