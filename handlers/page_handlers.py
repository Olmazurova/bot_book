from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager

from database.database import users_db
from dialog.states import StartSG


async def previous_page(callback: CallbackQuery, dialog_manager: DialogManager):
    """Переключение на предыдущую страницу книги."""
    page = users_db[callback.from_user.id]['page'] - 1
    users_db[callback.from_user.id]['page'] = page
    await dialog_manager.switch_to(state=StartSG.read)


async def forward_page(callback: CallbackQuery, dialog_manager: DialogManager):
    """Переключение на следующую страницу книги."""
    page = users_db[callback.from_user.id]['page'] + 1
    users_db[callback.from_user.id]['page'] = page
    await dialog_manager.switch_to(state=StartSG.read)