from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

USERNAME = "Nikitadevi"
REPO = "MiniGithub_DevopsProject"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/commits")
def commits():
    url = f"https://api.github.com/repos/{USERNAME}/{REPO}/commits"
    res = requests.get(url).json()

    html = "<h1>Latest Commits</h1><ul>"
    for c in res[:10]:
        html += f"<li><b>{c['commit']['message']}</b> — {c['commit']['author']['name']}</li>"
    html += "</ul>"
    return html

@app.route("/branches")
def branches():
    url = f"https://api.github.com/repos/{USERNAME}/{REPO}/branches"
    res = requests.get(url).json()

    html = "<h1>Branches</h1><ul>"
    for b in res:
        html += f"<li>{b['name']}</li>"
    html += "</ul>"
    return html

@app.route("/status")
def status():
    return "<h1>Deployment Active 🟢</h1><p>Git operations limited on server</p>"

if __name__ == "__main__":
    app.run()
