from aiogram import Router, types
from aiogram.filters import Command
from keyboards.inline_menu import inline_menu
from data.help import HELP_TEXT

router = Router()

@router.message(Command("help"))
async def send_help(message: types.Message):
    await message.answer(HELP_TEXT)