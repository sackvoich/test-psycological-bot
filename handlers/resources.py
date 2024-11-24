from aiogram import Router, types
from data.resources import RESOURCES_TEXT
from aiogram.filters import Command
from keyboards.menu_keyboards import back_to_menu_keyboard # Импортируем клавиатуру

router = Router()

@router.message(Command("resources"))
async def send_resources(message: types.Message):
    await message.answer(RESOURCES_TEXT, disable_web_page_preview=True, reply_markup=back_to_menu_keyboard)
