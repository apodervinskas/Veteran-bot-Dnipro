import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from datetime import date
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.row("💬 Моральна підтримка", "♿ Реабілітація")
main_menu.row("⚖ Правова підтримка", "💰 Фінансова допомога")
main_menu.row("🏛 Державні програми")

districts_keyboard = InlineKeyboardMarkup(row_width=2)
districts = {
    "dist_sobornyi": "Соборний район, Дніпро",
    "dist_shevchenko": "Шевченківський район, Дніпро",
    "dist_krivyi": "М. Кривий Ріг, Металургійний район",
    "dist_pavlograd": "М. Павлоград",
    "dist_nikopol": "М. Нікополь",
    "dist_kamianske": "М. Кам’янське"
}
for key, label in districts.items():
    districts_keyboard.insert(InlineKeyboardButton(label, callback_data=key))

deputies = {
    "dist_sobornyi": ["Іван Іванов – +38 067 123 4567", "Олена Петрівна – +38 067 765 4321"],
    "dist_shevchenko": ["Марко Тарас – +38 067 111 2233"],
    "dist_krivyi": ["Наталя Коваль – +38 067 888 9900"],
    "dist_pavlograd": ["Андрій Семенов – +38 067 222 3344"],
    "dist_nikopol": ["Ірина Савчук – +38 067 555 6666"],
    "dist_kamianske": ["Василь Литвин – +38 067 333 4444"]
}

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Вітаю! Я бот для ветеранів Дніпропетровської області 💙💛")
Оберіть розділ:", reply_markup=main_menu)

@dp.message_handler(lambda m: m.text == "💬 Моральна підтримка")
async def moral_support(message: types.Message):
    await message.answer(
        "🫂 Моральна підтримка:
"
        "• Центр психологічної допомоги ветеранів (Дніпро): +38 067 123 45 67
"
        "• Telegram‑чат з психологом: @dnipro_psy_support
"
        "• [Графік груп підтримки](https://dnipro-veterans.org)",
        parse_mode=types.ParseMode.MARKDOWN
    )

@dp.message_handler(lambda m: m.text == "♿ Реабілітація")
async def rehab(message: types.Message):
    await message.answer(
        "♿ Реабілітація:
"
        "• Протезування: https://mva.gov.ua/rehabilitation/protezuvannya
"
        "• Реабілітаційні центри: https://mva.gov.ua/rehabilitation/tsentri-reabilitaciyi
"
        "• Програми реабілітації: https://mva.gov.ua/rehabilitation/programi",
        parse_mode=types.ParseMode.MARKDOWN
    )

@dp.message_handler(lambda m: m.text == "⚖ Правова підтримка")
async def legal(message: types.Message):
    await message.answer(
        "⚖ Правова підтримка:
"
        "• Проходження МСЕК: https://mva.gov.ua/prava/msek
"
        "• Оформлення пенсії для ветеранів: https://mva.gov.ua/prava/pensiyi
"
        "• Оформлення статусу інваліда війни: https://mva.gov.ua/prava/status-ogd",
        parse_mode=types.ParseMode.MARKDOWN
    )

@dp.message_handler(lambda m: m.text == "💰 Фінансова допомога")
async def ask_district(message: types.Message):
    await message.answer("🔹 Оберіть ваш район:", reply_markup=districts_keyboard)

@dp.callback_query_handler(lambda c: c.data.startswith("dist_"))
async def handle_district(c: types.CallbackQuery):
    name = districts[c.data]
    deps = deputies[c.data]
    fullname = c.from_user.full_name
    today = date.today().strftime("%d.%m.%Y")
    statement = (
        f"ЗАЯВА

"
        f"Я, {fullname}, ветеран війни, звертаюся до Вас як до депутата громади {name} "
        f"з проханням про щорічну матеріальну допомогу.

"
        f"Дата: {today}
Підпис: ____________"
    )
    await bot.send_message(c.from_user.id,
        f"📋 *Район:* {name}
"
        f"👥 *Ваші депутати:*
• " + "
• ".join(deps),
        parse_mode=types.ParseMode.MARKDOWN)
    await bot.send_message(c.from_user.id,
        f"📝 *Шаблон заяви:*
```{statement}```",
        parse_mode=types.ParseMode.MARKDOWN)

@dp.message_handler(lambda m: m.text == "🏛 Державні програми")
async def gov(message: types.Message):
    await message.answer(
        "🏛 Державні програми дивіться тут:
"
        "https://mva.gov.ua/dopomoha/derzhavni-programi",
        parse_mode=types.ParseMode.MARKDOWN
    )

@dp.message_handler()
async def unknown(message: types.Message):
    await message.answer("Оберіть розділ з меню нижче:", reply_markup=main_menu)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)