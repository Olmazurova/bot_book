from aiogram import Router
from aiogram.types import Message


other_router = Router()


@other_router.message()
async def send_unknown_command(message: Message):
    """Хендлер будет срабатывать на все сообщения,
    не отловленные другими хендлерами."""
    await message.answer(f'Мне неизвестна команда {message.text}')
