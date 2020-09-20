from threading import Thread 
import socket

from express.request import Request
from express.response import Response

class ServerSocketThread(Thread):

    socket: socket or None = None

    def __init__(self, app, host: str, port: int) -> None:

        self.app = app
        self.host = host
        self.port = port
        self.socket = None

        super().__init__()
        
    def run(self) -> None:
        
      serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      serv.bind( ( self.host, self.port ) )
      serv.listen(1)

      self.socket = serv
        
      try:
        while True:

          conn, addr = serv.accept()
          data = conn.recv(8192).decode().strip()

          if len(data) > 0: 
            req = Request.parse(Request.decode(data))


            Handler = self.app.handler()

            if Handler.is_accepted(req.headers["path"], req.headers["method"]):
              Handler.get(req.headers["path"]).handle(req, Response(conn))
            else: pass
          else: pass
      except: 
        exit()