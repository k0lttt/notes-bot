from aiogram.fsm.state import State, StatesGroup

class Crt(StatesGroup):
    notes_name = State()
    notes_time = State()