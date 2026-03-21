class ApplicationException(Exception):
    status_code: int = 500
    message: str = "Internal server error."

    def __init__(self) -> None:
        super().__init__(self.message)


class NotFoundException(ApplicationException):
    status_code: int = 404
    message: str = "Resource not found."
