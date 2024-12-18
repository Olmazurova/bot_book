import asyncio
import logging


from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers
from keyboards.main_menu import set_main_menu


# Инициализируем логгер
logger = logging.getLogger(__name__)


async def main() -> None:
    '''Функция настройки(конфигурирования) и запуска бота'''

    # Настраиваем логгирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )
    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    # Загружаем конфигурацию в переменную config
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot = Bot(token=config.tg_bot.token,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))  # чтобы распознавать теги
    dp = Dispatcher()

    # Настраиваем главное меню бота
    await set_main_menu(bot)

    # Регистрация диспетчеров
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
