import sqlite3

class DBBaseManager:
    def __init__(self) -> None:
        self.db = get_db()

    def _get_rows(self, table_name: str) -> list[dict]:
        self.db.row_factory = sqlite3.Row

        rows = self.db.execute(
            f"SELECT * FROM {table_name}"
        ).fetchall()

        return [dict(row) for row in rows]

    def _insert_row(self, table_name: str, row: dict[str, str]) -> None:
        columns = ", ".join(row.keys())
        placeholders = ", ".join(f":{key}" for key in row)

        sql = (
            f"INSERT INTO {table_name} "
            f"({columns}) "
            f"VALUES ({placeholders})"
        )

        self.db.execute(sql, row)
        self.db.commit()

def get_db() -> sqlite3.Connection:
    db_name = "database.db"
    db = sqlite3.connect(db_name)
    db.row_factory = sqlite3.Row
    return db