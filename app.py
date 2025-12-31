from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

GITHUB_USER = "Nikitadevi"
REPO_NAME = "MiniGithub_DevopsProject"

# Home
@app.route("/")
def home():
    return render_template("index.html")


# Get commits from GitHub
@app.route("/commits")
def commits():
    url = f"https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}/commits"
    data = requests.get(url).json()

    html = "<h2>Latest Commits</h2><ul>"
    for c in data[:10]:
        html += f"<li><b>{c['commit']['message']}</b> - {c['commit']['author']['name']} </li>"
    html += "</ul>"

    return html


# Get branches from GitHub
@app.route("/branches")
def branches():
    url = f"https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}/branches"
    data = requests.get(url).json()

    html = "<h2>Branches</h2><ul>"
    for b in data:
        html += f"<li>{b['name']}</li>"
    html += "</ul>"

    return html


# Git Status (static message on cloud)
@app.route("/status")
def status():
    return "<h2>Status</h2><p>Live deployed version - Git history unavailable on server.</p>"


if __name__ == "__main__":
    app.run(debug=True)
