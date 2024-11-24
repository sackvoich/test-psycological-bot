from aiogram import Router, types
from data.tips import TIPS_TEXT
from aiogram.filters import Command
from keyboards.menu_keyboards import back_to_menu_keyboard # Импортируем клавиатуру

router = Router()

@router.message(Command("tips"))
async def send_tips(message: types.Message):
    await message.answer(TIPS_TEXT, disable_web_page_preview=True, reply_markup=back_to_menu_keyboard)
