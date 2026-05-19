# BlogWebsite

A simple Django blog website project with users, categories, posts, comments, admin management, sample data, and the required HTML pages.

## Setup

```powershell
..\.venv\Scripts\python.exe manage.py migrate
..\.venv\Scripts\python.exe manage.py seed_blog_data
..\.venv\Scripts\python.exe manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## PyCharm

Open the `BlogWebsite` folder in PyCharm. This project includes a PyCharm run configuration named `Django Runserver`.

If PyCharm asks for an interpreter, choose:

```text
C:\Users\shoog\Documents\Codex\2026-05-19\files-mentioned-by-the-user-project\.venv\Scripts\python.exe
```

More details are in `PYCHARM_SETUP.md`.

## Admin

Open `http://127.0.0.1:8000/admin/` and log in with:

```text
Username: Shoog
Password: ShoogRa
```

## Pages

- `main.html` - main page with links to all other pages
- `users.html` - list of users with username and email
- `blogs.html` - list of blog titles
- `blogdetails.html` - detail page for a selected blog post
- `comments.html` - list of comments with blog IDs
- `categories.html` - list of categories
- `master.html` - shared layout used by all pages

## GitHub Upload

```powershell
git init
git add .
git commit -m "Create Django blog website"
git branch -M main
git remote add origin https://github.com/shoog6138-rgb
git push -u origin main
```
