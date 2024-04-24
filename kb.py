from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


main_menu = [
    [KeyboardButton(text="Выбор темы", callback_data="сhoose_theme")],
    [KeyboardButton(text="Хз не придумал", callback_data="idk")],
]

right_answer_choice = [
    [KeyboardButton(text="Следующее", callback_data="next")],
    [KeyboardButton(text="Показать решение", callback_data="show_soulution")],
]

next_step = [
    [KeyboardButton(text="Следующее", callback_data="next")],
]

fault = [
    [KeyboardButton(text="Попробовать еще раз", callback_data="one_more_time")],
    [KeyboardButton(text="Показать решение", callback_data="show_solution")],
]


main_menu = ReplyKeyboardMarkup(keyboard=main_menu, resize_keyboard=True)

right_answer_choice = ReplyKeyboardMarkup(keyboard=right_answer_choice, resize_keyboard=True)

next_step = ReplyKeyboardMarkup(keyboard=next_step, resize_keyboard=True)

fault = ReplyKeyboardMarkup(keyboard=fault, resize_keyboard=True)
