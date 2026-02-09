# Planner (Bot + API + WebApp)

## Install
pip install -r requirements.txt

## Configure
Copy `.env.example` -> `.env` and fill values.

## Run API
uvicorn app.api.main:app --reload --port 8080

## Run Bot
python -m app.bot.main
