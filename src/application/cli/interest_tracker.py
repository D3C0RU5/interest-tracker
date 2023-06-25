import argparse
import sys
from src.repository.sqlite.interest_repo import InterestRepo
from src.repository.sqlite.tags_repo import TagsRepo
from src.use_cases.create_log import CreateLogUseCase

from src.use_cases.list_log import ListLogUseCase
from src.utilities.parse_effort import parse_effort
from src.utilities.parse_tags import parse_tags


class InterestTracker:
    def __init__(self):
        parser = argparse.ArgumentParser(
            description="Track your hacking sessions with this simple cli app.",
            usage="""interest-tracker.py <command> [<args>]

Available commands are:
    log         Register a new hacking interest
    visualize   Visualize existing interests
""",
            epilog="a joint venture by guites <https://github.com/guites> and D3C0RU5 <https://github.com/D3C0RU5>.",
        )

        parser.add_argument("command", help="Subcommand to run")
        # parse_args defaults to [1:] for args, but you need to
        # exclude the rest of the args too, or validation will fail
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print("Unrecognized command")
            parser.print_usage()
            sys.exit(1)
        # use dispatch pattern to invoke method with same name
        getattr(self, args.command)()

    def log(self):
        parser = argparse.ArgumentParser(description="Register a new hacking interest")
        parser.add_argument("log", metavar="LOG", help="What you've been hacking at")
        parser.add_argument(
            "-e", "--effort", required=True, help="How long you've been at it (HH:MM)"
        )
        parser.add_argument(
            "-t", "--tags", help="Comma separated tags to group your interests"
        )
        # now that we're inside a subcommand, ignore the first
        # TWO argvs, ie the command (interest-tracker) and the subcommand (log)
        args = parser.parse_args(sys.argv[2:])

        try:
            parsed_effort = parse_effort(args.effort)
        except ValueError:
            parser.error("EFFORT (-e, --effort) should be in HH:MM format")

        parsed_tags = parse_tags(args.tags)

        interests_repo = InterestRepo()
        tags_repo = TagsRepo()
        CreateLogUseCase(
            interest_repository=interests_repo, tag_repository=tags_repo
        ).handle(log=args.log, effort=parsed_effort, tags=parsed_tags)

    def visualize(self):
        # TODO: should be able to filter by day, week, month, etc
        # parser = argparse.ArgumentParser(description="Visualize existing interests")
        # parser.add_argument("")

        interests_repo = InterestRepo()
        interests = ListLogUseCase(interests_repo).handle()

        for interest in interests:
            print(interest)
