class ZeroProductQuantityError(Exception):
    """Exception for raise error for product with zero quantity"""

    def __init__(self, message: str = None) -> None:
        super().__init__(message)