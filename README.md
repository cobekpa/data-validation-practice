# Patient Data Validation

Validates hospital patient records using Python + Docker.

## What it checks
- Duplicates patient_id
- Missing age
- Empty rows ignored

## How to run
'''bash
docker build -t validation
docker run validation
