from os import environ
import sys

TEMPLATE_DIR = environ.get("TEMPLATE_DIR")


def handle_request(request):
    if "GET / " in request:
        with open(f"{TEMPLATE_DIR}/index.html", "r") as file:
            body = file.read()
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: {len(body)}\r\n\r\n{body}"
    elif "GET /auth " in request:
        with open(f"{TEMPLATE_DIR}/auth.html", "r") as file:
            body = file.read()
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: {len(body)}\r\n\r\n{body}"
    else:
        body = "<html><body><h1>Page non trouvée!</h1></body></html>"
        response = f"HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\nContent-Length: {len(body)}\r\n\r\n{body}"
    return response


if __name__ == "__main__":
    request = sys.argv[1]
    response = handle_request(request)
    print(response)
