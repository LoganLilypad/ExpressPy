from express.app import App as ExpressApp
from express.request import Request


App     = ExpressApp()
Router  = App.router()

@Router.get(route="/")
def test(t):
  pass


@Router.multi(methods=["GET"], route="/honk")
def honk(req, res):
  res.send(b'hi')


App.listen(3002)


