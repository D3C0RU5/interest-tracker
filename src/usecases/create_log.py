from src.repository.sqlite.interest_repo import InterestRepo
from src.repository.sqlite.tags_repo import TagsRepo


class CreateLogUseCase:
    def __init__(self, interest_repository: InterestRepo, tag_repository: TagsRepo):
        self.interest_repository = interest_repository
        self.tag_repository = tag_repository

    def handle(self, log: str, effort: int, tags: list[str]):
        interest_id = self.interest_repository.create(log=log, effort=effort)

        for tag in tags:
            result = self.tag_repository.get_by_name(name=tag)
            if result is None:
                tag_id = self.tag_repository.create(name=tag)
            else:
                tag_id = result[0]
            self.tag_repository.relate_tags_to_interest(
                interest_id=interest_id, tag_id=tag_id
            )
