<div align="center">
  <img src="frontend/public/logo.png" alt="Citizens Advice Logo" width="100" height="100" />
    <h1>Citizens Advice SORT</h1>
    <h3>Junior Developer Practical</h3>
</div>

---

## Overview

This is a full stack practical for Junior Developer at Citizens Advice SORT. The project consists of a full-stack application with a Python backend and Next.js frontend.

## Project Structure

```
junior-developer/
├── backend/
│   ├── data/
│   │   └── mock.json         # Mock data containing content and sources
│   ├── main.py               # FastAPI backend server
│   └── models.py             # Data models and schemas
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   │   ├── page.tsx      # Main page component
│   │   │   └── layout.tsx    # App layout
│   │   └── components/
│   │       └── Content.tsx   # Content display component
│   └── public/
│       └── logo.png          # Citizens Advice logo
└── Makefile                  # Build and run commands
```

## Task Description

### Backend Task

In the backend, you need to:

1. **Identify cited sources** within the content from `mock.json`
2. **Replace document IDs** with actual links to the sources
3. **Extract favicon URLs** from the source websites

### Frontend Task

The `Content.tsx` component has been provided for you to:

1. **Display each piece of content** and its associated sources, both cited and non-cited
2. **Show favicons** from the source websites alongside each source
3. **Create a clean, user-friendly interface**

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+
- npm
- [poetry](https://python-poetry.org/docs/#installation)

### Installation & Setup

1. **Clone the repository - DO NOT FORK**

   ```bash
   git clone https://github.com/Citizens-Advice-SORT/junior-developer.git
   cd junior-developer
   ```

2. **Install backend dependencies**

   ```bash
   cd backend
   poetry install --no-root
   ```

3. **Install frontend dependencies**
   ```bash
   cd frontend
   npm install
   ```

### Running the Application

Use the provided Makefile for easy setup:

```bash
# Install all dependencies
make install

# Run both frontend and backend
make dev

# OR INDIVIDUALLY
# Start the backend server
make run-backend

# Start the frontend development server
make run-frontend
```

Or run manually:

**Backend:**

```bash
cd backend
poetry run fastapi dev main.py
```

**Frontend:**

```bash
cd frontend
npm run dev
```

## API Endpoints

- `GET /data` - Returns the list of data

## Submission

Please respond to the invitation email with a link to your complete repository.

> If you have any problems or are unsure about any of the steps please email technology@casort.org
