FROM python:3.11
WORKDIR /app
COPY validate.py .
COPY patients.csv .
CMD ["python", "validate.py"]