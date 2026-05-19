# PyCharm Setup

Open this folder in PyCharm:

```text
C:\Users\shoog\Documents\Codex\2026-05-19\files-mentioned-by-the-user-project\BlogWebsite
```

Then connect the interpreter:

1. Open `File > Settings > Project: BlogWebsite > Python Interpreter`.
2. Choose `Add Interpreter`.
3. Select `Existing`.
4. Pick this Python file:

```text
C:\Users\shoog\Documents\Codex\2026-05-19\files-mentioned-by-the-user-project\.venv\Scripts\python.exe
```

After that, use the run configuration named `Django Runserver`.

If it does not appear automatically, create a Python run configuration:

- Script path: `manage.py`
- Parameters: `runserver 127.0.0.1:8000`
- Working directory: `C:\Users\shoog\Documents\Codex\2026-05-19\files-mentioned-by-the-user-project\BlogWebsite`
- Environment variable: `DJANGO_SETTINGS_MODULE=BlogWebsite.settings`

The website URL is:

```text
http://127.0.0.1:8000/
```

Admin panel:

```text
http://127.0.0.1:8000/admin/
```

Admin username:

```text
Shoog
```

Admin password:

```text
ShoogRa
```
