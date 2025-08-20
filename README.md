The code in this repo reproduces the `hypercorn.utils.LifespanTimeoutError` thrown by Hypercorn's DispatcherMiddleware when using two ASGI-Lifespan capable applications.

Entry point is module `restate_app`, which loads the restate and litestar app and configures the DispatcherMiddleware before running Hypercorn.  
(This app uses restate, which is not supported on Windows).

To run this app, do the following:

```bash
uv venv
uv sync
# Press F5 in VSCode to debug the app

# Or manually:
# $ python -m restate_app
#
# Optional params:
# --address=localhost
# --port=9080
# --reload
```

The traceback is:

```
Traceback (most recent call last):
  File "/root/.local/share/uv/python/cpython-3.13.6-linux-x86_64-gnu/lib/python3.13/asyncio/tasks.py", line 507, in wait_for
    return await fut
           ^^^^^^^^^
  File "/root/.local/share/uv/python/cpython-3.13.6-linux-x86_64-gnu/lib/python3.13/asyncio/locks.py", line 213, in wait
    await fut
asyncio.exceptions.CancelledError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/code/hypercornlitestarissue/.venv/lib/python3.13/site-packages/hypercorn/asyncio/lifespan.py", line 94, in wait_for_startup
    await asyncio.wait_for(self.startup.wait(), timeout=self.config.startup_timeout)
  File "/root/.local/share/uv/python/cpython-3.13.6-linux-x86_64-gnu/lib/python3.13/asyncio/tasks.py", line 506, in wait_for
    async with timeouts.timeout(timeout):
               ~~~~~~~~~~~~~~~~^^^^^^^^^
  File "/root/.local/share/uv/python/cpython-3.13.6-linux-x86_64-gnu/lib/python3.13/asyncio/timeouts.py", line 116, in __aexit__
    raise TimeoutError from exc_val
TimeoutError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/root/.local/share/uv/python/cpython-3.13.6-linux-x86_64-gnu/lib/python3.13/multiprocessing/process.py", line 313, in _bootstrap
    self.run()
    ~~~~~~~~^^
  File "/root/.local/share/uv/python/cpython-3.13.6-linux-x86_64-gnu/lib/python3.13/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/code/hypercornlitestarissue/.venv/lib/python3.13/site-packages/hypercorn/asyncio/run.py", line 196, in asyncio_worker
    _run(
    ~~~~^
        partial(worker_serve, app, config, sockets=sockets),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        debug=config.debug,
        ^^^^^^^^^^^^^^^^^^^
        shutdown_trigger=shutdown_trigger,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/code/hypercornlitestarissue/.venv/lib/python3.13/site-packages/hypercorn/asyncio/run.py", line 234, in _run
    runner.run(main(shutdown_trigger=shutdown_trigger))
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/.local/share/uv/python/cpython-3.13.6-linux-x86_64-gnu/lib/python3.13/asyncio/runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
  File "/root/.local/share/uv/python/cpython-3.13.6-linux-x86_64-gnu/lib/python3.13/asyncio/base_events.py", line 725, in run_until_complete
    return future.result()
           ~~~~~~~~~~~~~^^
  File "/code/hypercornlitestarissue/.venv/lib/python3.13/site-packages/hypercorn/asyncio/run.py", line 84, in worker_serve
    await lifespan.wait_for_startup()
  File "/code/hypercornlitestarissue/.venv/lib/python3.13/site-packages/hypercorn/asyncio/lifespan.py", line 96, in wait_for_startup
    raise LifespanTimeoutError("startup") from error
hypercorn.utils.LifespanTimeoutError: Timeout whilst awaiting startup. Your application may not support the ASGI Lifespan protocol correctly, alternatively the startup_timeout configuration is incorrect.
```