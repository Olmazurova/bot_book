from aiogram import Bot
from aiogram.types import BotCommand
from lexicon.lexicon import LEXICON_COMMANDS


async def set_main_menu(bot: Bot):
    # Создаём список с командами и их описанием для кнопки menu
    main_menu_commands = [BotCommand(command=command, description=descript) 
                          for command, descript in LEXICON_COMMANDS.items()]

    await bot.set_my_commands(main_menu_commands)
