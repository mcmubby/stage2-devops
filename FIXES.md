# Bug Fixes

Here is the list of bugs found and fixed in the source code to make it production-ready and containerizable.

1. **File:** `frontend/app.js`
   - **Line:** 6
   - **Problem:** The `API_URL` was hardcoded to `http://localhost:8000`. In a containerized environment, `localhost` refers to the container itself, not the API container.
   - **Fix:** Changed it to use the `API_URL` environment variable with a fallback to `localhost`: `const API_URL = process.env.API_URL || "http://localhost:8000";`.
