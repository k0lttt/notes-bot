from aiogram.fsm.state import State, StatesGroup

class NoticeStates(StatesGroup):
    notes_name = State()
    notes_time = State()
    reg_timezone = State()
    reg_name = State()