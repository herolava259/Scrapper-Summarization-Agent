FROM python:3.11-slim

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8501

RUN mkdir ~/.streamlit

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "interactive_ui.py", "--server.port=8501", "--server.address=0.0.0.0"]