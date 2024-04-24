from aiogram.fsm.state import StatesGroup, State

class Gen(StatesGroup):
    choosing_theme = State()
    choosing_number_of_variants = State()
    generating_variant = State()
    getting_answer = State()
    next_or_get_answer = State()
    one_more_time_or_answer = State()