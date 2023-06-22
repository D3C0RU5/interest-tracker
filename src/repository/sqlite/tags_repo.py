from src.repository.sqlite.sqliterepo import SQLiteRepo


class TagsRepo(SQLiteRepo):
    def get_by_name(self, name):
        query = """SELECT id, name FROM tags WHERE name=?"""
        self.cursor.execute(query, (name,))

        tag = self.cursor.fetchone()

        if tag is None:
            return None

        return (tag[0], name)

    # __create_tags
    def create(self, name: str):
        self.cursor.execute("""INSERT INTO tags (name) VALUES (?)""", (name,))
        self.connection.commit()

        tag_id = self.cursor.lastrowid

        return tag_id

    def list(self, tags: list[str]):
        bind_params = ", ".join(["?"] * len(tags))
        escaped_query = f"SELECT id, name FROM tags WHERE name IN ({bind_params})"

        query_result = self.cursor.execute(escaped_query, tags)
        tags = query_result.fetchall()

        return tags

    # __relate_tags_to_interest
    def relate_tags_to_interest(self, interest_id: int, tag_id: int):
        self.cursor.execute(
            "INSERT INTO interests_tags VALUES(?, ?)", (interest_id, tag_id)
        )
        self.connection.commit()
