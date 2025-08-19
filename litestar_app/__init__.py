from contextlib import asynccontextmanager
from litestar import Litestar
from litestar_app.api import greet


def option1():
    return Litestar([greet])


def option2():
    @asynccontextmanager
    async def lifespan(app: Litestar):
        yield

    return Litestar([greet], lifespan=[lifespan])


def option3():
    @asynccontextmanager
    async def lifespan(
        app_settings,
        _app: Litestar,
    ):
        yield

    return Litestar([greet], lifespan=[lifespan])


# Update as desired.
# Option1 throws a hypercorn.utils.LifespanTimeoutError
# Option2, while syntactically correct, also throws a hypercorn.utils.LifespanTimeoutError
# Option3, while wrong code, works
app = option2()
