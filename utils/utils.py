from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.common import Whenable

from services.file_handling import book

def is_not_first_page(data: dict, widget: Whenable, manager: DialogManager):
    """Проверяет, что не первая страница книги."""
    return data.get('page') != 1


def is_not_last_page(data: dict, widget: Whenable, manager: DialogManager):
    """Проверяет, что не последняя страница книги."""
    return data.get('page') != len(book)
