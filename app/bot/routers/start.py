from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from app.bot.keyboards.menu import webapp_kb

router = Router()

@router.message(CommandStart())
async def start(m: Message):
    cfg = m.bot.get("config")
    await m.answer("Привет! Открой ежедневник 👇", reply_markup=webapp_kb(cfg.webapp_url))
