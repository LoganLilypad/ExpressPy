class Response:

  _socket = None 

  def __init__(self, socket):
    self._socket = socket

  def status(self, code: int):
    self.status = code
    return self

  def send(self, response: dict or str) -> None:
    #TBA: Integrate response variable.
    
    if self.status != None:
        self._socket.send(bytes("Http/1.0 {}".format(self.status), 'utf8'))
    else: 
        self._socket.send(bytes("Http/1.0 200 OK", 'utf8'))