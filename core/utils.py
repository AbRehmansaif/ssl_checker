import ssl, socket, requests
from datetime import datetime
from urllib.parse import urlparse


def check_website(url):
    result = {"url": url, "status": None, "ssl_days_left": None, "error": None}

    try:
        # 1. Check HTTP status
        response = requests.get(url, timeout=5)
        result["status"] = response.status_code
    except Exception as e:
        result["error"] = f"HTTP Error: {e}"

    try:
        # 2. Check SSL Expiry
        hostname = urlparse(url).hostname
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                ssl_info = ssock.getpeercert()
                expiry_date = datetime.strptime(ssl_info['notAfter'], '%b %d %H:%M:%S %Y %Z')
                days_left = (expiry_date - datetime.utcnow()).days
                result["ssl_days_left"] = days_left
    except Exception as e:
        result["error"] = result["error"] or f"SSL Error: {e}"

    return result
