from express.app import App as ExpressApp
from express.request import Request


App     = ExpressApp()
Router  = App.router()
Handler = App.handler()

@Router.get(route="/", handler=Handler)
def test(t):
  pass


@Router.multi(methods=["GET"], route="/honk", handler=Handler)
def honk(req, res):
  res.send(b'hi')


App.listen(3002)


