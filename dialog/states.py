from aiogram.fsm.state import State, StatesGroup


class StartSG(StatesGroup):
    """Состояния стартового диалога чтения."""

    start = State()
    descript = State()
    read = State()


class BookmarksSG(StatesGroup):
    """Состояния диалога закладок."""

    bookmarks = State()
    edit = State()
