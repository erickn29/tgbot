from aiogram.utils import executor
from create_bot import dp
from handlers import admin, client, other


# TOKEN = os.getenv('TOKEN')
# botname = 'my_1st_secretary_bot'


def main():

    async def on_startup(_):
        print('<== Бот запущен ==>')

    client.register_handlers_client(dp)
    other.register_handlers_other(dp)  # Должен быть последним!

    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


if __name__ == '__main__':
    main()
