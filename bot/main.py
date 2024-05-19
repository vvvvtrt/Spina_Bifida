from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
import requests
import asyncio

bot = Bot("")
dq = Dispatcher(bot)

url_fastapi = "https://699e-31-173-85-46.ngrok-free.app"
url_web = ""

@dq.message_handler(commands=["start"])
async def start(message: types.Message):
    await bot.send_message(message.chat.id, 'Введите свою почту для авторизации')


@dq.message_handler(commands=["app"])
async def start(message: types.Message):
    print(message.from_user.id)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton(f"Открыть карточки посетителей", web_app=WebAppInfo(url=f"https://vvvvtrt2.pythonanywhere.com/biography/{message.from_user.id}"))
    markup.add(button)
    await message.answer("Выберите эпитафию или сделайте выбор в wedapps", reply_markup=markup)

@dq.message_handler(content_types=["text"])
async def text(message):
    try:
        data = {"email": message.text, "id_tg": message.from_user.id}

        response = requests.post(url_fastapi + "/api/v1/add_tg_id", json=data)

        await bot.send_message(message.chat.id, 'Вы успешно авторизировались, чтобы найти карточку пациента воспользуйтесь командой /app')
    except:
        await bot.send_message(message.chat.id, 'Произошла ошибка, проверьте данные')

@dq.message_handler(content_types=["web_app_data"])
async def web_app(message: types.Message):
    print(message.web_app_data)
    await message.answer(str(message.web_app_data["data"]))

async def get_message():
    response = requests.get(url_fastapi + "/api/v1/get_message")

    for i in response.json()["data"]:
        await bot.send_message(i[0], i[1])

async def send_message(update_interval=5):
    while True:
        await get_message()

        await asyncio.sleep(update_interval)
        print("[INFO] working")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(send_message())
    executor.start_polling(dq)
    loop.run_forever()
