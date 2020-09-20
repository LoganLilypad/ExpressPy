import socket 
import time
from express.request import Request
from express.response import Response
from express.tcpserver.socket_thread import ServerSocketThread

class Server:
  host: str = 'localhost'
  port: int

  def __init__(self, port: int) -> None:
    self.port = port

  def start(self, app) -> socket:

    sub = ServerSocketThread(app, self.host, self.port)
    sub.start()
    
    return sub.socket
    
