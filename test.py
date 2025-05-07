import urllib.request

url = "http://127.0.0.1:8091"
headers = {
    "User-Agent": "MyCustomAgent/1.0",
    "Content-Type": "application/json",
    "X-Forwarded-For": "127.0.0.1"
}

req = urllib.request.Request(url, headers=headers, method='GET')

try:
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code} - {e.reason}")
except urllib.error.URLError as e:
    print(f"URL Error: {e.reason}")