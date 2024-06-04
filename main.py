from aiogram import Bot, Dispatcher, executor, types
from config import telegram_token

help_command = """
<b>/start</b> - <em>начать работу с ботом</em>
<b>/help</b> - <em>список комманд</em>
<b>/give</b> - <em>можешь получить уникальный стикер</em>
<b>/картинка</b> - <em>крутая картинка</em>
<b>/location</b> - <em>показывает заданную локацию.</em>
"""

bot = Bot(token = telegram_token) # Создадим объект класса бот
dp = Dispatcher(bot) # Передаем объект класса бот

async def on_startup(_):
    print('Бот был успешно запущен!')

@dp.message_handler(commands='help')     # Создаем диспетчер который будет обрабатывать команды в нашем случае это 'help'
async def help(message: types.Message):  # Создаем ассихронную функцию, которая обрабатывает эту команду, создадим message типа Message
    await message.answer(text=help_command, parse_mode="HTML")
    await message.delete()

@dp.message_handler(commands='start')
async def start(message: types.Message):
    user_name = message.from_user.first_name
    # await message.answer(f'Привет, {user_name
    await message.answer(f'<em><b>Здравствуй {user_name}!</b> Добро пожаловать в наш Бот!</em>', parse_mode="HTML")
    await message.delete()

@dp.message_handler(commands='give')
async def give(message: types.Message):
    await message.answer('Поздравляю! Ты нашел секретный команду. В подарок я тебе отправляю крутой стикер.')
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEMPOhmXZk01msvrs5upnB_IxJBDHxI0gACASYAAsqriUshdPqhh3WEnTUE')

@dp.message_handler()
async def emoji(message: types.Message):
    await message.answer(message.text + '❤️ ')

@dp.message_handler()
async def send_sticker(message: types.Message):
    if message.text == "❤️  ":
        await message.answer("🖤")

@dp.message_handler(commands='картинка')
async def send_command_image(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo='https://img.razrisyika.ru/kart/90/1200/358432-krutye-ochen-35.jpg')
    await message.delete()

@dp.message_handler(commands='location')
async def send_point(message: types.Message):
    await bot.send_location(chat_id=message.from_user.id, latitude=55.69115137123731, # Широта
                            longitude=37.61153088545992) # Долгота
    await message.delete()

# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(text=message.text.capitalize())  # Написать на сообщение


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)