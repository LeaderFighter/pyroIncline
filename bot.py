import asyncio
import os
import time
import logging
from decouple import config
from pyrogram import Client
from pyrogram import enums
import random


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


STRING_SESSION = config("STRING_SESSION", default=None)

COUNT = config("COUNT", default=None)

CHATID = config("CHATID", default=None)

MESSAGE1 = config("MESSAGE1", default=None)

MESSAGE2 = config("MESSAGE2", default=None)

MESSAGE3 = config("MESSAGE3", default=None)

api_id = 2184829
api_hash = "6930b92388baabff4cb4a1d377085035"



async def main():
    async with Client(session_name=STRING_SESSION, API_ID, API_HASH) as app:
        await app.send_message("me", "Bot Deployed Successfully!")
        
        for i in range(COUNT):
            spam = [
            MESSAGE1,
            MESSAGE2,
            MESSAGE3
            ]
            
            myChoice = random.choice(spam)
      
            await app.send_chat_action(str(CHATID), enums.ChatAction.TYPING)
            await app.send_message(CHATID, myChoice)
            await app.send_chat_action(str(CHATID), enums.ChatAction.TYPING)
            await asyncio.sleep(0.4)

    app.run()
asyncio.run(main())
