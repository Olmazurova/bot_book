from typing import Any

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button

from database.database import users_db
from dialog.states import StartSG

async def go_to_page(callback: CallbackQuery, widget: Any, dialog_manager: DialogManager, item_id: str):
    users_db[callback.from_user.id]['page'] = int(item_id)
    await dialog_manager.start(state=StartSG.read, mode=StartMode.RESET_STACK)


async def previous_page(callback: CallbackQuery, button: Button, dialog_manager: DialogManager, **kwargs):
    """Переключение на предыдущую страницу книги."""
    page = users_db[callback.from_user.id]['page'] - 1
    users_db[callback.from_user.id]['page'] = page
    await dialog_manager.switch_to(state=StartSG.read)


async def forward_page(callback: CallbackQuery, button: Button, dialog_manager: DialogManager, **kwargs):
    """Переключение на следующую страницу книги."""
    page = users_db[callback.from_user.id]['page'] + 1
    users_db[callback.from_user.id]['page'] = page
    await dialog_manager.switch_to(state=StartSG.read)