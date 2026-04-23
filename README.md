# Job Processor Application

This is a microservices application consisting of a Node.js frontend, a Python FastAPI backend, and a Python worker, with a Redis queue.

## Prerequisites
- Docker
- Docker Compose

## How to Run

1. Clone the repository and navigate into the project directory:
   ```bash
   git clone https://github.com/isw-mubby/stage2-devops.git
   cd stage2-devops
   ```

2. Create a `.env` file from the provided example:
   ```bash
   cp .env.example .env
   ```

3. Start the entire stack using Docker Compose:
   ```bash
   docker compose up --build -d
   ```

4. **Verify Startup:**
   Wait a few moments for the health checks to pass. You can verify the status of the containers by running:
   ```bash
   docker compose ps
   ```
   A successful startup will show `frontend`, `api`, `worker`, and `redis` as `Up (healthy)`.

5. **Access the Application:**
   Open your browser and navigate to `http://localhost:3000` to access the Job Dashboard.

## CI/CD Pipeline
This repository uses GitHub Actions for continuous integration and continuous deployment. On push to `main`, the pipeline automatically lints the code, runs unit tests, builds the images, scans them for vulnerabilities, runs integration tests, and performs a simulated rolling update deployment using Docker Compose.
