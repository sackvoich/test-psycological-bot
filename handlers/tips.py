from aiogram import Router, types
from data.tips import TIPS_TEXT
from aiogram.filters import Command
from keyboards.inline_menu import inline_menu

router = Router()

@router.message(Command("tips"))
async def send_tips(message: types.Message):
    await message.answer(TIPS_TEXT)
