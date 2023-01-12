class Syn10Error(Exception):
    def __init__(self, message=None):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message

    def __repr__(self):
        err_tokens = []
        for k, v in self.__dict__.items():
            err_tokens.append("%s=%r" % (k, v))

        err_msg = f"{self.__class__.__name__}" + "(" + ", ".join(err_tokens) + ")"
        return err_msg


class APIError(Syn10Error):
    def __init__(self, message=None, code=None):
        super().__init__(message=message)
        self.code = code


class AuthenticationError(APIError):
    pass


class Timeout(APIError):
    pass


class InvalidResponse(APIError):
    pass
