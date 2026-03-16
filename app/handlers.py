from aiogram import F, Router, Bot
import asyncio
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ChatAction
from aiogram.fsm.context import FSMContext

from . import keyboards as kb
from .states import Crt

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id, 
                                       action=ChatAction.TYPING)
    await asyncio.sleep(0.5)
    await message.answer(
        f"Привет, {message.from_user.full_name}! Я твой бот помощник! Я буду напоминать тебе о важных событиях.", 
        reply_markup=kb.main
    )

@router.callback_query(F.data == "not_info")
async def cmd_how(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.edit_text(
        "Справка: ",
        reply_markup=kb.spravka
    )

@router.callback_query(F.data == "info_wd")
async def cmd_skill(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.edit_text("Бот создан для того, чтобы напоминать вам о событиях.", 
                                     reply_markup=kb.sp_back)

@router.callback_query(F.data == "info_project")
async def cmd_skill(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.edit_text("Бот создан как учебный проект.\n Информация об авторе: \n github: https://github.com/k0lttt \n Донат: jopa",
                                     reply_markup=kb.sp_back)

@router.callback_query(F.data == "info_back")
async def cmd_how(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.edit_text(
        f"Привет, {callback.from_user.full_name}! Я твой бот помощник! Я буду напоминать тебе о важных событиях.", 
        reply_markup=kb.main
    )


@router.message(Command("create"))
async def cmd_crt(message: Message, state: FSMContext):
    await state.set_state(Crt.notes_name)
    await message.answer("Как будет называться напоминание?")

@router.message(Crt.notes_name)
async def cmd_crt_notesname(message: Message, state: FSMContext):
    await state.update_data(notes_name=message.text)
    await state.set_state(Crt.notes_time)
    await message.answer("Введите время напоминания")

@router.message(Crt.notes_time)
async def cmd_crt_notestime(message: Message, state: FSMContext):
    await state.update_data(notes_time=message.text)
    await state.set_state(Crt.notes_time)
    data = await state.get_data()
    await message.answer(f"Создано напоминание: \n{data['notes_name']} - {data['notes_time']}")
