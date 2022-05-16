from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
import emoji
from aiogram.dispatcher.filters import Text
from aiogram.utils.callback_data import CallbackData
from random import randint
from .weather import get_weather
from .news import *
from .currency import get_currency


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    if message.from_user.first_name:
        await bot.send_message(message.from_user.id,
                                   f'Дароу, {message.from_user.first_name}, чем могу помочь?',
                               reply_markup=kb_client)
    else:
        await bot.send_message(message.from_user.id,
                                   f'Хай, чем могу помочь?')

############################## ПОГОДА ################################

cb = CallbackData("post", "id", "action")

def get_kb():
    buttons = [
        types.InlineKeyboardButton(text="Архангельск", callback_data=cb.new(id=1, action="arkh")),
        types.InlineKeyboardButton(text="Санкт-Петербург", callback_data=cb.new(id=2, action="spb")),
        types.InlineKeyboardButton(text="Москва", callback_data=cb.new(id=3, action="msk")),
        types.InlineKeyboardButton(text="Краснодар", callback_data=cb.new(id=4, action="krd")),
        types.InlineKeyboardButton(text="Калинингад", callback_data=cb.new(id=5, action="kng")),
        types.InlineKeyboardButton(text="Нижний Новгород", callback_data=cb.new(id=6, action="nn")),
        types.InlineKeyboardButton(text="Ярославль", callback_data=cb.new(id=7, action="yar")),
        types.InlineKeyboardButton(text="Казань", callback_data=cb.new(id=8, action="kzn")),
        types.InlineKeyboardButton(text="Анталья", callback_data=cb.new(id=9, action="ala")),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    keyboard.add(*buttons)
    return keyboard


async def command_weather(message: types.Message):
    keyboard = get_kb()
    await message.answer(emoji.emojize("Выберите город. Я покажу прогноз погоды на неделю!"), reply_markup=keyboard)


@dp.callback_query_handler(cb.filter())
async def callbacks(call: types.CallbackQuery, callback_data: dict):
    post_id = callback_data["id"]
    action = callback_data["action"]
    if action == 'arkh':
        await call.message.answer(get_weather(action), parse_mode='Markdown')
        await call.answer()
    elif action == 'spb':
        await call.message.answer(get_weather(action), parse_mode='Markdown')
        await call.answer()
    elif action == 'msk':
        await call.message.answer(get_weather(action), parse_mode='Markdown')
        await call.answer()
    elif action == 'krd':
        await call.message.answer(get_weather(action), parse_mode='Markdown')
        await call.answer()
    elif action == 'kng':
        await call.message.answer(get_weather(action), parse_mode='Markdown')
        await call.answer()
    elif action == 'nn':
        await call.message.answer(get_weather(action), parse_mode='Markdown')
        await call.answer()
    elif action == 'yar':
        await call.message.answer(get_weather(action), parse_mode='Markdown')
        await call.answer()
    elif action == 'kzn':
        await call.message.answer(get_weather(action), parse_mode='Markdown')
        await call.answer()
    elif action == 'ala':
        await call.message.answer(get_weather(action), parse_mode='Markdown')
        await call.answer()
    elif action == 'ftbl':
        await call.message.answer(get_football_news(), parse_mode='Markdown')
        await call.answer()
    elif action == 'soc':
        await call.message.answer(get_soc_news(), parse_mode='Markdown')
        await call.answer()
    elif action == 'pol':
        await call.message.answer(get_politics_news(), parse_mode='Markdown')
        await call.answer()
    elif action == 'eco':
        await call.message.answer(get_econamics_news(), parse_mode='Markdown')
        await call.answer()
    elif action == 'tech':
        await call.message.answer(get_tech_news(), parse_mode='Markdown')
        await call.answer()
    elif action == 'gam':
        await call.message.answer(get_games_news(), parse_mode='Markdown')
        await call.answer()
    elif action == 'arhafisha':
        await call.message.answer(get_arh_afisha(), parse_mode='Markdown')
        await call.answer()
    elif action == 'arhnews':
        await call.message.answer(get_arh_news(), parse_mode='Markdown')
        await call.answer()


############################## НОВОСТИ ################################

def get_news_kb():
    buttons = [
        types.InlineKeyboardButton(text="АрхАфиша", callback_data=cb.new(id=10, action="arhafisha")),
        types.InlineKeyboardButton(text="АрхНовости", callback_data=cb.new(id=10, action="arhnews")),
        types.InlineKeyboardButton(text="Общество", callback_data=cb.new(id=2, action="soc")),
        types.InlineKeyboardButton(text="Политика", callback_data=cb.new(id=2, action="pol")),
        types.InlineKeyboardButton(text="Экономика", callback_data=cb.new(id=2, action="eco")),
        types.InlineKeyboardButton(text="Технологии", callback_data=cb.new(id=2, action="tech")),
        types.InlineKeyboardButton(text="Игры", callback_data=cb.new(id=2, action="gam")),
        types.InlineKeyboardButton(text="Футбол", callback_data=cb.new(id=10, action="ftbl")),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


async def command_news(message: types.Message):
    keyboard = get_news_kb()
    await message.answer(emoji.emojize("Какие новости интересуют?"), reply_markup=keyboard)

############################## ВАЛЮТЫ ################################

async def command_currency(message: types.Message):
    # await call.message.answer(get_currency(), parse_mode='Markdown')
    # await call.answer()
    await bot.send_message(message.from_user.id, get_currency())


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_weather, Text(equals=emoji.emojize(':sun: Погода')))
    dp.register_message_handler(command_news, Text(equals=emoji.emojize(':newspaper: Новости')))
    dp.register_message_handler(command_currency, Text(equals=emoji.emojize(':chart_increasing_with_yen: Курсы валют')))
