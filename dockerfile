FROM python:3.11

WORKDIR /app

COPY dependances.txt .

RUN pip install -r dependances.txt

COPY . .

EXPOSE 8501

CMD [ "streamlit", "run", "app.py", "--serveur.address=0.0.0.0" ]