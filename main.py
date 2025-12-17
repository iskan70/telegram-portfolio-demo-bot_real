from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import F
from aiogram.enums import ParseMode  # Добавили это
from aiogram.client.default import DefaultBotProperties  # И это
import asyncio
import logging

# Токен бота
TOKEN = "8521847895:AAEtigpMdfSZ1LdPe7KC7JBlwljxZVF9tOQ"

# Твой ID админа
ADMIN_ID = 494255577

# Новый способ задания parse_mode по умолчанию (HTML)
defaults = DefaultBotProperties(parse_mode=ParseMode.HTML)

bot = Bot(token=TOKEN, default=defaults)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

# Главное Reply-меню
main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Услуги"), KeyboardButton(text="О нас")],
    [KeyboardButton(text="Контакты"), KeyboardButton(text="Помощь")]
], resize_keyboard=True)

# Inline-кнопки для "Услуги"
services_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Telegram-боты", callback_data="service_bots")],
    [InlineKeyboardButton(text="Парсинг и автоматизация", callback_data="service_parsing")],
    [InlineKeyboardButton(text="ИИ-интеграция", callback_data="service_ai")],
    [InlineKeyboardButton(text="Назад в меню", callback_data="back_main")]
])

@dp.message(Command("start"))
async def start(message: types.Message):
    text = (
        "<b>Добро пожаловать в демо-бота!</b>\n\n"
        "Я — пример работы разработчика Telegram-ботов на Python + aiogram.\n"
        "Выберите раздел в меню ниже 👇"
    )
    await message.answer(text, reply_markup=main_kb)
    
    # Уведомление тебе
    await bot.send_message(ADMIN_ID, 
        f"🚀 Новый пользователь запустил бота!\n"
        f"ID: {message.from_user.id}\n"
        f"Username: @{message.from_user.username or 'нет'}\n"
        f"Имя: {message.from_user.full_name}")

@dp.message(F.text == "Услуги")
async def services(message: types.Message):
    await message.answer("Выберите интересующую услугу:", reply_markup=services_inline)

@dp.message(F.text == "О нас")
async def about(message: types.Message):
    await message.answer("Я — портфолио-бот, демонстрирующий навыки разработки Telegram-ботов любой сложности.")

@dp.message(F.text == "Контакты")
async def contacts(message: types.Message):
    await message.answer("Связаться с разработчиком: @Iskander_70")

@dp.message(F.text == "Помощь")
async def help_cmd(message: types.Message):
    await message.answer("Нажмите /start для возврата в главное меню.")

# Inline-обработчики
@dp.callback_query(F.data == "service_bots")
async def cb_bots(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "✅ <b>Telegram-боты</b>\n\nСоздаю ботов любой сложности: меню, сбор заявок, магазины, интеграции.",
        reply_markup=services_inline
    )

@dp.callback_query(F.data == "service_parsing")
async def cb_parsing(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "✅ <b>Парсинг и автоматизация</b>\n\nСбор данных с сайтов, автоматизация задач, скрипты на Python.",
        reply_markup=services_inline
    )

@dp.callback_query(F.data == "service_ai")
async def cb_ai(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "✅ <b>ИИ-интеграция</b>\n\nПодключение ChatGPT/OpenAI, умные ответы, RAG-системы.",
        reply_markup=services_inline
    )

@dp.callback_query(F.data == "back_main")
async def cb_back(callback: types.CallbackQuery):
    await callback.message.edit_text("Вернулись в главное меню 👇", reply_markup=main_kb)

# Запуск polling
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
