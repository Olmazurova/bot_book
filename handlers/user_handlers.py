from copy import deepcopy

from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from database.database import user_dict_template, users_db
from dialog.states import StartSG, BookmarksSG

user_router = Router()


@user_router.message(CommandStart())
async def process_command_start(
        message: Message, dialog_manager: DialogManager
):
    """
    Обработка команды /start.
    Стартует диалог чтения и добавляет пользователя в БД, если его там нет.
    """
    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = deepcopy(user_dict_template)
    await dialog_manager.start(state=StartSG.start, mode=StartMode.RESET_STACK)


@user_router.message(Command(commands='help'))
async def process_command_help(message: Message, dialog_manager: DialogManager):
    """
    Обработка команды /help.
    Открывает окно диалога справки о боте.
    """
    await dialog_manager.start(
        state=StartSG.descript, mode=StartMode.RESET_STACK
    )


@user_router.message(Command(commands='beginning'))
async def process_command_beginning(
        message: Message, dialog_manager: DialogManager
):
    """
    Обработка команды /beginning.
    Сбрасывает текущую страницу до 1 и
    открывает окно диалога чтения текущей страницы.
    """
    users_db[message.from_user.id]['page'] = 1
    await dialog_manager.start(state=StartSG.read, mode=StartMode.RESET_STACK)


@user_router.message(Command(commands='continue'))
async def process_command_continue(
        message: Message, dialog_manager: DialogManager
):
    """
    Обработка команды /continue.
    Открывает окно диалога чтения текущей страницы.
    """
    await dialog_manager.start(state=StartSG.read, mode=StartMode.RESET_STACK)


@user_router.message(Command(commands='bookmarks'))
async def process_command_bookmarks(
        message: Message,  dialog_manager: DialogManager
):
    """
    Обработка команды /bookmarks.
    Открывает окно диалога закладок.
    """
    await dialog_manager.start(state=BookmarksSG.bookmarks)
