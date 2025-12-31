## 🚀 Mini GitHub – DevOps Source Code Management Project

A practical implementation of Git + GitHub workflow with branching, merging, conflict resolution, commits tracking, and Flask integration.
This project simulates how real development teams manage code, collaborate, review history, and deploy updates.

## 📌 Project Objective

The main aim of this project is to learn and perform version control in DevOps, understand how source code evolves over time, and demonstrate how developers work using Git.
To practice this, I created a web page and maintained its versions through Git branches, commits, and merges.

Later, I integrated Flask (Python) to allow viewing Git Commit History, Branches, and Status through the browser — making it interactive.

## 🧠 What this project demonstrates

Concept	Description
-Version Control	Track changes, revert anytime, maintain history

-Branching	Work on new features without affecting main code

-Merge & Conflicts	Combine branches and manually resolve conflicts

-Remote Collaboration	Push, pull, sync using GitHub

-Flask Integration	View commits/branches/status inside the web app

-Deployment Ready	Files added for hosting (requirements.txt, Procfile)

## 📄 How the Project Works

1.Created a Git repository locally

2.Built a web page (index.html) to practice code changes

3.Created multiple Git branches (feature, test, bugfix, experiment)

4.Made modifications in each branch

5.Merged back to master (intentionally created & solved conflict)

6.Connected repo to GitHub and pushed code

7.Integrated Flask to display Git output through UI

8.Prepared project for deployment

## 🛠 Tech Stack & Tools Used

-Technology	Usage

-Git	Version control system

-GitHub	Remote repo hosting

-HTML + CSS	UI design for project webpage

-Python + Flask	Backend routes to fetch commit/branch/status

-Git Bash / Terminal	Executed commands to manage repo

-Windows	Development environment

## 🔥 Flask Features Added

After running the app using python app.py, user can visit:

Route	Output
/	Main webpage (UI)

/commits	Shows complete commit history

/branches	Lists all Git branches

/status	Displays git status of working directory

/run (optional interactive)	Execute custom git commands (POST method)

## 📌 Git Commands Used (with explanation)

git init                # Start a new repository

git status              # Check modified/untracked files

git add .               # Stage all files

git commit -m ""        # Save snapshot of changes

git branch              # Show branch list

git branch <name>       # Create new branch

git checkout <name>     # Switch between branches

git merge <name>        # Merge branch into current

git log --oneline       # View short commit history

git diff                # View file differences before commit

git remote add origin   # Connect local repo to GitHub

git push -u origin master   # Push code to GitHub

## 🧩 What I Learned

✔ How Git internally manages versions

✔ How branches prevent conflicts during development

✔ Handling & solving merge conflicts manually

✔ Pushing and maintaining repository on GitHub

✔ How Flask can execute system commands and show output on UI

✔ Preparing a project for hosting

## 📁 Project Structure

MiniGithub_Devops/
│── app.py               # Flask backend

│── index.html           # Main UI (inside templates)

│── templates/

    └── index.html

│── requirements.txt     # Libraries for deployment

│── Procfile             # Render/Heroku deployment file

└── README.md

## 🎯 Final Output

This project successfully demonstrates end-to-end Git workflow with practical implementation.
It is useful for DevOps, version control training, beginners learning Git, and portfolio presentation.

👤 Developed By
## Nikita Nath
