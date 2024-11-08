from aiogram import Router, types
from data.resources import RESOURCES_TEXT
from aiogram.filters import Command
from keyboards.inline_menu import inline_menu

router = Router()

@router.message(Command("resources"))
async def send_resources(message: types.Message):
    await message.answer(RESOURCES_TEXT, disable_web_page_preview=True)
