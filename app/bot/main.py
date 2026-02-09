import asyncio
from aiogram import Bot, Dispatcher
from app.common.config import load_config
from app.common.logging import setup_logging
from app.bot.routers.start import router as start_router

async def main():
    setup_logging("INFO")
    cfg = load_config()
    if not cfg.bot_token:
        raise RuntimeError("BOT_TOKEN is empty. Put it into .env")

    bot = Bot(token=cfg.bot_token)
    dp = Dispatcher()
    dp["config"] = cfg
    dp.include_router(start_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
