from vkbottle.bot import Bot, Message
from pyowm.owm import OWM

bot = Bot(token="vk1.a.C_QxUPu1KbMgKjXpWOMc6_5id0Py_Hj5jr3r9GIN1sHDypJLsKkSj6eQnGDM9Wudxy5u57R_w0RuoS-JX5pXYMVBCNRcpmFWYMmiedXp8zci4jckVaMt59Os-3Hanm2v1WLe0byeebKyAftdWe2V_Fy6BrfB5nx1_qg_hWudZVgELW9BvG0o_hqVlHVGMFJN0D4WoghSYVGaycDdmtUs6Q")

@bot.on.message(text=["Привет","привет","Ку"])
async def message_handler(message:Message):
    await message.answer("Привет")


@bot.on.chat_message(text=["/погода <city>"])
async def city_chat(message:Message, city=None):
    owm = OWM('d6901b7f0e58a81b6e3b55dc1f85fb1e')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    w = observation.weather
    temperature = w.temperature('celsius')['temp']
    weather = w.status.lower()
    wind = w.wind()['speed']
    humi = w.humidity
    if weather == "snow":
        weather = "снег"
    elif weather == "clouds":
        weather = "облачно"
    elif weather == "rain":
        weather = "дождь"

    ad = (f"По запросу города {city} найдено:\n Температура: {temperature}℃"
          f"\n Погода: {weather}\n Ветер: {wind} м/с\n Влажность: {humi}%")

    if city is not None:
        await message.answer(ad)

    else:
        await message.answer("говно")

bot.run_forever()
