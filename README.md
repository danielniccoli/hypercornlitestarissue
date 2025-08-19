This is a sample app demoing an issue with wrong lifespan code leading to a working application. For details, check `./litestar_app/__init__.py` and choose one of the three options give. Note the inline comments.


Run via:
```bash
uv venv
uv sync
python -m restate_app
# or by pressing F5 in VSCode

# optional params:
# --address=localhost
# --port=9080
# --reload
```