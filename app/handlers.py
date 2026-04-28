from aiogram import F, Router, Bot
import asyncio
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.enums import ChatAction
from aiogram.fsm.context import FSMContext

from app.database.requests import (set_user, timezone_check, update_user, 
                                   get_title, timezone_update)


from . import states as st
from . import keyboards as kb

user = Router()


@user.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.bot.send_chat_action(chat_id=message.from_user.id, 
                                       action=ChatAction.TYPING)
    await asyncio.sleep(0.3)
    is_user = await set_user(message.from_user.id)
    if not is_user:
        await message.answer(
            f'👋 Привет! \n Пройдите процесс регестрации.. \n\n Введите ваше имя..✍️', 
            reply_markup=await kb.client_name(message.from_user.first_name)
        )
        await state.set_state(st.NoticeStates.reg_name)
    else:
        await message.answer(
            f'🤝 Добро пожаловать, {message.from_user.full_name}! \n Я Notes-bot! Я буду напоминать тебе о важных для тебя событиях, стоит тебе только создать напоминание. Для начала работы нажми на "Создать Напоминание"', 
            reply_markup=kb.main
        )

@user.message(st.NoticeStates.reg_name)
async def get_reg_name(message: Message, state: FSMContext):
    await state.update_data(user_name=message.text.capitalize())
    data = await state.get_data()
    await update_user(message.from_user.id,
                      data['user_name'])
    await message.answer('Регистрация пройдена успешно!', 
                        reply_markup = ReplyKeyboardRemove())
    await message.answer(
            f'🤝 Добро пожаловать, {message.from_user.full_name}! \n Я Notes-bot! Я буду напоминать тебе о важных для тебя событиях, стоит тебе только создать напоминание. Для начала работы нажми на "Создать Напоминание"', 
            reply_markup=kb.main

        )
    
    await state.clear()

@user.callback_query(F.data == "not_create")
async def cmd_notcreate(callback: CallbackQuery, state: FSMContext):
    await callback.answer("")
    is_timezone = await timezone_check(callback.from_user.id)
    if is_timezone:
        await callback.message.edit_text("Перед созданием напоминания укажите свой часовой пояс: \n \n(Укажите в формате + к  МСК) \n Например если вы из Москвы, напишите +0, \n а если вы из Екатеринбурга, напишите +2")
        
        await state.set_state(st.NoticeStates.reg_timezone)
    else:
        await callback.message.edit_text("Для создания напоминания напишите его название.. : \n\n", 
                                    reply_markup=kb.create_not)
    

@user.message(StateFilter(st.NoticeStates.reg_timezone))
async def new_timezone(message: Message, state: FSMContext):
    await state.update_data(new_timezone=message.text.capitalize())
    timezone_new = await state.get_data()
    await timezone_update(message.from_user.id,
                       timezone_new['new_timezone'])
    await message.answer('Часовой пояс обновлен!',
                         reply_markup=kb.create_not)
    
    await state.set_state(st.NoticeStates.notes_name)

@user.message(StateFilter(st.NoticeStates.notes_name))
async def not_name(message: Message, State: FSMContext):
    pass

@user.callback_query(F.data == "back_crnot")
async def cmd_back(callback: CallbackQuery):
    await callback.message.edit_text(
        f'🤝 Добро пожаловать, {callback.from_user.full_name}! \n Я Notes-bot! Я буду напоминать тебе о важных для тебя событиях, стоит тебе только создать напоминание. Для начала работы нажми на "Создать Напоминание"', 
            reply_markup=kb.main
            )

@user.message(StateFilter(st.NoticeStates.notes_name))
async def get_nameofnot(message: Message, state: FSMContext):
    await state.update_data(title=message.text.capitalize())
    data = await state.get_data()
    await get_title(message.from_user.id,
                      data['title'])

    

@user.callback_query(F.data == "not_info")
async def cmd_how(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.edit_text(
        "🔎 Справочный материал:",
        reply_markup=kb.spravka
    )

@user.callback_query(F.data == "info_wd")
async def cmd_skill(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.edit_text('🤖 Бот, который помнит за вас \n\n Отправьте мне сообщение и время — я верну его вам, когда наступит нужный момент. 📢 \n\nБольше никаких "ой, забыл" — только точность и забота о ваших делах.✅', 
                                     reply_markup=kb.sp_back)

@user.callback_query(F.data == "info_project")
async def cmd_skill(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.edit_text("Бот разработан в образовательных целях. Весь исходный код открыт и доступен в репозитории: \n\n 🔗 GitHub: <a href='https://github.com/k0lttt'>GitHub</a>!\n\n 🍩 Донат на кофе: jopa",
                                     reply_markup=kb.sp_back,
                                     parse_mode="HTML")
@user.callback_query(F.data == "info_back")
async def cmd_how(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.edit_text(
        f'🤝 Добро пожаловать, {callback.from_user.full_name}! \n Я Notes-bot! Я буду напоминать тебе о важных для тебя событиях, стоит тебе только создать напоминание. Для начала работы нажми на "Создать Напоминание"', 
            reply_markup=kb.main
            )

