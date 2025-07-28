
from aiogram import types

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Вітаю! Я бот для ветеранів Дніпропетровської області ♡♡")
    await message.answer("Оберіть розділ:", reply_markup=main_menu)

@dp.message_handler(lambda m: m.text == "💬 Моральна підтримка")
async def moral_support(message: types.Message):
    await message.answer("Центр психологічної допомоги ветеранів (Дніпро): +38 067 123 45 67")

@dp.message_handler(lambda m: m.text == "📄 Юридична допомога")
async def legal_support(message: types.Message):
    await message.answer("Перейдіть за посиланням, щоб дізнатися більше:
https://example.com")
