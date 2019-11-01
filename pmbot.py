import telethon
import logging
logging.basicConfig(level=logging.WARNING)
logger = logging.getlogger(__name__)
from config import API_ID, API_HASH

client = telethon.TelegramClient("pmbot", API_ID, API_HASH)
client.start()
memory = {}

@client.on(telethon.events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def start(event):
    sender = await event.get_sender()
    me = await client.get_me()
    if sender.is_bot:
        return
    if event.from_id == me.id:
        return
    if event.from_id in memory:
        await event.reply("""Il mio capo sta valutando se risponderti o no. Attendi fino alla sua risposta""")
    else:
        await event.reply("""Non spammare, il mio capo presto ti risponderà. Attendi fino alla sua risposta.""")
        memory[event.from_id] = 1

@client.on(telethon.events.NewMessage(pattern=r"\.off", outgoing=True))
async def shutdown(event):
    client.remove_event_handler(start)
    await event.edit("PM Bot switched off...")

@client.on(telethon.events.NewMessage(pattern=r"\.on", outgoing=True))
async def shutdown(event):
    client.add_event_handler(start, telethon.events.New.Message(incoming=True, func=lambda e: e.is_private))
    await event.edit("PM Bot switched on...")
client.run_until_disconnected()
