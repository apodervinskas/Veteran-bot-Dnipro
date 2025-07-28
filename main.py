import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Command
from aiogram.types.message import Message
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(
    KeyboardButton("💬 Моральна підтримка"),
    KeyboardButton("♿ Реабілітація"),
    KeyboardButton("⚖ Правова підтримка"),
)
main_menu.add(
    KeyboardButton("💰 Фінансова допомога"),
    KeyboardButton("📋 Державні програми")
)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(
        "Вітаю! Я бот для ветеранів Дніпропетровської області 💙💛\nОберіть розділ:",
        reply_markup=main_menu
    )

@dp.message_handler(lambda message: message.text == "💬 Моральна підтримка")
async def moral_support(message: types.Message):
    await message.answer(
        "📞 Центр психологічної допомоги ветеранів:
"
        "• м. Дніпро: +38 067 123 45 67
"
        "• м. Кривий Ріг: +38 099 222 33 44
"
        "• Telegram‑чат з психологом: @dnipro_psy_support
"
        "• [Графік груп підтримки](https://dnipro-veterans.org)",
        parse_mode=types.ParseMode.MARKDOWN
    )

@dp.message_handler(lambda message: message.text == "♿ Реабілітація")
async def rehab(message: types.Message):
    await message.answer(
        "♿ *Реабілітація:*
"
        "• [Протезування](https://mva.gov.ua/rehabilitation/protezuvannya)
"
        "• [Реабілітаційні центри](https://mva.gov.ua/rehabilitation/tsentri-reabilitaciyi)
"
        "• [Програми реабілітації](https://mva.gov.ua/rehabilitation/programi)",
        parse_mode=types.ParseMode.MARKDOWN
    )

@dp.message_handler(lambda message: message.text == "⚖ Правова підтримка")
async def legal_support(message: types.Message):
    await message.answer(
        "⚖ *Правова підтримка:*
"
        "• [Проходження МСЕК](https://mva.gov.ua/prava/msek)
"
        "• [Оформлення пенсії для ветеранів](https://mva.gov.ua/prava/pensiyi)
"
        "• [Оформлення статусу інваліда війни](https://mva.gov.ua/prava/status-ogd)",
        parse_mode=types.ParseMode.MARKDOWN
    )

@dp.message_handler(lambda message: message.text == "📋 Державні програми")
async def programs(message: types.Message):
    await message.answer(
        "📋 Державні програми дивіться тут:
"
        "https://mva.gov.ua/dopomoha/derzhavni-programi",
        parse_mode=types.ParseMode.MARKDOWN
    )

@dp.message_handler(lambda message: message.text == "💰 Фінансова допомога")
async def financial(message: types.Message):
    await message.answer(
        "💰 Інформацію про щорічну допомогу від мерів та депутатів по районах можна отримати, обравши район.",
        reply_markup=main_menu
    )

@dp.message_handler()
async def fallback(message: types.Message):
    await message.answer("Оберіть розділ з меню нижче:", reply_markup=main_menu)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)