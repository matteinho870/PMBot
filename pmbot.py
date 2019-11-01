import telethon
from config import API_ID, API_HASH

client = telethon.TelegramClient("pmbot", API_ID, API_HASH)

@client.on(telethon.events.New.Message(incoming=True, func=lambda e: e.is_private))
async def start(event):
    sender = await event.get_sender()
    me = await client.get_me()
    if sender.is_bot:
        return
    if event.from_id == me.id:
        return
    await event.reply("""""")
    await event.reply("""""")

@client.on(telethon.events.NewMessage(pattern=r"\.off", outgoing=True))
async def shutdown(event):
    client.remove_event_handler(start)
    await event.edit("PM Bot switched off...")

@client.on(telethon.events.NewMessage(pattern=r"\.on", outgoing=True))
async def shutdown(event):
    client.add_event_handler(start, telethon.events.New.Message(incoming=True, func=lambda e: e.is_private))
    await event.edit("PM Bot switched on...")
