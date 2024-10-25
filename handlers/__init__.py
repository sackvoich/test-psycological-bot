from .start import router as start_router
from .help import router as help_router
from .resources import router as resources_router
from .tips import router as tips_router
from .contact import router as contact_router
from .mood import router as mood_router
from .callback_handler import router as callback_router

def register_handlers(dp):
    dp.include_router(start_router)
    dp.include_router(help_router)
    dp.include_router(resources_router)
    dp.include_router(tips_router)
    dp.include_router(contact_router)
    dp.include_router(mood_router)
    dp.include_router(callback_router)
