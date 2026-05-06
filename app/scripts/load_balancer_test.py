import requests
from collections import defaultdict

URL = "http://localhost:8080/hello"
REQUESTS = 200

counts = defaultdict(int)

print(f"Sending {REQUESTS} requests to {URL}\n")

for i in range(REQUESTS):
    try:
        response = requests.get(URL, timeout=2)
        data = response.json()

        server_no = data.get("server_no", "unknown")

    except Exception:
        server_no = "unknown"

    counts[server_no] += 1

print("Request distribution:")
print("---------------------")

for key, value in counts.items():
    print(f"{key}: {value}")
