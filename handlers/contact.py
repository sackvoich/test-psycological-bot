from aiogram import Router, types
from data.contact import CONTACT_TEXT
from aiogram.filters import Command
from keyboards.inline_menu import inline_menu

router = Router()

@router.message(Command("contact"))
async def send_contact(message: types.Message):
    await message.answer(CONTACT_TEXT, disable_web_page_preview=True, reply_markup=inline_menu)
