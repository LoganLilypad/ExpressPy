from express.exceptions.errors import RequestValidationError
import re

class Request: 

  params: dict or None = None
  query: dict or None = None
  path: str = ""
  headers: dict or None = None
  _QUERY_REGEX = "\?\w+=\w+|\&\w+=\w+"

  @property
  def query_regex(self) -> str:
    return self._QUERY_REGEX

  def __init__(
    self, 
    method: str, 
    headers: dict = {}, 
    params: str = "", 
    query: str = "", 
    parsedPath: str = "", 
    path: str = ""
  ) -> None:

    self.method = method
    self.headers = headers
    self.query = query
    self.params = params
    self.parsedPath = parsedPath 
    self.path = path


  @staticmethod
  def is_valid_method(method: str) -> bool:
    _methods = [
      "GET", 
      # "HEAD", 
      "POST", 
      "PATCH",
      "PUT", 
      "DELETE", 
      # "CONNECT", 
      "OPTIONS", 
      # "TRACE"
    ]

    return method.strip().upper() in _methods


  @staticmethod 
  def parse_query_string(query: str) -> dict:
    queries = {} 

    matches = re.findall(Request(None).query_regex, query)

    for match in matches:
      q = match.split("=")

      queries[re.sub('(\&|\?)', '', q[0])] = q[1]


    return queries

  @staticmethod
  def remove_query_string(line: str) -> None:
    return re.sub(Request(None).query_regex, '', line)

  @staticmethod
  def parse_cookie(line: str) -> None:
    cookie = ""

    matches = re.findall("Cookie\:\ .{1,}", line)


    for match in matches:
        cookie = match

    return Request.decode(cookie) 

  @staticmethod
  def parse(request_line: str):

    headers = {}
    queries = {}


    for line in request_line.lower().strip().split("\r\n"):
      parsed = line.replace(":", "~", 1).split("~")
      if len(parsed) > 1:
        headers[parsed[0]] = parsed[1].strip()
      else:
       
        method_type = parsed[0].split(" ")


      
        if Request.is_valid_method(method_type[0]):
          if len(method_type) == 3:
            headers["path"] = method_type[1]

            queries = Request.parse_query_string(method_type[1])
            
            headers["method"] = method_type[0].upper()
            headers["__v"] = method_type[2].upper()
          else:
            headers["method"] = method_type[0].upper()
            headers["__v"] = method_type[1].upper()    
        elif len(method_type[0]) <= 0:
          raise RequestValidationError(method_type[0].upper())
          
    try:
      headers["content-type"]
    except KeyError:
      headers["content-type"] = "html/plaintext"

    if Request.parse_cookie(Request.decode(request_line)) != None:
        headers["cookie"] = Request.parse_cookie(Request.decode(request_line))

    if len(queries) > 0:
      return Request(headers["method"], headers, None, queries, Request.remove_query_string(headers["path"]), headers["path"])
    else:
      return Request(headers["method"], headers, None, None, headers["path"], headers["path"]) 


  @staticmethod
  def generate(_dict: dict, status: int = 200) -> str:

    request = "Http/1.0 {status}" 

    for k, v in _dict.items:
      k = k.lower()
      v = v.lower()
      request += " {}: {}".format(k.replace(k[0], k[0].upper(), 1), v)

    return request.strip()

  @staticmethod
  def decode(_r: str) -> str:

    _new = ""
    _match = re.findall("\%[a-zA-Z0-9]{1,2}", _r.strip())

    for match in _match:
        
        _old = match
        match = match.replace("%", "", 1)
        _new = _r.replace(_old,  chr(int("0x{}".format(match), 16)))

    if not _new:
      return _r.strip()
    else:
      return _new
    
    

    




