from copy import deepcopy

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, StartMode

from database.database import user_dict_template, users_db
from dialog.states import StartSG, BookmarksSG
from filters.filters import IsDelBookmarkCallbackData, IsDigitalCallbackData
from keyboards.bookmarks_kb import (create_bookmarks_keyboard,
                                    create_edit_keyboard)
from keyboards.pagination_kb import create_pagination_keyboard
from lexicon.lexicon import LEXICON
from services.file_handling import book


user_router = Router()


@user_router.message(CommandStart())
async def process_command_start(message: Message, dialog_manager: DialogManager):
    """
    Хендлер, срабатывающий на кнопку /start.
    Отправляет приветственное сообщение и
    добавляет пользователя в БД, если его там нет.
    """
    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = deepcopy(user_dict_template)
    await dialog_manager.start(state=StartSG.start, mode=StartMode.RESET_STACK)


@user_router.message(Command(commands='help'))
async def process_command_help(message: Message, dialog_manager: DialogManager):
    """Хендлер, срабатывающий на команду /help.
    Отправляет пользователю сообщение со списком всех команд бота.
    """
    await dialog_manager.start(state=StartSG.descript, mode=StartMode.RESET_STACK)


@user_router.message(Command(commands='beginning'))
async def process_command_beginning(message: Message, dialog_manager: DialogManager):
    """Хендлер, срабатывающий на команду /beginning.
    Отправляет пользователю первую страницу книги с кнопками пагинации.
    """
    users_db[message.from_user.id]['page'] = 1  # назначаем текущей страницей первую
    await dialog_manager.start(state=StartSG.read, mode=StartMode.RESET_STACK)


@user_router.message(Command(commands='continue'))
async def process_command_continue(message: Message, dialog_manager: DialogManager):
    """Хендлер, срабатывающий на команду /continue.
    Отправляет пользователю страницу книги, на которой
    он остановился в процессе взаимодействия с ботом."""
    await dialog_manager.start(state=StartSG.read, mode=StartMode.RESET_STACK)


@user_router.message(Command(commands='bookmarks'))
async def process_command_bookmarks(message: Message,  dialog_manager: DialogManager):
    """Хендлер, срабатывающий на команду /bookmarks.
    Отправляет пользователю список закладое, если он есть,
    или сообщение о том, что закладок нет.
    """
    await dialog_manager.start(state=BookmarksSG.bookmarks)


# @router.callback_query(F.data == 'forward')
# async def process_press_forward(callback: CallbackQuery):
#     """Хедлер, срабатывающий на нажание кнопки вперёд."""
#     if users_db[callback.from_user.id]['page'] < len(book):
#         users_db[callback.from_user.id]['page'] += 1
#         text = book[users_db[callback.from_user.id]['page']]
#         await callback.message.edit_text(
#             text=text,
#             reply_markup=create_pagination_keyboard(
#                 'backward',
#                 f'{users_db[callback.from_user.id]["page"]}/{len(book)}',
#                 'forward'
#             )
#         )
#     await callback.answer()


# @router.callback_query(F.data == 'backward')
# async def process_press_backward(callback: CallbackQuery):
#     """Хендлер, срабатывающий на нажание кнопки назад."""
#     if users_db[callback.from_user.id]['page'] > 1:
#         users_db[callback.from_user.id]['page'] -= 1
#         text = book[users_db[callback.from_user.id]['page']]
#         await callback.message.edit_text(
#             text=text,
#             reply_markup=create_pagination_keyboard(
#                 'backward',
#                 f'{users_db[callback.from_user.id]["page"]}/{len(book)}',
#                 'forward'
#             )
#         )
#     await callback.answer()


# @router.callback_query(lambda x: '/' in x.data
#                        and x.data.replace('/', '').isdigit())
# async def process_press_page(callback: CallbackQuery):
#     """Хендлер, добавляющий закладку в список закладок."""
#     users_db[callback.from_user.id]['bookmarks'].add(
#         users_db[callback.from_user.id]['page']
#     )
#     await callback.answer(text='Страница добавлена в закладки!')


# @router.callback_query(IsDigitalCallbackData())
# async def process_press_bookmark(callback: CallbackQuery):
#     """Хендлер, срабатывающий на нажатие одной из закладок."""
#     text = book[int(callback.data)]
#     users_db[callback.from_user.id]['page'] = int(callback.data)
#     await callback.message.edit_text(
#         text=text,
#         reply_markup=create_pagination_keyboard(
#             'backward',
#             f'{users_db[callback.from_user.id]["page"]}/{len(book)}',
#             'forward'
#         )
#     )


# @router.callback_query(F.data == 'edit_bookmarks')
# async def process_press_edit(callback: CallbackQuery):
#     """Хендлер, срабатывающий на нажатие кнопки редактировать."""
#     await callback.message.edit_text(
#         text=LEXICON[callback.data],
#         reply_markup=create_edit_keyboard(
#             *users_db[callback.from_user.id]['bookmarks']
#         )
#     )


# @router.callback_query(F.data == 'cancel')
# async def process_press_cancel(callback: CallbackQuery):
#     """Хендлер, срабатывающий на нажатие кнопки отменить."""
#     await callback.message.edit_text(
#         text=LEXICON['cancel_text']
#     )


# @router.callback_query(IsDelBookmarkCallbackData())
# async def process_press_del_bookmark(callback: CallbackQuery):
#     """Хендлер, срабатывающий на нажатие закладки в режиме редактирования.
#     Удаляет закладку из списка.
#     """
#     users_db[callback.from_user.id]['bookmarks'].remove(
#         int(callback.data[:-3])
#     )
#     if users_db[callback.from_user.id]['bookmarks']:
#         await callback.message.edit_text(
#             text=LEXICON['/bookmarks'],
#             reply_markup=create_edit_keyboard(
#                 *users_db[callback.from_user.id]['bookmarks']
#             )
#         )
#     else:
#         await callback.message.edit_text(text=LEXICON['no_bookmarks'])
