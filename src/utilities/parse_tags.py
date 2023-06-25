def parse_tags(tags: str) -> "list[str]":
    """splits a list of tags by comma and replaces any internal spaces with underlines

    Return: list[str] (list of tags)"""
    if tags is not None:
        return [t.strip().replace(" ", "_") for t in tags.split(",")]
    return []
