from litestar import post
from pydantic import BaseModel

#from restate_app.services import greet as greet_svc

class GreetingRequest(BaseModel):
    name: str


class Greeting(BaseModel):
    message: str


@post("/greet")
async def greet(data: GreetingRequest) -> Greeting:
    restate_response = f"You said hi to {data.name}!"
    # call restate_app.services.greet():
    # e.g., restate_response = restate.client(...)
    return Greeting(message=restate_response)
