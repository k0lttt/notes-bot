from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardButton, InlineKeyboardMarkup)

main = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="📝 Создать напоминание", callback_data="not_create"),
                                      InlineKeyboardButton(text="⚙️ Изменить напоминание", callback_data="not_change")], 
                                      [InlineKeyboardButton(text="✅️ Закончить напоминание", callback_data="not_finish"),
                                     InlineKeyboardButton(text="📅 Просмотреть напоминания", callback_data="not_view")],
                                     [InlineKeyboardButton(text="🛠️ Поддержка", url="https://t.me/ross789"), 
                                      InlineKeyboardButton(text="ℹ️ Справка", callback_data="not_info")],
                                    ])

spravka = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="❔ Что умеет бот?", callback_data = "info_wd"),
                                                 InlineKeyboardButton(text="📜 О проекте", callback_data = "info_project")], 
                                                 [InlineKeyboardButton(text = "⬅️ Назад", callback_data = "info_back")]
                                                ])

sp_back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬅️ Назад", callback_data = "not_info")]]
    )

create_not = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬅️ Назад", callback_data = "back_crnot")]
])


go_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬅️ Назад", callback_data = "go_main")]]
    )


async def client_name(name):
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=name)]],
                               resize_keyboard=True,
                               input_field_placeholder='Введите имя или оставьте такое же..')