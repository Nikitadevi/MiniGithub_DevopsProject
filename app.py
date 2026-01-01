from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# 🔗 Your GitHub Repo Info
GITHUB_USER = "Nikitadevi"
GITHUB_REPO = "MiniGithub_DevopsProject"
BASE_API = f"https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}"


@app.route("/")
def home():
    return render_template("index.html")


# ---------------- COMMITS TABLE ----------------
@app.route("/commits")
def commits():
    url = f"{BASE_API}/commits"
    response = requests.get(url)
    commits = response.json()

    html = "<h2 style='font-family:Arial;'>Commit History</h2>"
    html += "<table border='1' cellpadding='8' style='border-collapse:collapse;font-family:Arial;'>"
    html += "<tr><th>Hash</th><th>Message</th><th>Author</th><th>Date</th></tr>"

    for c in commits:
        sha = c["sha"][:7]
        msg = c["commit"]["message"]
        author = c["commit"]["author"]["name"]
        date = c["commit"]["author"]["date"][:10]
        html += f"<tr><td>{sha}</td><td>{msg}</td><td>{author}</td><td>{date}</td></tr>"

    html += "</table>"
    return html


# ---------------- BRANCHES LIST ----------------
@app.route("/branches")
def branches():
    url = f"{BASE_API}/branches"
    response = requests.get(url)
    branches = response.json()

    html = "<h2 style='font-family:Arial;'>Repository Branches</h2><ul style='font-size:20px;'>"
    for b in branches:
        html += f"<li><b>{b['name']}</b></li>"
    html += "</ul>"

    return html


# ---------------- GIT STATUS (Summary) ----------------
@app.route("/status")
def status():
    repo = requests.get(BASE_API).json()
    latest_commit = requests.get(f"{BASE_API}/commits").json()[0]

    html = "<h2 style='font-family:Arial;'>Repository Status</h2>"
    html += f"<p><b>Repo:</b> {repo['full_name']}</p>"
    html += f"<p><b>Default Branch:</b> {repo['default_branch']}</p>"
    html += f"<p><b>Last Commit:</b> {latest_commit['commit']['message']}</p>"
    html += f"<p><b>Last Commit Author:</b> {latest_commit['commit']['author']['name']}</p>"
    html += f"<p><b>Date:</b> {latest_commit['commit']['author']['date'][:10]}</p>"

    return html


# ---------------- RUN CUSTOM GIT COMMAND (LOCAL ONLY) ----------------
@app.route("/run", methods=["GET", "POST"])
def run_git():
    return "<h3>Git Run Command only works locally, not on Render deployment.</h3>"


if __name__ == "__main__":
    app.run(debug=True)
