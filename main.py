from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import F
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
import asyncio
import logging

TOKEN = "8521847895:AAEtigpMdfSZ1LdPe7KC7JBlwljxZVF9tOQ"
ADMIN_ID = 494255577

defaults = DefaultBotProperties(parse_mode=ParseMode.HTML)
bot = Bot(token=TOKEN, default=defaults)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Услуги 🚀"), KeyboardButton(text="Обо мне 📝")],
    [KeyboardButton(text="Примеры работ 🖼"), KeyboardButton(text="Контакты ✉️")]
], resize_keyboard=True)

services_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Telegram-боты", callback_data="service_bots")],
    [InlineKeyboardButton(text="Парсинг и автоматизация", callback_data="service_parsing")],
    [InlineKeyboardButton(text="ИИ и ChatGPT интеграция", callback_data="service_ai")],
    [InlineKeyboardButton(text="Назад в главное меню", callback_data="back_main")]
])

@dp.message(Command("start"))
async def start(message: types.Message):
    text = (
        "<b>Привет! Я — демо-бот портфолио разработчика Telegram-ботов</b> 👋\n\n"
        "Здесь вы можете увидеть примеры моих работ и узнать, что я умею.\n"
        "Выберите раздел в меню ниже:"
    )
    await message.answer(text, reply_markup=main_kb)
    
    await bot.send_message(ADMIN_ID, 
        f"🚀 Новый пользователь запустил демо-бота!\n"
        f"ID: {message.from_user.id}\n"
        f"Username: @{message.from_user.username or 'нет'}\n"
        f"Имя: {message.from_user.full_name}")

@dp.message(F.text == "Услуги 🚀")
async def services(message: types.Message):
    await message.answer("Выберите интересующую услугу:", reply_markup=services_inline)

@dp.message(F.text == "Обо мне 📝")
async def about(message: types.Message):
    text = (
        "<b>О разработчике</b>\n\n"
        "Привет! Я — Iskander (@Iskander_70), специализируюсь на создании Telegram-ботов любой сложности на Python (aiogram 3.x).\n\n"
        "Опыт: от простых меню и заявок до умных ИИ-ботов с ChatGPT, магазинами, платежами и базами данных.\n"
        "Работаю быстро, код чистый, всегда на связи и делаю доработки по ТЗ.\n\n"
        "Готов взяться за ваш проект на Kwork!"
    )
    await message.answer(text, reply_markup=main_kb)

@dp.message(F.text == "Примеры работ 🖼")
async def examples(message: types.Message):
    text = (
        "<b>Примеры моих работ</b>\n\n"
        "Этот бот — один из примеров 🙂\n"
        "Также есть:\n"
        "• Бот для сбора заявок с формой и уведомлениями\n"
        "• ИИ-ассистент на ChatGPT для ответов на вопросы\n"
        "• Бот-магазин с каталогом и корзиной\n\n"
        "Все примеры живые — могу показать по запросу!"
    )
    await message.answer(text, reply_markup=main_kb)

@dp.message(F.text == "Контакты ✉️")
async def contacts(message: types.Message):
    await message.answer("Связаться со мной: @Iskander_70\nИли прямо на Kwork!", reply_markup=main_kb)

@dp.callback_query(F.data == "service_bots")
async def cb_bots(callback: types.CallbackQuery):
    text = (
        "<b>Telegram-боты любой сложности</b> 🤖\n\n"
        "Создаю ботов под ваши задачи:\n"
        "• Меню, кнопки, формы заявок\n"
        "• Интеграция с платежами (ЮKassa, Crypto)\n"
        "• Магазины и каталоги товаров\n"
        "• Рассылки, админ-панели\n"
        "• Боты для каналов/групп\n\n"
        "Примеры: бот для записи на услуги, опросник, уведомления о заказах.\n"
        "Цена от 1000 руб. за простой бот до 15–30к за сложный проект.\n"
        "Сроки: 1–7 дней. Полный код + инструкция по запуску."
    )
    await callback.message.edit_text(text, reply_markup=services_inline)
    await bot.send_message(ADMIN_ID, f"Пользователь интересуется Telegram-ботами! ID: {callback.from_user.id}")

@dp.callback_query(F.data == "service_parsing")
async def cb_parsing(callback: types.CallbackQuery):
    text = (
        "<b>Парсинг и автоматизация</b> 🕷\n\n"
        "Собираю данные с сайтов и сервисов:\n"
        "• Парсинг объявлений, цен, товаров\n"
        "• Автоматизация рутинных задач\n"
        "• Скрипты для мониторинга конкурентов\n"
        "• Работа с API (Avito, Wildberries, VK и др.)\n\n"
        "Примеры: парсер цен конкурентов, авто-заполнение Excel, мониторинг изменений на сайте.\n"
        "Цена от 3000 руб. за простой парсер до 15к за сложный с расписанием.\n"
        "Использую requests, BeautifulSoup, Selenium."
    )
    await callback.message.edit_text(text, reply_markup=services_inline)
    await bot.send_message(ADMIN_ID, f"Пользователь интересуется парсингом! ID: {callback.from_user.id}")

@dp.callback_query(F.data == "service_ai")
async def cb_ai(callback: types.CallbackQuery):
    text = (
        "<b>ИИ и ChatGPT интеграция</b> 🧠\n\n"
        "Делаю умных ботов:\n"
        "• Ответы на вопросы клиентов 24/7\n"
        "• Подбор товаров/услуг по описанию\n"
        "• Персональные ассистенты\n"
        "• RAG-системы с вашей базой знаний\n\n"
        "Примеры: ИИ-консультант для магазина, чат-бот для поддержки, генератор контента.\n"
        "Цена от 5000 руб. за базовую интеграцию до 30к+ за сложные решения.\n"
        "Использую OpenAI, Grok, LangChain."
    )
    await callback.message.edit_text(text, reply_markup=services_inline)
    await bot.send_message(ADMIN_ID, f"Пользователь интересуется ИИ-интеграцией! ID: {callback.from_user.id}")

@dp.callback_query(F.data == "back_main")
async def cb_back(callback: types.CallbackQuery):
    text = "Вернулись в главное меню 👇\nВыберите раздел:"
    await callback.message.edit_text(text, reply_markup=main_kb)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
