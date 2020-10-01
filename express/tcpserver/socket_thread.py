from threading import Thread 
import socket, os, errno
from time import sleep
from express.request import Request
from express.response import Response

class ServerSocketThread(Thread):

    socket: socket or None = None

    def __init__(self, app, host: str, port: int, timeout: int or float) -> None:

        self.app = app
        self.host = host
        self.port = port
        self.socket = None
        self.timeout = timeout

        super().__init__()
        self.start()

    def _detect_exit(self, sock) -> None:
        try:
            print("waiting for keyboardinterrupt")
            sleep(1)
        except KeyboardInterrupt:
            sock.close
            exit()

    def run(self) -> None:
        
      # Should probably give this a more descriptive name but that's alright I guess.
  
      serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      serv.bind( ( self.host, self.port ) ) # Bind on localhost:{port}
      serv.setblocking(0)
      serv.settimeout(self.timeout)
      self.socket = serv

      # fcntl.fcntl(serv, fcntl.F_SETFL, os.O_NONBLOCK)
      # Realized the above only works on linux, which is pretty annoying but alright.

      serv.listen(1)

      

      try:
          while True:
              try:
                  conn, addr = serv.accept()
                  data = conn.recv(8192).decode().strip()

                  if len(data) > 0:
                      req = Request.parse(Request.decode(data))

                      Handler = self.app.handler()

                      if Handler.is_accepted(req.headers["path"], req.headers["path"]):
                          Handler.get(req.headers["path"]).handle(req, Response(conn))
                      else:
                          pass
                  else:
                      pass
              except socket.timeout:
                  pass # Unsure what to do here.
              except KeyboardInterrupt:
                  pass
      except KeyboardInterrupt:
          exit()


      #while True:
      #  try:
      #      conn, addr = serv.accept()
      #      data = conn.recv(8192).decode().strip()
      #
      #      if len(data) > 0: 
      #          req = Request.parse(Request.decode(data))
      #
    
      #          Handler = self.app.handler()
      #  
      #          if Handler.is_accepted(req.headers["path"], req.headers["method"]):
      #              Handler.get(req.headers["path"]).handle(req, Response(conn))
      #          else: pass
      #      else: pass
      #  except socket.error as e:
      #      err = e.args[0]
      #      if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
      #          sleep(1)
      #         continue
      #      else:
      #          print("?")
      #         exit()