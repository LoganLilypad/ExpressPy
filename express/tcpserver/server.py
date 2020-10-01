import socket 
import time
from express.request import Request
from express.response import Response
from express.tcpserver.socket_thread import ServerSocketThread

class Server:
  host: str = 'localhost'
  port: int
  __default_timeout: int or float = 0.5

  def __init__(self, port: int) -> None:
    self.port = port

  def start_server_thread(self, app) -> socket:

    sub = ServerSocketThread(app, self.host, self.port, self.__default_timeout)
    
    return sub.socket
    
