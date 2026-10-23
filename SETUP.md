# Project setup

How to install the tools you need and get the app running.

## What you need to install

| Tool | Version | What it's for | Install |
|---|---|---|---|
| Git | any recent | Getting the code | https://git-scm.com/downloads |
| Node.js | 20.9 or newer (we recommend the current LTS, 24) | Running the frontend | https://nodejs.org/en/download |
| uv | latest | Managing Python and the backend's packages | https://docs.astral.sh/uv/getting-started/installation/ |
| make | any (optional) | Shortcut commands | Already on most Macs and Linux machines (see below for Windows) |

You **don't** need to install Python yourself. uv downloads the right version (3.14) the first time you run it.

### Check everything is installed

Open a **new** terminal and run:

```bash
git --version
node -v
uv --version
```

Each one should print a version number. If you get `command not found`, close your terminal, open a new one, and try again. New installs often need a fresh terminal before they work.

## Getting started

### 1. Get the code

```bash
git clone https://github.com/Citizens-Advice-SORT/junior-developer.git
cd junior-developer
```

### 2. Install dependencies

```bash
make install
```

This also downloads the redaction model the backend uses, [fastino/GLiNER2-Guardrails-PII-Multi](https://huggingface.co/fastino/GLiNER2-Guardrails-PII-Multi). It's about 1.2 GB, so the first run can take a few minutes. When it's done you'll see `Model ready`.

### 3. Run the app

```bash
make dev
```

This starts the backend and the frontend together. Press `Ctrl+C` to stop both.

The backend loads the redaction model when it starts, so it takes about 10 seconds to be ready. It reloads every time you save a Python file, so expect the same wait after each save.

| What | URL | What you should see |
|---|---|---|
| Backend | http://localhost:8000 | `{"message": "Hello World"}` |
| API docs | http://localhost:8000/docs | Interactive API documentation |
| Frontend | http://localhost:3000 | "Citizens Advice SORT" |

### Without make (e.g. on Windows)

Use two terminals, both starting from the `junior-developer` folder.

**Terminal 1: backend**

```bash
cd backend
uv sync
uv run python -c "from gliner2 import GLiNER2; from app.config import get_settings; GLiNER2.from_pretrained(get_settings().model_id); print('Model ready')"
uv run fastapi dev
```

The middle command downloads the redaction model, [fastino/GLiNER2-Guardrails-PII-Multi](https://huggingface.co/fastino/GLiNER2-Guardrails-PII-Multi) (about 1.2 GB). You only need it the first time.

**Terminal 2: frontend**

```bash
cd frontend
npm install
npm run dev
```

## Project structure

```
backend/            FastAPI app (Python, managed with uv)
  app/
    main.py         Creates the app, loads the redaction model and includes the routers
    config.py       Settings, read from environment variables or a .env file
    dependencies.py get_model, for using the redaction model in an endpoint
    models.py       The shape of the data GET /data returns
    routers/        One file per group of endpoints
  data/
    mock.json       The data for the task
frontend/           Next.js app (App Router, TypeScript, Tailwind)
  app/
    page.tsx        The home page
  components/
    Content.tsx     Shows one item from the data
Makefile            Shortcut commands (install, dev, backend, frontend)
TASK.md             What to build
```

## Editor setup (optional)

If you use VS Code, point it at the backend's Python so imports and autocomplete work. Run `make install` first, then open the Command Palette and choose **Python: Select Interpreter**. Enter:

- macOS / Linux: `backend/.venv/bin/python`
- Windows: `backend\.venv\Scripts\python.exe`

## Useful links

- FastAPI tutorial: https://fastapi.tiangolo.com/tutorial/
- Next.js docs: https://nextjs.org/docs
- uv docs: https://docs.astral.sh/uv/
