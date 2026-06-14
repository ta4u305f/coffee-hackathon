import sqlite3
from db_database import get_db, DBBaseManager

class RosterDBManager(DBBaseManager):
    def __init__(self):
        super().__init__()
        self._roaster_db_name = "roasters"

    def create_user(self, user_data: dict[str, str]) -> None:
        self._insert_row(self._roaster_db_name, user_data)

    def get_all_user(self) -> list[dict[str, str]]:
        return self._get_rows(self._roaster_db_name)


# if __name__ == "__main__":
#     data ={
#         "company_name": "株式会社サンプルテック",
#         "company_name_kana": "サンプルテック",
#         "contact_name": "山田 太郎",
#         "address": "東京都千代田区丸の内1-1-1",
#         "phone_number": "03-1234-5678",
#         "email": "yamada@example.co.jp",
#         "prefecture_id": "東京都",
#     }

#     rdbm = RosterDBManager()
#     rdbm.create_user(data)
#     print(rdbm.get_all_user())