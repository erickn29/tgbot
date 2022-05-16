from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton
import emoji


button_weather = KeyboardButton(emoji.emojize(':sun: Погода'))
button_news = KeyboardButton(emoji.emojize(':newspaper: Новости'))
button_currency = KeyboardButton(emoji.emojize(':chart_increasing_with_yen: Курсы валют'))

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.row(button_weather, button_news).add(button_currency)
