class ResponseBuilder:
    def __init__(self, status: bool, code: int, message: str, data=None, error=None):
        self.status = status
        self.code = code
        self.message = message
        self.data = data
        self.error = error

    def build(self):
        return {
            "status": self.status,
            "code": self.code,
            "message": self.message,
            "data": self.data,
            "error": self.error
        }

    @staticmethod
    def success(data=None, message="Success", code=200):
        return ResponseBuilder(True, code, message, data).build()

    @staticmethod
    def error(message="Error", error=None, code=500):
        return ResponseBuilder(False, code, message, None, error).build()
