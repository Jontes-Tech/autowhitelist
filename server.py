### Imports
import configparser
import discord
from mctools import RCONClient  # Import the RCONClient

### Read from Config File
parser = configparser.ConfigParser()
parser.read("config.txt")
HOST = parser.get("rcon", "HOST")  # Hostname of the Minecraft server
PORT = parser.get("rcon", "PORT")  # Port number of the RCON server
PASSWORD = parser.get("rcon", "PASSWORD")  # Password of the RCON server

rcon = RCONClient(HOST, port=PORT)
if rcon.login(PASSWORD):
    print("RCON login successful")
else:
    print("RCON login failed")
    exit(0)

print("AutoWhitelist is starting up...")
bot_token = parser.get("discord", "BOT_TOKEN")
print("Your bot token is: ", bot_token)

def add_to_whitelist(username_for_add):
    resp = rcon.command("whitelist add " + username_for_add)
    print("Response: " + resp)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
    async def on_message(self, message): 
        # don't respond to ourselves
        if message.author == self.user:
            return
        if "whitelist" in message.content:
            query = message.content
            username_to_add = query.split(" ")[1]
            await message.channel.send('Adding ' + username_to_add + ' to whitelist')
            add_to_whitelist(username_to_add)

client = MyClient()
client.run(bot_token)