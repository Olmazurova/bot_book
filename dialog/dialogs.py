from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs, ShowMode
from aiogram_dialog.widgets.kbd import Button, Row, Column, Group, Select, Multiselect, Start, Next, Cancel
from aiogram_dialog.widgets.text import Const, Format, Multi, Case, List

from dialog.states import StartSG, BookmarksSG
from lexicon.lexicon import LEXICON, LEXICON_COMMANDS
from services.file_handling import book



start_dialog = Dialog(
    Window(
        Const(LEXICON['/start']),
        Row(
            Button(Const(LEXICON_COMMANDS['/read']), id='read', on_click=switch_to_read),
            Start(Const(LEXICON_COMMANDS['/bookmarks']), id='bookmarks'),
        ),
        Button(Const(LEXICON_COMMANDS['/help']), id='descript', on_click=switch_to_descript),
        state=StartSG.start,
        getter=get_page,
    ),
    Window(
        Const(LEXICON['/help']),
        Row(
            Button(Const(LEXICON_COMMANDS['/read']), id='read', on_click=switch_to_read),
            Start(Const(LEXICON_COMMANDS['/bookmarks']), id='bookmarks'),
        ),
        state=StartSG.descript,
        getter=get_page,
    ),
    Window(
        Format('{text}'),
        Row(
            Button(LEXICON_COMMANDS['/back'], id='back', on_click=previous_page),
            Button(Format('{page}/{all_count}'), id='page', on_click=add_bookmarks),
            Button(LEXICON_COMMANDS['/forward'], id='forward', on_click=forward_page),
        ),
        Start(Const(LEXICON_COMMANDS['/bookmarks']), id='bookmarks'),
        state=StartSG.read,
        getter=get_page,
    ),
)


bookmarks_dialog = Dialog(
    Window(
        Const(LEXICON['/bookmarks']),
        Column(
            Select(
                Format('{item[0]} - {item[1]}'),
                id='list_bookmarks',
                item_id_getter=lambda x: x[0],
                items='bookmarks',
                on_click=return_bookmark,
            ),
        ),
        Row(
            Next(Const(LEXICON_COMMANDS['/edit']), id='edit'),
            Cancel(Const(LEXICON_COMMANDS['/cancel']), id='cancel'),
        ),
        getter=get_bookmarks,
        state=BookmarksSG.bookmarks,
    ),
    Window(
        Const(LEXICON['edit_bookmarks']),
        Column(
            Select(
                Format('❌ {item[0]} - {item[1]}'),
                id='edit_bookmarks',
                item_id_getter=lambda x: x[0],
                items='bookmarks',
                on_click=delete_bookmark,
            ),
            Cancel(Const(LEXICON_['cancel']), id='cancel'),
        ),
        state=BookmarksSG.edit,
        getter=get_bookmarks,
    ),
)
