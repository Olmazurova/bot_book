import os
import sys


BOOK_PATH = 'book/Bredberi_Marsianskie-hroniki.txt'  # путь к файлу книги
PAGE_SIZE = 1050  # максимальное количество букв для одной страницы

book: dict[int, str] = {}


def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    """Функция возвращает строку с текстом страницы и её размер."""
    punctuation = ',.!;:?'
    result_text = ''
    if len(text[start:]) > page_size:
        curr_text = text[start:start + page_size]
        if text[start + page_size] in punctuation:
            curr_text = (curr_text[:-1]
                         if curr_text[-2] not in punctuation
                         else curr_text[:-2])
    else:
        curr_text = text[start:]
    for i, el in enumerate(curr_text[::-1], -len(curr_text)):
        if el in punctuation:
            result_text = curr_text[:-i]
            break
    return result_text, len(result_text)


def prepare_book(path: str) -> None:
    """Функция формирует словарь книги"""
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()
        count = 1
        start = 0
        while start < len(text):
            current_page, len_page = _get_part_text(text, start, PAGE_SIZE)
            if current_page:
                book[count] = current_page.lstrip(" \t\n")
                count += 1
                start += len_page
            else:
                break


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
