FROM python:3.11
WORKDIR /app
COPY patients.csv .
CMD ["python", "validation.py"]