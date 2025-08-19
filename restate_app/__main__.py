import argparse

from hypercorn.config import Config
from hypercorn.run import run

parser = argparse.ArgumentParser(prog=f"python -m {__package__}")
parser.add_argument(
    "-a",
    "--address",
    help="set the IP address or hostname to bind to (default: 0.0.0.0)",
    default="0.0.0.0",
)
parser.add_argument(
    "-p", "--port", help="set the TCP port to listen on (default: 8000)", default="8000"
)
parser.add_argument(
    "-r",
    "--reload",
    action="store_true",
    help="enable automatic reloads on code changes",
)
args = parser.parse_args()

config = Config()
config.application_path = f"{__package__}:app"
config.bind = [f"{args.address}:{args.port}"]
config.use_reloader = args.reload

try:
    run(config)
except OSError as err:
    print(err.strerror)
