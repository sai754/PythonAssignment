class InvalidDataException(Exception):
    def __init__(self, message="Invalid data entered"):
        self.message = message
        super().__init__(self.message)

class IncompleteOrderException(Exception):
    def __init__(self, message="Incomplete order: Missing product reference"):
        self.message = message
        super().__init__(self.message)

class InsufficientStockException(Exception):
    def __init__(self, message="Insufficient stock available"):
        self.message = message
        super().__init__(self.message)

class DBConnectionException(Exception):
    def __init__(self, message="Problem with connecting the DB"):
        self.message = message
        super().__init__(self.message)

class AuthenticationException(Exception):
    def __init__(self, message="You are not Authenticated for this"):
        self.message = message
        super().__init__(self.message)