from aiogram import Router
from .start import router as start_router
from .help import router as help_router
from .resources import router as resources_router
from .tips import router as tips_router
from .contact import router as contact_router
from .mood import router as mood_router
from .callback_handler import router as callback_router
from .menu import router as menu_router
from .chat import router as chat_router  # Зарегистрируем чат в самом конце

router = Router()

def register_handlers(dp):
    dp.include_router(start_router)
    dp.include_router(help_router)
    dp.include_router(resources_router)
    dp.include_router(tips_router)
    dp.include_router(contact_router)
    dp.include_router(mood_router)  # mood_router должен быть зарегистрирован раньше
    dp.include_router(callback_router)
    dp.include_router(menu_router)
    dp.include_router(chat_router)

