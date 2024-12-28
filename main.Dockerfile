FROM python:3.9-slim

RUN pip install fastapi uvicorn transformers

COPY main.py /main.py

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]