
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add("📍 Моральна підтримка", "⚕ Реабілітація")
main_menu.add("📜 Правова підтримка", "🏛 Державні програми")

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Вітаю! Я бот для ветеранів Дніпропетровської області ♡♡\nОберіть розділ:", reply_markup=main_menu)

@dp.message_handler(lambda m: m.text == "📍 Моральна підтримка")
async def moral_support(message: types.Message):
    await message.answer("""📍 Центр психологічної допомоги ветеранів:
м. Дніпро, вул. Прикладна 12
+38 067 123 45 67""")

@dp.message_handler(lambda m: m.text == "⚕ Реабілітація")
async def rehab(message: types.Message):
    await message.answer("Перейдіть за посиланням, щоб дізнатися більше:
https://mva.gov.ua/dopomoha/reabilitaciya", parse_mode=types.ParseMode.MARKDOWN)

@dp.message_handler(lambda m: m.text == "📜 Правова підтримка")
async def legal_support(message: types.Message):
    await message.answer("🔹 Оформлення статусу інваліда війни:
https://mva.gov.ua/dopomoha/prava

🔹 Проходження МСЕК:
https://mva.gov.ua/dopomoha/msek")

@dp.message_handler(lambda m: m.text == "🏛 Державні програми")
async def gov(message: types.Message):
    await message.answer("📌 Державні програми дивіться тут:
https://mva.gov.ua/dopomoha/derzhavni-programi", parse_mode=types.ParseMode.MARKDOWN)

@dp.message_handler()
async def unknown(message: types.Message):
    await message.answer("Оберіть розділ з меню нижче:", reply_markup=main_menu)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
