from functools import wraps

from ai_core.utils.ai_core_exception import InternalException


def db_transaction(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Assume the first argument is 'self', which is the instance of the repository
        self = args[0]
        session = getattr(self, "session", None)
        if not session:
            raise InternalException(
                "Session attribute not found in the repository instance"
            )
        try:
            result = func(*args, **kwargs)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise InternalException(str(e))
        finally:
            session.close()

    return wrapper
