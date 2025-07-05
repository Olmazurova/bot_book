from typing import Any

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from database.database import users_db
from dialog.states import BookmarksSG
from lexicon.lexicon import LEXICON


async def add_bookmarks(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    """Добавление закладки в список закладок."""
    users_db[callback.from_user.id]['bookmarks'].add(
        users_db[callback.from_user.id]['page']
    )
    await callback.answer(text=LEXICON['add_bookmark'])


async def delete_bookmark(callback: CallbackQuery, widget: Any, dialog_manager: DialogManager, item_id: str):
    """Удаление закладки из списка закладок."""
    users_db[callback.from_user.id]['bookmarks'].remove(
        int(callback.data.split(':')[1])
    )
    if users_db[callback.from_user.id]['bookmarks']:
        await dialog_manager.switch_to(state=BookmarksSG.edit)
