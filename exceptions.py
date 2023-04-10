class Error(Exception):
    """Base class for all other exceptions"""

    pass


class NoTaskForGivenId(Exception):
    """Raised when no task is found for the given Id"""

    pass
