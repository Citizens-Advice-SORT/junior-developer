.PHONY: install model dev backend frontend

# Install backend and frontend dependencies, then download the model
install:
	cd backend && uv sync
	cd frontend && npm install
	$(MAKE) --no-print-directory model

# Download the redaction model (about 1.2 GB, only the first time) and check it loads
model:
	cd backend && uv run python -c "from gliner2 import GLiNER2; from app.config import get_settings; GLiNER2.from_pretrained(get_settings().model_id); print('Model ready')"

# Run backend and frontend together (Ctrl+C stops both)
dev:
	$(MAKE) --no-print-directory -j2 backend frontend

# Run the FastAPI backend on http://localhost:8000
backend:
	cd backend && uv run fastapi dev

# Run the Next.js frontend on http://localhost:3000
frontend:
	cd frontend && npm run dev
