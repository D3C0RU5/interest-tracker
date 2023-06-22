import sqlite3


class SQLiteRepo:
    def __init__(self):
        self.connection = sqlite3.connect("interest_tracker.db")
        self.cursor = self.connection.cursor()
        self.__create_tables()

    def __create_tables(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS interests(id INTEGER PRIMARY KEY, log TEXT, effort INTEGER, created_at TEXT DEFAULT CURRENT_TIMESTAMP);"
        )
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS tags(id INTEGER PRIMARY KEY, name VARCHAR(255));"
        )
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS interests_tags (interest_id INTEGER, tag_id INTEGER, FOREIGN KEY(interest_id) REFERENCES interest, FOREIGN KEY(tag_id) REFERENCES tag);"
        )
