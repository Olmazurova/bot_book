from aiogram.types import User
from aiogram_dialog import DialogManager

from database.database import users_db
from services.file_handling import book

async def get_page(
        dialog_manager: DialogManager, event_from_user: User, **kwargs
):
    page = users_db[event_from_user.id]['page']
    text_page = book[page]
    return {
        'page': page,
        'all_count': len(book),
        'text_page': text_page,
    }


async def get_bookmarks(
        dialog_manager: DialogManager, event_from_user: User, **kwargs
):
    bookmarks = [
        (page, book[page])
        for page in sorted(users_db[event_from_user.id]['bookmarks'])
    ]
    return {
        'bookmarks': bookmarks,
        'lack_bookmarks': len(bookmarks) == 0,
    }
