from aiogram import Router, types
from aiogram.filters import Command
from keyboards.inline_menu import inline_menu

router = Router()

@router.message(Command(commands=['help']))
async def send_help(message: types.Message):
    help_text = (
        "Вот как я могу помочь:\n\n"
        "/resources - Полезные ресурсы и контакты служб поддержки\n"
        "/tips - Советы по улучшению психического здоровья\n"
        "/contact - Связаться с психологом университета\n"
        "/mood - Поделиться своим настроением\n"
        "/exit - Завершить разговор\n\n"
        "Помни, что я не заменяю профессиональную помощь, но всегда готов выслушать."
    )
    await message.answer(help_text, reply_markup=inline_menu)
