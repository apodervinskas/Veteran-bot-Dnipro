from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import logging
import os

API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Головне меню
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(KeyboardButton("💬 Моральна підтримка"))
main_menu.add(KeyboardButton("⚖️ Правова підтримка"))
main_menu.add(KeyboardButton("🦿 Реабілітація"))
main_menu.add(KeyboardButton("📞 Контакти депутатів"))

# Депутати по районах
districts = {
    "dist_sobornyi": "Соборний",
    "dist_shevchenko": "Шевченківський",
    "dist_krivyi": "Кривий Ріг",
    "dist_pavlograd": "Павлоград",
    "dist_nikopol": "Нікополь",
    "dist_kamianske": "Кам’янське"
}

districts_keyboard = InlineKeyboardMarkup(row_width=1)
for key, label in districts.items():
    districts_keyboard.insert(InlineKeyboardButton(label, callback_data=key))

deputies = {
    "dist_sobornyi": ["Іван Іванов – +38 067 123 4567", "Олена Петрівна – +38 067 765 4321"],
    "dist_shevchenko": ["Марко Тарас – +38 067 111 2233"],
    "dist_krivyi": ["Наталя Коломацька – +38 067 388 9900"],
    "dist_pavlograd": ["Андрій Семенов – +38 067 222 3344"],
    "dist_nikopol": ["Ірина Савчук – +38 067 555 6666"],
    "dist_kamianske": ["Василь Литвин – +38 067 333 4444"]
}

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Вітаю! Я бот для ветеранів Дніпропетровської області ♡♡ Оберіть розділ:", reply_markup=main_menu)

@dp.message_handler(lambda m: m.text == "💬 Моральна підтримка")
async def moral_support(message: types.Message):
    await message.answer("💬 Центр психологічної допомоги ветеранів (Дніпро): +38 067 123 45 67")

@dp.message_handler(lambda m: m.text == "⚖️ Правова підтримка")
async def legal_support(message: types.Message):
    await message.answer("⚖️ Напрями правової підтримки:")

("1. Проходження МСЕК")
("2. Оформлення пенсії")
("3. Статус інваліда війни")

@dp.message_handler(lambda m: m.text == "🦿 Реабілітація")
async def rehabilitation(message: types.Message):
    await message.answer("⏱ Реабілітація ветеранів:\n\n👉 Протезування\n👉 Реабілітаційні центри\n👉 Програми підтримки")


@dp.message_handler(lambda m: m.text == "📞 Контакти депутатів")
async def contact_deputies(message: types.Message):
    await message.answer("📍 Оберіть свій район:", reply_markup=districts_keyboard)

@dp.callback_query_handler(lambda c: c.data in deputies)
async def send_contacts(callback_query: types.CallbackQuery):
    district = callback_query.data
    contacts = deputies[district]
    await bot.send_message(callback_query.from_user.id, f"Контакти депутатів у районі:\n{some_variable}")

".join(contacts))

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
