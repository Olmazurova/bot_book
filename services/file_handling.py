import os
import sys


BOOK_PATH = 'book/book.txt'  # путь к файлу книги
PAGE_SIZE = 1050  # максимальное количество букв для одной страницы

book: dict[int, str] = {}


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    """Функция возвращает строку с текстом страницы и её размер."""
    pass


def prepare_book(path: str) -> None:
    """Функция формирует словарь книги"""
    pass


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
