FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["sh", "-c", "python init_db.py && python app.py"]

EXPOSE 5000
CMD ["python", "app.py"]