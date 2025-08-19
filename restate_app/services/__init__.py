from pydantic import BaseModel
import restate


class GreetingRequest(BaseModel):
    name: str


class Greeting(BaseModel):
    message: str


greeter = restate.Service("Greeter")


@greeter.handler()
async def greet(ctx: restate.Context, req: GreetingRequest) -> Greeting:
    return Greeting(message=f"You said hi to {req.name}!")
