# Project Structure

This service follows a layered FastAPI layout.

## Layout

app/
- exceptions/
  - custom_exceptions.py
  - handlers.py
- init/
  - database.py
- routers/
  - health.py
  - feedback.py
- services/
  - feedback.py
- models/
  - feedback.py
- schemas/
  - feedback.py
- main.py

## Run

- Ensure env var DATABASE_URL is set.
- Install deps: pip install -r requirements.txt
- Start: uvicorn app.main:app --reload

