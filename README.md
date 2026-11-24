# Career Agent

**Status: In Active Development**

A small FastAPI foundation for a future career-assistance service. The current repository intentionally contains only the API skeleton, a health check, and an initial career preference model; it does not yet include agent workflows or recommendations.

## Implemented today

- FastAPI application entry point
- `GET /health` readiness endpoint
- Initial Pydantic `CareerPreference` model
- Local setup and environment examples

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` for the generated API documentation or request `http://127.0.0.1:8000/health`.

## Roadmap

- [ ] Add preference and conversation endpoints
- [ ] Add structured career guidance workflows
- [ ] Connect to the Career Match Engine
- [ ] Introduce LangGraph orchestration
- [ ] Add Redis-backed session state
- [ ] Add automated tests and deployment configuration

The roadmap describes planned work, not currently available features.
