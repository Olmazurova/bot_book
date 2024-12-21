from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON


def create_pagination_keyboard(*buttons: str) -> InlineKeyboardMarkup:
    """Функция, генерирующая клавиатуру для страницы книги."""
    # Инициализируем конструктор клавиатуры
    kb_builder = InlineKeyboardBuilder()
    # Добавляем в конструтор ряд с кнопками
    kb_builder.row(*[InlineKeyboardButton(
                         text=LEXICON[button] if button in LEXICON else button,
                         callback_data=button)
                     for button in buttons])
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()
