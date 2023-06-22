from src.repository.sqlite.interest_repo import InterestRepo
from src.repository.sqlite.tags_repo import TagsRepo
from src.usecases.create_log import CreateLogUseCase
from src.usecases.list_log import ListLogUseCase


interests_repo = InterestRepo()
tags_repo = TagsRepo()

list_log_use_case = ListLogUseCase(interest_repository=interests_repo)
create_log_use_case = CreateLogUseCase(
    interest_repository=interests_repo, tag_repository=tags_repo
)


list_log_use_case.handle()
create_log_use_case.handle("some log", 100, ["class", "another-class"])
list_log_use_case.handle()
