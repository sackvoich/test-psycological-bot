from aiogram.fsm.state import StatesGroup, State

class ChatState(StatesGroup):
    START = State()
    CHAT = State()
    END = State()