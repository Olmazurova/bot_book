from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON
from services.file_handling import book


def create_bookmarks_keyboard(*args: int) -> InlineKeyboardMarkup:
    """Функция, генерирующая список закладок в виде инлайн-кнопок
    + кнопки 'Редактировать' и 'Отменить'"""
    kb_builder = InlineKeyboardBuilder()
    # Наполняем конструктор кнопками из переданных аргументов
    for button in sorted(args):
        kb_builder.row(InlineKeyboardButton(
            text=f'{button} - {book[button][:100]}',
            callback_data=str(button)
        ))

    kb_builder.row(
        InlineKeyboardButton(
            text=LEXICON['edit_bookmarks_button'],
            callback_data='edit_bookmarks'
        ),
        InlineKeyboardButton(
            text=LEXICON['cancel'],
            callback_data='cancel'
        ),
        width=2
    )

    return kb_builder.as_markup()


def create_edit_keyboard(*args: int) -> InlineKeyboardMarkup:
    """Функция генерирует список закладок к удалению + кнопку 'Отменить'"""
    kb_builder = InlineKeyboardBuilder()

    # Наполняем клавиатуру кнопками-закладками в порядке возрастания
    for button in sorted(args):
        kb_builder.row(InlineKeyboardButton(
            text=f'{LEXICON['del']} {button} - {book[button][:100]}',
            callback_data=f'{button}del'
        ))

    # Добавляем в конец клавиатуры кнопку Отменить
    kb_builder.row(InlineKeyboardButton(
        text=LEXICON['cancel'],
        callback_data='cancel'
    ))

    return kb_builder.as_markup()
