from aiogram import F, Router, Bot
import asyncio
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ChatAction
from aiogram.fsm.context import FSMContext

from app.database.requests import set_user
from app.database.requests import update_user

from . import keyboards as kb
from .states import Crt

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
        await state.set_state('reg_name')
    else:
        await message.answer(
            f'🤝 Добро пожаловать, {message.from_user.full_name}! \n Я Notes-bot! Я буду напоминать тебе о важных для тебя событиях, стоит тебе только создать напоминание. Для начала работы нажми на "Создать Напоминание"', 
            reply_markup=kb.main
        )

@user.message(StateFilter('reg_name'))
async def get_reg_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text.capitalize)
    data = await state.get_data()
    await update_user(message.from_user.id, 
                    data['name'])
    await message.answer('Регистрация прошла успешно!', 
                        reply_markup=kb.main)

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
        f'👋 Привет, {callback.from_user.full_name}! \n Я Notes-bot! Я буду напоминать тебе о важных для тебя событиях, стоит тебе только создать напоминание. Для начала работы нажми на "Создать Напоминание"', 
        reply_markup=kb.main
    )


@user.message(Command("create"))
async def cmd_crt(message: Message, state: FSMContext):
    await state.set_state(Crt.notes_name)
    await message.answer("Как будет называться напоминание?")

@user.message(Crt.notes_name)
async def cmd_crt_notesname(message: Message, state: FSMContext):
    await state.update_data(notes_name=message.text)
    await state.set_state(Crt.notes_time)
    await message.answer("Введите время напоминания")

@user.message(Crt.notes_time)
async def cmd_crt_notestime(message: Message, state: FSMContext):
    await state.update_data(notes_time=message.text)
    await state.set_state(Crt.notes_time)
    data = await state.get_data()
    await message.answer(f"Создано напоминание: \n{data['notes_name']} - {data['notes_time']}")
