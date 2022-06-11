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

API_ID = 2184829
API_HASH = "6930b92388baabff4cb4a1d377085035"



async def main():
    async with Client("kids", API_ID, API_HASH) as app:
        await app.send_message("me", "Bot Deployed Successfully!")
        print ("Bot Deployed To Spam!!!")
        
        try:
            for i in range(int(COUNT)):
                spam = [
                MESSAGE1,
                MESSAGE2,
                MESSAGE3
                ]
                
                myChoice = random.choice(spam)
                try:
                    await app.send_chat_action(int(CHATID), enums.ChatAction.TYPING)
                    await app.send_message(int(CHATID), myChoice)
                    await app.send_chat_action(int(CHATID), enums.ChatAction.TYPING)
                    await asyncio.sleep(0.4)
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)
asyncio.run(main())
