class Server:
  host: str = '127.0.0.1'
  port: int

  def __init__(self, port: int) -> None:
    self.port = port

  def start(self) -> None:
    pass


