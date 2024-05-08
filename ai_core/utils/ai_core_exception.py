class LLMCoreException(Exception):
    pass


class NotFoundException(LLMCoreException):
    pass


class ValidationException(LLMCoreException):
    pass


class NetworkException(LLMCoreException):
    pass


class InternalException(LLMCoreException):
    pass


class UnknownException(LLMCoreException):
    pass
