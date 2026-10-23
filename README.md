<div align="center">
  <img src="frontend/public/logo.png" alt="Citizens Advice" width="100" height="100" />
  <h1>Citizens Advice SORT</h1>
  <h3>Junior Developer Practical</h3>
</div>

A small full-stack app: a **FastAPI** backend (Python) and a **Next.js** frontend (TypeScript).

The app shows answers to advisers' questions, along with the sources each answer is based on. Your job is to finish it. [TASK.md](TASK.md) explains what to build.

## Project structure

```
junior-developer/
├── backend/                 FastAPI app (Python, managed with uv)
│   ├── app/                 The API, including GET /data
│   └── data/mock.json       The questions, answers and sources
├── frontend/                Next.js app (TypeScript, Tailwind)
│   ├── app/page.tsx         The home page
│   └── components/          Content.tsx shows one item from the data
├── Makefile                 Shortcut commands (install, dev)
├── SETUP.md                 How to install the tools and get the app running
└── TASK.md                  What to build
```

## The task

[TASK.md](TASK.md) has the full instructions.

**Backend.** In the backend, you need to:

1. Work out which sources each answer cites, and replace each `<ref>` with a link.
2. Get a favicon for each source's website.
3. Redact the client's name, email and phone number from each question.

**Frontend.** In `Content.tsx`, show each item:

1. The redacted question.
2. The answer, with working citation links.
3. Every source, cited and not cited, with its favicon.

## Getting set up

Follow [SETUP.md](SETUP.md) to install the tools you need and get the app running. The first run downloads the redaction model, [fastino/GLiNER2-Guardrails-PII-Multi](https://huggingface.co/fastino/GLiNER2-Guardrails-PII-Multi) (about 1.2 GB).

```bash
make install
make dev
```

| What | URL |
|---|---|
| Backend | http://localhost:8000 |
| API docs | http://localhost:8000/docs |
| Frontend | http://localhost:3000 |

> If you have any problems or are unsure about any of the steps please email technology@casort.org
