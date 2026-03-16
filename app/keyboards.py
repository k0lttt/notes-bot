from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardButton, InlineKeyboardMarkup)

main = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Создать напоминание", callback_data="not_create"),
                                      InlineKeyboardButton(text="Изменить напоминание", callback_data="not_change"), 
                                      InlineKeyboardButton(text="Закончить напоминание", callback_data="not_finish"),],
                                     [InlineKeyboardButton(text="Просмотреть напоминания", callback_data="not_view")],
                                     [InlineKeyboardButton(text="Поддержка", callback_data="not_help"), 
                                      InlineKeyboardButton(text="Справка", callback_data="not_info")],
                                    ])

spravka = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Что умеет бот?", callback_data = "info_wd"),
                                                 InlineKeyboardButton(text="О проекте", callback_data = "info_project")], 
                                                 [InlineKeyboardButton(text = "Выход", callback_data = "info_back")]
                                                ])

back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Назад", callback_data = "not_info")]]
    )