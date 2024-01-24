from vkbottle.bot import Bot, Message
from vkbottle import *
from pyowm.owm import OWM

bot = Bot(token="vk1.a.C_QxUPu1KbMgKjXpWOMc6_5id0Py_Hj5jr3r9GIN1sHDypJLsKkSj6eQnGDM9Wudxy5u57R_w0RuoS-JX5pXYMVBCNRcpmFWYMmiedXp8zci4jckVaMt59Os-3Hanm2v1WLe0byeebKyAftdWe2V_Fy6BrfB5nx1_qg_hWudZVgELW9BvG0o_hqVlHVGMFJN0D4WoghSYVGaycDdmtUs6Q")

ctx = CtxStorage()


class Weather(BaseStateGroup):
    city_name = None


@bot.on.private_message(text="start")
@bot.on.private_message(payload={"back": "start"})
async def start(message:Message):
    keyboard = Keyboard(one_time=True)
    # keyboard.add(Text("GPT", {"next": "gpt"}), color=KeyboardButtonColor.NEGATIVE)
    keyboard.add(Text("Погода"), color=KeyboardButtonColor.POSITIVE)
    await message.answer("Выберите что-то из предложенного списка", keyboard=keyboard)


@bot.on.private_message(lev="Погода")
@bot.on.private_message(payload={"next": "weather"})
async def waiting_for_city_name(message:Message):
    await bot.state_dispenser.set(message.peer_id, Weather.city_name)
    return "Введите название города"


@bot.on.private_message(state=Weather.city_name)
async def test(message:Message):
    ctx.set("city_name", message.text)
    await bot.state_dispenser.delete(message.peer_id)
    city = ctx.get("city_name")

    keyboard = Keyboard(one_time=True)
    keyboard.add(Text("Другой город", {"next": "weather"}), color=KeyboardButtonColor.NEGATIVE)
    keyboard.add(Text("Назад", {"back": "start"}), color=KeyboardButtonColor.POSITIVE)

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
        await message.answer(ad, keyboard=keyboard)

bot.run_forever()
