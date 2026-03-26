from aiogram import F, Router, Bot
import asyncio
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ChatAction
from aiogram.fsm.context import FSMContext

from . import keyboards as kb
from .states import Crt

admin = Router()