import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

def _csv_ints(v: str) -> list[int]:
    return [int(x.strip()) for x in (v or "").split(",") if x.strip().isdigit()]

@dataclass(frozen=True)
class Config:
    bot_token: str
    webapp_url: str
    db_path: str
    admin_ids: list[int]

def load_config() -> Config:
    return Config(
        bot_token=os.getenv("BOT_TOKEN", "").strip(),
        webapp_url=os.getenv("WEBAPP_URL", "").strip().rstrip("/"),
        db_path=os.getenv("DB_PATH", "./data/app.db").strip(),
        admin_ids=_csv_ints(os.getenv("ADMIN_IDS", "")),
    )
