import logging
import os
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN") or "ВАШ_ТОКЕН_ТУТ"

# Налаштування логування
logging.basicConfig(level=logging.INFO)

# Ініціалізація бота та диспетчера
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
router = Router()
dp.include_router(router)


# Стартове повідомлення
@router.message(commands=['start'])
async def cmd_start(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📘 Довідкова інформація", callback_data="info")],
        [InlineKeyboardButton(text="🦿 Реабілітація", callback_data="rehab")],
        [InlineKeyboardButton(text="⚖️ Правова підтримка", callback_data="law")],
        [InlineKeyboardButton(text="💰 Фінансова допомога", callback_data="finance")],
        [InlineKeyboardButton(text="👥 Контакти депутатів", callback_data="contacts")],
        [InlineKeyboardButton(text="🏛️ Державні програми", callback_data="programs")],
    ])
    await message.answer("👋 Вітаю! Оберіть розділ:", reply_markup=keyboard)


# Довідкова інформація
@router.callback_query(lambda c: c.data == "info")
async def show_info(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "ℹ️ <b>Довідкова інформація</b>\n\n"
        "📌 Телефон гарячої лінії Мінветеранів: 0-800-33-20-29\n"
        "📌 Адреса: Київ, вул. Липська 5\n"
        "📌 Сайт: https://mva.gov.ua"
    )


# Реабілітація
@router.callback_query(lambda c: c.data == "rehab")
async def show_rehab(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "🦿 <b>Реабілітація</b>\n\n"
        "🔹 Протезування: https://mva.gov.ua/pages/protezuvannya\n"
        "🔹 Центри реабілітації: https://mva.gov.ua/pages/reabilitaciyni-zakladi\n"
        "🔹 Програми: https://mva.gov.ua/pages/reabilitaciyni-programi"
    )


# Правова підтримка
@router.callback_query(lambda c: c.data == "law")
async def show_law(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "⚖️ <b>Правова підтримка</b>\n\n"
        "🔸 Проходження МСЕК: https://mva.gov.ua/pages/msek\n"
        "🔸 Оформлення пенсії: https://mva.gov.ua/pages/pensii-veteranam\n"
        "🔸 Статус інваліда війни: https://mva.gov.ua/pages/status-invalidnosti"
    )


# Фінансова допомога
@router.callback_query(lambda c: c.data == "finance")
async def show_finance(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "💰 <b>Фінансова допомога від місцевої влади:</b>\n"
        "✅ Щорічна допомога ветеранам (від мерів та депутатів)\n"
        "🔗 Детальніше: https://mva.gov.ua/pidtrimka/finansova"
    )


# Контакти депутатів
@router.callback_query(lambda c: c.data == "contacts")
async def show_contacts(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "👥 <b>Контакти депутатів Дніпропетровської області:</b>\n"
        "📍 Список депутатів: https://dniprorada.gov.ua/structure/deputies"
    )


# Державні програми
@router.callback_query(lambda c: c.data == "programs")
async def show_programs(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "🏛️ <b>Державні програми:</b>\n"
        "📎 Всі програми для ветеранів: https://mva.gov.ua/programi\n"
        "📎 е-Ветеран: https://eveteran.gov.ua/"
    )


# Запуск бота
if __name__ == "__main__":
    import asyncio

    async def main():
        await dp.start_polling(bot)

    asyncio.run(main())


if __name__ == "__main__":
    if not TOKEN or TOKEN == "ВАШ_ТОКЕН_ТУТ":
        raise ValueError("❌ BOT_TOKEN не встановлено у .env або Render Secret")
    import asyncio
    asyncio.run(dp.start_polling(bot))
