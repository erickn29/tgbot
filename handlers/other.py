from aiogram import types, Dispatcher
from create_bot import dp, bot


# @dp.message_handler()
async def echo_send(message: types.Message):
    if message.text.lower() in ['minecraft', 'майнкрафт', 'майн']:
        await bot.send_message(message.from_user.id, 'Это топ!')
    elif message.text.lower() in ['gta', 'гта',]:
        await bot.send_message(message.from_user.id, 'Это тоже топ!')
    print(f'Принял сообщение "{message.text}"')
    # await message.answer(message.text)
    # await message.reply(message.text)
    await bot.send_message(message.from_user.id, message.text)


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)