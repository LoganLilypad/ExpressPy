class Response:

  def __init__(self, status):
    self.status = status 
  

  @staticmethod
  def status(code: int):
    return Response(code)

  @staticmethod 
  def send(response: dict or str) -> None:
    pass
