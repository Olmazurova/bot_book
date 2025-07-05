from aiogram import Router
from aiogram.types import Message

other_router = Router()


@other_router.message()
async def send_unknown_command(message: Message):
    """
    Обработка всех сообщений,
    не отловленных другими хендлерами.
    """
    await message.answer(f'Мне неизвестна команда {message.text}')
