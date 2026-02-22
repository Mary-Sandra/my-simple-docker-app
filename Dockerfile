# 1. Use Python
FROM python:3.12-slim

# 2. Put your script into the container
COPY app.py .

# 3. Run it
CMD ["python", "app.py"]
