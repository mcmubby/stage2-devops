# Bug Fixes

Here is the list of bugs found and fixed in the source code to make it production-ready and containerizable.

1. **File:** `frontend/app.js`
   - **Line:** 6
   - **Problem:** The `API_URL` was hardcoded to `http://localhost:8000`. In a containerized environment, `localhost` refers to the container itself, not the API container.
   - **Fix:** Changed it to use the `API_URL` environment variable with a fallback to `localhost`: `const API_URL = process.env.API_URL || "http://localhost:8000";`.

2. **File:** `api/main.py`
   - **Line:** 8
   - **Problem:** Redis connection parameters (`host="localhost", port=6379`) were hardcoded. In a containerized setup, the API container cannot access Redis at `localhost`, and there was no provision for a password, which is a security best practice and required by the provided `.env`.
   - **Fix:** Updated the code to read `REDIS_HOST`, `REDIS_PORT`, and `REDIS_PASSWORD` from environment variables, passing them securely to the `redis.Redis()` instantiation.
