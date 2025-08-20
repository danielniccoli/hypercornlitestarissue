import restate
from hypercorn.middleware import DispatcherMiddleware

from .services import greeter
from litestar_app import app as litestar_app

restate_app = restate.app([greeter])

mounts = {
    "/restate": restate_app,
    "/": litestar_app,
}

app = DispatcherMiddleware(mounts)
