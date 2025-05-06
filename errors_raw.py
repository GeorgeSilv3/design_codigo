class HttpUprocessableEntityError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = "HttpUprocessableEntityError"
        self.status_code = 422

try:
    print("Estou no bloco Try")
    raise HttpUprocessableEntityError("Estou lancando a exception")
except Exception as exception:
    print("Estu no tratamento de erro")
    print(exception.name)
    print(exception.status_code)