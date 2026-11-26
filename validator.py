import csv

seen_ids = set()
with open('patieents.csv', 'r') as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader, start=2):
      if not row['age']:
          print(f"Row {i} FAILED - age is missing.")
      elif not row['patient_id'] in seen_ids:
          print(f"Row {i} FAILED - FAILED - duplicates patient_id {row['patient_id'] }.")
      elif len (row['visit_date']) != 10:
          print(f"Row {i} FAILED - date format wrong.")
    else:
        print(f"Row {i} OK")
        seen_ids.add(row['patient_id'])