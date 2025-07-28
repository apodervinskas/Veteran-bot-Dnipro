import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import F

TOKEN = os.getenv("BOT_TOKEN") or "ВАШ_ТОКЕН_ТУТ"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

# Головне меню
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("Моральна підтримка", callback_data="support"),
        InlineKeyboardButton("Реабілітація", callback_data="rehab"),
        InlineKeyboardButton("Правова підтримка", callback_data="legal"),
        InlineKeyboardButton("Фінансова допомога", callback_data="financial"),
        InlineKeyboardButton("Державні програми", callback_data="programs")
    )
    await message.answer("Вітаю! Оберіть розділ 👇", reply_markup=keyboard)

# Моральна підтримка
@dp.callback_query_handler(lambda c: c.data == "support")
async def moral_support(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await bot.send_message(callback_query.from_user.id,
        "🧠 Центр психологічної допомоги ветеранам:"

        "https://mva.gov.ua/pidtrimka-veteraniv-ta-chleniv-rodin"


        "📞 Гаряча лінія підтримки: 0 800 33 92 91"
    )

# Реабілітація
@dp.callback_query_handler(lambda c: c.data == "rehab")
async def rehab(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await bot.send_message(
    callback_query.from_user.id,
    "🧠 Реабілітація:\n"
    "🔹 Протезування: https://mva.gov.ua/rehabilitaciya-ta-protezuvannya\n"
    "🔹 Реабілітаційні центри: https://mva.gov.ua/dlya-veteraniv/rehabilitaciyni-zakladi\n"
    "🔹 Програми підтримки: https://mva.gov.ua/diyalnist/rehabilitaciya"
)

    
# Правова підтримка
@dp.callback_query_handler(lambda c: c.data == "legal")
async def legal_support(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await bot.send_message(callback_query.from_user.id,
        "⚖️ Правова підтримка:"

        "1. Проходження МСЕК: https://mva.gov.ua/diyalnist/mediko-socialna-ekspertiza"

        "2. Оформлення пенсії: https://mva.gov.ua/pitannya-pensijnogo-zabezpechennya"

        "3. Статус інваліда війни: https://mva.gov.ua/dokumenty-ta-statusy"
    )

# Фінансова допомога
@dp.callback_query_handler(lambda c: c.data == "financial")
async def financial_aid(callback_query: types.CallbackQuery):
    await callback_query.answer()
    contacts = [
        "🏛 Дніпровський район: Іваненко О.О. – 099 123 45 67",
        "🏛 Кам’янський район: Петренко І.І. – 098 765 43 21"
    ]
    await bot.send_message(callback_query.from_user.id,
        "💸 Фінансова допомога від місцевої влади:"
        "✅ Щорічна допомога ветеранам (від мерів та депутатів)"
        "🔗 Детальніше: https://mva.gov.ua/pidtrimka/finansova"
   )     
# Державні програми
@dp.callback_query_handler(lambda c: c.data == "programs")
async def state_programs(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await bot.send_message(
    callback_query.from_user.id,
    (
        "📜 Державні програми:\n"
        "➤ Всі програми для ветеранів: https://mva.gov.ua/programi\n"
        "➤ Є-Ветеран: https://eveteran.gov.ua/"
    )
)



 
import asyncio

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())