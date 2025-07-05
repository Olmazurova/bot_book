from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager

from database.database import users_db
from dialog.states import StartSG, BookmarksSG
from lexicon.lexicon import LEXICON


async def add_bookmarks(callback: CallbackQuery, dialog_manager: DialogManager):
    """Добавление закладки в список закладок."""
    users_db[callback.from_user.id]['bookmarks'].add(
        users_db[callback.from_user.id]['page']
    )
    await callback.answer(text=LEXICON['add_bookmark'])


async def delete_bookmark(callback: CallbackQuery, dialog_manager: DialogManager):
    """Удаление закладки из списка закладок."""
    users_db[callback.from_user.id]['bookmarks'].remove(
        int(callback.data.split(':')[1])
    )
    if users_db[callback.from_user.id]['bookmarks']:
        await dialog_manager.switch_to(state=BookmarksSG.edit)
