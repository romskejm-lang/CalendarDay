from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

def webapp_kb(webapp_url: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="Открыть ежедневник", web_app=WebAppInfo(url=webapp_url))
    ]])
