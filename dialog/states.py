from aiogram.fsm.state import State, StatesGroup


class StartSG(StatesGroup):
    start = State()
    descript = State()
    read = State()


class BookmarksSG(StatesGroup):
    bookmarks = State()
    edit = State()
