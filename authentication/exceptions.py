# authentication/exceptions.py

class TokenExpiredError(Exception):
    """Exception raised when the token is expired."""
    pass

class InvalidTokenError(Exception):
    """Exception raised when the token is invalid."""
    pass