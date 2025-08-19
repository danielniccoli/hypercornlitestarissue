from contextlib import asynccontextmanager
from litestar import Litestar
from litestar_app.api import greet


@asynccontextmanager
async def lifespan(app: Litestar):
    # Setup code here
    yield
    # Teardown code here

app = Litestar([greet], lifespan=[lifespan])
