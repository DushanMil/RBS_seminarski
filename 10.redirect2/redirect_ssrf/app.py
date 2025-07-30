from flask import Flask, request, redirect
import urllib.request
from urllib.parse import urlparse

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h1>🖨️ PDF Generator</h1>
    <form method="GET" action="/generate">
        <input name="url" placeholder="Enter URL to convert to PDF" style="width: 400px;">
        <button type="submit">Generate PDF</button>
    </form>
    """

@app.route("/generate")
def generate_pdf():
    url = request.args.get("url", "")
    parsed = urlparse(url)

    if (
    parsed.hostname is None
    or "localhost" in parsed.netloc
    or parsed.hostname.startswith("127.")
    or parsed.hostname == "::1"
    or "admin" in parsed.path
    or parsed.scheme not in ["http", "https", "file"]
    ):
        return "URL blocked by SSRF filter."


    try:
        with urllib.request.urlopen(url, timeout=3) as res:
            content = res.read().decode("utf-8")
        return f"<h2>PDF Rendered:</h2><pre>{content}</pre>"
    except Exception as e:
        return f"<h2>Error:</h2><pre>{e}</pre>"

@app.route("/redirect")
def redirect_to():
    to = request.args.get("to", "/")
    return redirect(to, code=302)

@app.route("/admin")
def admin_panel():
    try:
        with open("/app/file.txt", "r") as f:
            flag = f.read()
        return f"<h3>Welcome, admin!</h3><pre>{flag}</pre>"
    except:
        return "Access denied. Flag file missing or unreadable."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
