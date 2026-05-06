 NGINX Load Balancing Demo with FastAPI

## Overview

This project demonstrates load balancing using NGINX with multiple FastAPI backend instances running in Docker.

It simulates a simple distributed system where multiple identical API servers handle incoming requests, and NGINX distributes traffic across them.

A Python script is used to test and verify how requests are distributed across backend instances.

---

## Architecture

- 3 FastAPI application instances (app1, app2, app3)
- NGINX reverse proxy acting as a load balancer
- Docker Compose used to orchestrate services
- Python script used for load testing and validation

Flow:

Client → NGINX → One of the FastAPI instances → Response returned to client

---

## Tech Stack

- FastAPI
- NGINX
- Docker

---

## Project Structure
```
.
├── app
│   ├── main.py
│   ├── nginx
│   │   └── nginx.conf
│   └── scripts
│       └── load_balancer_test.py
├── docker-compose.yml
├── dockerfile
├── readme.md
└── requirements.txt
```

---

## Running the Project

### 1. Build and start all services

Run the following command from the project root:

```
docker compose up --build
```

This will:

- Build the FastAPI image
- Start 3 backend containers (app1, app2, app3)
- Start the NGINX load balancer container with configurations in app->nginx->nginx.conf

### 2. Verify NGINX is running

Open in browser or use curl:
```
curl http://localhost:8080/hello
```
Expected response example:
```
{"server_no": 1}
```
The server_no will vary depending on which backend instance handled the request.

### 3. Run load balancing test script
Install dependency (if not already installed):
```
pip install requests
```
Run the test:
```
python scripts/load_balancer_test.py
```
### Expected Output
```
Sending 300 requests to http://localhost:8080/hello...

Request distribution:
---------------------
1: 100
2: 100
3: 100
```

