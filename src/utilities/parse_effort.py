from datetime import datetime, timedelta


def parse_effort(time_string: str) -> int:
    """receives `time_string` in HH:MM:SS format and return
    the number of seconds as an integer.

    based on https://stackoverflow.com/a/12352624/14427854

    Raises:
        ValueError: time_string is incorrectly formatted

    Return: int (time in seconds)"""
    date_time = datetime.strptime(time_string, "%H:%M")
    time_delta = timedelta(hours=date_time.hour, minutes=date_time.minute)
    return int(time_delta.total_seconds())
