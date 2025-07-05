from aiogram_dialog import Dialog, StartMode, Window, ShowMode
from aiogram_dialog.widgets.kbd import (
    Button, Row, Column, Select, Start, Next, Cancel, SwitchTo
)
from aiogram_dialog.widgets.text import Const, Format

from dialog.getters import get_bookmarks, get_page
from dialog.states import StartSG, BookmarksSG
from handlers.bookmark_handlers import add_bookmarks, delete_bookmark
from handlers.page_handlers import forward_page, previous_page
from lexicon.lexicon import LEXICON, LEXICON_COMMANDS


start_dialog = Dialog(
    Window(
        Const(LEXICON['/start']),
        Row(
            SwitchTo(Const(LEXICON_COMMANDS['/read']), id='read', state=StartSG.read),
            Start(Const(LEXICON_COMMANDS['/bookmarks']), id='bookmarks'),
        ),
        Next(Const(LEXICON_COMMANDS['/help']), id='descript'),
        state=StartSG.start,
        getter=get_page,
    ),
    Window(
        Const(LEXICON['/help']),
        Row(
            Next(Const(LEXICON_COMMANDS['/read']), id='read'),
            Start(Const(LEXICON_COMMANDS['/bookmarks']), id='bookmarks'),
        ),
        state=StartSG.descript,
        getter=get_page,
    ),
    Window(
        Format('{text}'),
        Row(
            Button(LEXICON_COMMANDS['/back'], id='back', on_click=previous_page, when='page' != 1),
            Button(Format('{page}/{all_count}'), id='page', on_click=add_bookmarks),
            Button(LEXICON_COMMANDS['/forward'], id='forward', on_click=forward_page, when='page' != 'all_count'),
        ),
        Start(Const(LEXICON_COMMANDS['/bookmarks']), id='bookmarks'),
        state=StartSG.read,
        getter=get_page,
    ),
)


bookmarks_dialog = Dialog(
    Window(
        Const(LEXICON['/bookmarks'], when='bookmarks'),
        Const(LEXICON['no_bookmarks'], when='lack_bookmarks'),
        Column(
            Select(
                Start(
                    Format('{item[0]} - {item[1]}'),
                    id='get_bookmark',
                    state=StartSG.read,
                    mode=StartMode.RESET_STACK,
                ),
                id='list_bookmarks',
                item_id_getter=lambda x: x[0],
                items='bookmarks',
            ),
            when='bookmarks',
        ),
        Row(
            Next(Const(LEXICON_COMMANDS['/edit']), id='edit', when='bookmarks'),
            Cancel(Const(LEXICON_COMMANDS['/cancel']), id='cancel'),
        ),
        getter=get_bookmarks,
        state=BookmarksSG.bookmarks,
    ),
    Window(
        Const(LEXICON['edit_bookmarks'], when='bookmarks'),
        Const(LEXICON['no_bookmarks'], when='lack_bookmarks'),
        Column(
            Select(
                Format('❌ {item[0]} - {item[1]}'),
                id='edit_bookmarks',
                item_id_getter=lambda x: x[0],
                items='bookmarks',
                on_click=delete_bookmark,
                when='bookmarks',
            ),
            Cancel(Const(LEXICON['cancel']), id='cancel'),
        ),
        state=BookmarksSG.edit,
        getter=get_bookmarks,
    ),
)
