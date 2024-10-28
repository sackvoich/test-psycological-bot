import logging
from aiogram import Router, F
from aiogram.types import CallbackQuery
from data.resources import RESOURCES_TEXT
from data.tips import TIPS_TEXT
from data.contact import CONTACT_TEXT

router = Router()

@router.callback_query(F.data == "resources")
async def callback_resources(callback: CallbackQuery):
    logging.debug(f"Received callback data: {callback.data}")
    await callback.message.answer(RESOURCES_TEXT, disable_web_page_preview=True)
    await callback.answer()

@router.callback_query(F.data == "tips")
async def callback_tips(callback: CallbackQuery):
    logging.debug(f"Received callback data: {callback.data}")
    await callback.message.answer(TIPS_TEXT)
    await callback.answer()

@router.callback_query(F.data == "contact")
async def callback_contact(callback: CallbackQuery):
    logging.debug(f"Received callback data: {callback.data}")
    await callback.message.answer(CONTACT_TEXT, disable_web_page_preview=True)
    await callback.answer()

@router.callback_query(F.data == "mood")
async def callback_mood(callback: CallbackQuery):
    logging.debug(f"Received callback data: {callback.data}")
    from handlers.mood import mood_keyboard
    await callback.message.answer("Как ты себя чувствуешь сегодня?", reply_markup=mood_keyboard)
    await callback.answer()

@router.callback_query(F.data == "help")
async def callback_help(callback: CallbackQuery):
    logging.debug(f"Received callback data: {callback.data}")
    help_text = (
        "Вот как я могу помочь:\n\n"
        "/resources - Полезные ресурсы и контакты служб поддержки\n"
        "/tips - Советы по улучшению психического здоровья\n"
        "/contact - Связаться с психологом университета\n"
        "/mood - Поделиться своим настроением\n"
        "/exit - Завершить разговор\n\n"
        "Помни, что я не заменяю профессиональную помощь, но всегда готов выслушать."
    )
    await callback.message.answer(help_text)
    await callback.answer()
