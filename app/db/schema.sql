PRAGMA journal_mode=WAL;
PRAGMA synchronous=NORMAL;
PRAGMA foreign_keys=ON;

CREATE TABLE IF NOT EXISTS users (
  tg_id       INTEGER PRIMARY KEY,
  username    TEXT,
  first_name  TEXT,
  last_name   TEXT,
  created_at  INTEGER NOT NULL,
  updated_at  INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS tasks (
  id          TEXT NOT NULL,
  tg_id       INTEGER NOT NULL,
  date        TEXT NOT NULL,            -- YYYY-MM-DD
  title       TEXT NOT NULL DEFAULT '',
  desc        TEXT NOT NULL DEFAULT '',
  start_time  TEXT NOT NULL DEFAULT '', -- HH:MM
  end_time    TEXT NOT NULL DEFAULT '',
  done        INTEGER NOT NULL DEFAULT 0,
  priority    TEXT NOT NULL DEFAULT 'green',
  created_at  INTEGER NOT NULL,
  updated_at  INTEGER NOT NULL,
  deleted     INTEGER NOT NULL DEFAULT 0,
  PRIMARY KEY (tg_id, id),
  FOREIGN KEY (tg_id) REFERENCES users(tg_id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_tasks_user_date ON tasks(tg_id, date);
CREATE INDEX IF NOT EXISTS idx_tasks_user_date_del ON tasks(tg_id, date, deleted);
