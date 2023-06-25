from src.repository.sqlite.sqliterepo import SQLiteRepo


class InterestRepo(SQLiteRepo):
    def create(self, log: str, effort: int):
        self.cursor.execute(
            """ INSERT INTO interests (log, effort) VALUES (?, ?) """,
            (log, effort),
        )
        self.connection.commit()

        interest_id = self.cursor.lastrowid

        return interest_id

    def list(self):
        show_interests_query = """
            SELECT i.log, i.effort, GROUP_CONCAT(t.name, ',') 
            FROM interests i 
            LEFT JOIN interests_tags it ON i.id = it.interest_id 
            LEFT JOIN tags t ON it.tag_id = t.id GROUP BY i.id;
        """
        interests = self.cursor.execute(show_interests_query)

        rows = [row for row in interests]
        return rows
