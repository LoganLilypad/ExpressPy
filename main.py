from express.app import App as ExpressApp
from express.request import Request

App     = ExpressApp()
Router  = App.router()
Handler = App.handler()

@Router.get(route="/hi", handler=Handler)
def test(t):
  print(t)


@Router.multi(methods=["GET"], route="/g", handler=Handler)
def test2(t):
  print(t)


App.listen()

GeneratedRequest = Request.parse("""GET /search?honk=true HTTP/2\r\nHost: www.honk.com\r\nUser-Agent: curl/7.54.0\r\nAccept: */*""")

print(GeneratedRequest.parsedPath)
print(GeneratedRequest.path)


