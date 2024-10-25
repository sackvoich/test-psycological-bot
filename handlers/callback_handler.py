from aiogram import Router, types
from aiogram.types import CallbackQuery

router = Router()

@router.callback_query(lambda callback: callback.data == "resources")
async def callback_resources(callback: CallbackQuery):
    await callback.message.answer("Полезные ресурсы и контакты служб поддержки: ...")

@router.callback_query(lambda callback: callback.data == "tips")
async def callback_tips(callback: CallbackQuery):
    await callback.message.answer("Советы по улучшению психического здоровья: ...")

@router.callback_query(lambda callback: callback.data == "contact")
async def callback_contact(callback: CallbackQuery):
    await callback.message.answer("Контакты психолога: ...")

@router.callback_query(lambda callback: callback.data == "mood")
async def callback_mood(callback: CallbackQuery):
    await callback.message.answer("Как вы себя чувствуете сегодня? Пожалуйста, напишите ваше настроение.")

@router.callback_query(lambda callback: callback.data == "help")
async def callback_help(callback: CallbackQuery):
    await callback.message.answer("Вот как я могу помочь: ...")
