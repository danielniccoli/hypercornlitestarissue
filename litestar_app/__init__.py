from litestar import Litestar
from litestar_app.api import greet

app = Litestar([greet])
