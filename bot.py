from vkbottle.bot import Bot, Message
from pyowm.owm import OWM
import threading
import time

bot = Bot(token="vk1.a.C_QxUPu1KbMgKjXpWOMc6_5id0Py_Hj5jr3r9GIN1sHDypJLsKkSj6eQnGDM9Wudxy5u57R_w0RuoS-JX5pXYMVBCNRcpmFWYMmiedXp8zci4jckVaMt59Os-3Hanm2v1WLe0byeebKyAftdWe2V_Fy6BrfB5nx1_qg_hWudZVgELW9BvG0o_hqVlHVGMFJN0D4WoghSYVGaycDdmtUs6Q")

@bot.on.message(text=["Привет","привет","Ку"])
async def message_handler(message:Message):
    await message.answer("Привет")
    time.sleep(86400)

threading.Thread(target = message_handler, args = (1,), daemon = True).start()

bot.run_forever()
