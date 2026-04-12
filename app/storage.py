from __future__ import annotations

import json
import sqlite3
from pathlib import Path


class Storage:
    def __init__(self, db_path: str = "data/alfa.db") -> None:
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(self.db_path))
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS corpses (id INTEGER PRIMARY KEY AUTOINCREMENT, data TEXT NOT NULL)"
        )
        self.conn.commit()

    def save(self, data: dict) -> None:
        self.conn.execute("INSERT INTO corpses (data) VALUES (?)", (json.dumps(data),))
        self.conn.commit()
