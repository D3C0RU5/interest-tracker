from src.repository.sqlite.interest_repo import InterestRepo
from src.repository.sqlite.tags_repo import TagsRepo


class ListLogUseCase:
    def __init__(self, interest_repository: InterestRepo):
        self.interest_repository = interest_repository

    def handle(self):
        interests = self.interest_repository.list()

        return interests
