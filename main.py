from aiogram import Bot, Dispatcher, executor, types
from config import telegram_token


help_command = """
<b>/start</b> - <em>начать работу с ботом</em>
<b>/help</b> - <em>список комманд</em>
<b>/give</b> - <em>можешь получить уникальный стикер</em>
"""

bot = Bot(token = telegram_token)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот был успешно запущен!')

@dp.message_handler(commands='help')
async def help(message: types.Message):
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
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEMObFmWbUr5UNWIzR8yCiY7plUkgUYYQAC6TsAAo1lQUmkQ8obQWPbUjUE')

@dp.message_handler()
async def emoji(message: types.Message):
    await message.answer(message.text + '❤️ ')

@dp.message_handler()
async def send_sticker(message: types.Message):
    if message.text == "❤️  ":
        await message.answer("🖤")

# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(text=message.text.capitalize())  # Написать на сообщение

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)